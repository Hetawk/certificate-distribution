# smtp_handler.py
import os
import smtplib

class SMTPHandler:
    def __init__(self, smtp_servers):
        self.smtp_servers = smtp_servers

    def send_email(self, sender_email, sender_password, to_email, message):
        for smtp_config in self.smtp_servers:
            if sender_email == smtp_config['sender_email']:
                smtp_server = smtp_config['smtp_server']
                smtp_port = smtp_config['smtp_port']
                break
        else:
            raise ValueError(f"No SMTP configuration found for sender email: {sender_email}")

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        try:
            server.sendmail(sender_email, to_email, message)
            print(f"Email sent to {to_email} using SMTP server: {smtp_server}")
            return True
        except Exception as e:
            print(f"Failed to send email to {to_email} using SMTP server {smtp_server}: {str(e)}")
            return False
        finally:
            server.quit()