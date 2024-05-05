# send_participants_mail_cert.py
import os
from dotenv import load_dotenv
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from PIL import Image
from fpdf import FPDF
import datetime
from smtp_handler import SMTPHandler
from smtp_configurations import smtp_servers  # Import SMTP configurations

# Load environment variables from .env file
load_dotenv()

# Instantiate SMTPHandler with SMTP configurations
smtp_handler = SMTPHandler(smtp_servers)

def send_email(to_email, certificate_path_png, certificate_path_pdf):
    # Email configurations
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    subject = "Certificate of Completion"

    # Email content
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = subject

    # Participant's name formatting
    name = to_email.split('@')[0].replace('.', ' ').title()
    name_with_prefix = f"Scholar {name}"

    body = """\
    <html>
      <body>
        <p>Dear {name},</p>
        <p>Congratulations on completing the 2-Day Intensive Training on Office Suites [Word, Excel, and Powerpoint] with The Liberian Student Union in China (LSUIC) - Academic Excellence Committee (AEC) in collaboration with Teah Innovative Tech (TIT) on May 2-3, 2024. Your dedication and hard work throughout the training were truly commendable. We hope this experience has equipped you with valuable skills that will serve you well in your academic and professional journey.</p>
        <p>Thank you for your participation!</p>
        <p>Best regards,<br>Academic Excellence Committee <br>Liberian Student Union in China</p>
      </body>
    </html>
    """.format(name=name_with_prefix)

    message.attach(MIMEText(body, 'html'))

    # Attach PNG certificate
    with open(certificate_path_png, "rb") as attachment_png:
        certificate_png = MIMEBase('application', 'octet-stream')
        certificate_png.set_payload(attachment_png.read())
        encoders.encode_base64(certificate_png)
        certificate_png.add_header('Content-Disposition',
                                   "attachment; filename= %s" % certificate_path_png.split("/")[-1])
        message.attach(certificate_png)

    # Attach PDF certificate
    with open(certificate_path_pdf, "rb") as attachment_pdf:
        certificate_pdf = MIMEBase('application', 'octet-stream')
        certificate_pdf.set_payload(attachment_pdf.read())
        encoders.encode_base64(certificate_pdf)
        certificate_pdf.add_header('Content-Disposition',
                                   "attachment; filename= %s" % certificate_path_pdf.split("/")[-1])
        message.attach(certificate_pdf)

    # Send email using SMTP handler
    try:
        status = smtp_handler.send_email(sender_email, sender_password, to_email, message.as_string())
        if status:
            print(f"Email sent to {to_email} with certificate attached.")
            # Log success for successful deliveries
            email_status.append({'Email': to_email, 'Status': 'Success'})
        else:
            print(f"Failed to send email to {to_email}")
            email_status.append({'Email': to_email, 'Status': 'Failed'})
    except Exception as e:
        print(f"Failed to send email to {to_email}: {str(e)}")
        email_status.append({'Email': to_email, 'Status': 'Failed'})

def generate_pdf_from_image(image_path, output_path):
    # Open image
    image = Image.open(image_path)

    # Calculate aspect ratio
    aspect_ratio = image.width / image.height

    # Create PDF
    pdf = FPDF(unit="pt", format=(image.width, image.height))
    pdf.add_page()
    pdf.image(image_path, 0, 0, w=image.width, h=image.height)

    # Save PDF
    pdf.output(output_path)

# Read email addresses from CSV
data = pd.read_csv('data/participants.csv')

# Note to be included in the email body
note = """
Congratulations on completing the 2-Day Intensive Training on Office Suites [Word, Excel, and Powerpoint] with The Liberian Student Union in China (LSUIC) - Academic Excellence Committee (AEC) in collaboration with Teah Innovative Tech (TIT) on May 2-3, 2024. Your dedication and hard work throughout the training were truly commendable. We hope this experience has equipped you with valuable skills that will serve you well in your academic and professional journey.
"""

# Path to the directory containing certificates
results_dir = "results"

# Track the status of each email
email_status = []

# Iterate through each participant's data
for index, row in data.iterrows():
    # Get participant's information
    name = row['Name']
    email = row['Email']

    # Send email with certificate attachments
    certificate_path_png = f"{results_dir}/{name.replace(' ', '_')}_certificate.png"
    certificate_path_pdf = f"{results_dir}/{name.replace(' ', '_')}_certificate.pdf"

    # Generate PDF from image
    generate_pdf_from_image(certificate_path_png, certificate_path_pdf)
    # Send email
    status = send_email(email, certificate_path_png, certificate_path_pdf)

# Print and save email status
output_filename = f'email_status_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
with open(output_filename, 'w') as f:
    f.write(f'Email Delivery Status:\n\n')
    for index, row in data.iterrows():
        email = row['Email']
        participant_id = row['ID']
        status_info = next((status for status in email_status if status['Email'] == email), None)
        if status_info:
            status = status_info['Status']
            f.write(f'ID: {participant_id}, Email sent to: {email}, Status: {status}\n')
            print(f'ID: {participant_id}, Email sent to: {email}, Status: {status}')
        else:
            f.write(f'ID: {participant_id}, Email sent to: {email}, Status: Not Sent\n')
            print(f'ID: {participant_id}, Email sent to: {email}, Status: Not Sent')

print(f'Email status saved to {output_filename}')

