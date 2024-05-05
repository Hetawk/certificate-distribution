# Certificate Distribution System

This project automates the process of distributing certificates to recipients via email using SMTP servers. It eliminates the manual effort required for certificate distribution, especially when dealing with a large number of recipients.

## Inspiration

The inspiration behind this project comes from the challenges faced in distributing certificates manually, especially in organizations, firms, or educational institutions with a large number of recipients. Manual distribution can be time-consuming and inefficient, particularly when dealing with numerous recipients. This project aims to streamline the certificate distribution process and make it more efficient by automating the task.

## Features
- Read participant details from a CSV file.
- Load certificates image files and convert them to PDF.
- Sends personalized emails with certificates attached to each recipient including the image file and the generated PDF.
- Supports multiple SMTP servers for email delivery.
- Logs the delivery status of each email for tracking purposes.
- Easy setup and configuration for seamless execution.

## Project Setup

### Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- Pip (Python package manager)
- Git (optional for version control)

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/Hetawk/certificate-distribution.git
    ```

    Alternatively, download the project files as a ZIP archive and extract them to a local directory.

2. Navigate to the project directory:

    ```bash
    cd certificate-distribution
    ```

3. Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```
4. SMTP Configuration

   1. **Enable SMTP Access**: Many email providers require users to explicitly enable SMTP access for their accounts. This can usually be done through the account settings or security settings on the email provider's website. Look for options related to "SMTP" or "App Passwords" and follow the instructions to enable access.

   2. **Generate App Password (if needed)**: Some email providers, like Gmail, may require you to generate an "App Password" specifically for use with SMTP. This is a one-time password that allows applications to access your email without requiring your main account password. Generate the App Password following the provider's instructions and use it as the SMTP password in your application.

   3. **SMTP Server Settings**: Ensure you have the correct SMTP server address and port number for your email provider. These details are typically provided by the email service provider and may vary depending on the provider's infrastructure.

   4. **TLS/SSL Encryption**: It's recommended to use encrypted connections (TLS/SSL) when sending emails via SMTP to ensure security. Most email providers support TLS/SSL encryption, and you can usually enable this option in your SMTP client or library.

   5. **Test Configuration**: After setting up SMTP authentication, it's a good idea to test the configuration to ensure everything is working correctly. Send a test email from your application and verify that it's delivered successfully.

### Configuration

1. Create a `.env` file in the project root directory:

    ```plaintext
    SENDER_EMAIL=your_email_address
    SENDER_PASSWORD=your_email_password
    ```

    Replace `your_email_address` and `your_email_password` with your email credentials. These will be used to authenticate and send emails.

2. Customize the `participants.csv` file with the details of the participants for whom certificates need to be generated. Ensure the CSV file contains columns for `ID`, `Email`, `Name`, and `Sex`.

### Execution

Run the script `send_participants_mail_cert.py` to generate certificates and send emails to the recipients:

```bash
python send_participants_mail_cert.py
