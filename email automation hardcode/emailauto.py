import smtplib
import os
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

# Email credentials (hardcoded for testing purposes)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "adamyasood7@gmail.com"  # Replace with your email
SENDER_PASSWORD = "nsaiultcmdpunvnr"  # Replace with your password

# List of recipients
recipients = ['soodadamya24@gmail.com']  # Replace with actual recipients

# Function to send email
def send_weekly_email():
    current_date = datetime.now().strftime("%Y-%m-%d")  # Get current date

    for recipient in recipients:
        try:
            # Create the email object
            message = MIMEMultipart()
            message['From'] = SENDER_EMAIL
            message['To'] = recipient
            message['Subject'] = f"Important!! Your cloud report this week - {current_date}"

            # Email body
            body = "Here is your weekly cloud anomaly report."
            message.attach(MIMEText(body, 'plain'))

            # Attach PDF (ensure this file exists or replace with a valid file)
            pdf_filename = "weekly_cloud_anomaly_report.pdf"  # Make sure this file exists
            if os.path.exists(pdf_filename):
                with open(pdf_filename, "rb") as attachment:
                    mime_base = MIMEBase('application', 'octet-stream')
                    mime_base.set_payload(attachment.read())
                    encoders.encode_base64(mime_base)
                    mime_base.add_header('Content-Disposition', f'attachment; filename={os.path.basename(pdf_filename)}')
                    message.attach(mime_base)
            else:
                print(f"File {pdf_filename} not found. Skipping attachment.")

            # Establish a connection with the server
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)

            # Convert message to string and send
            text = message.as_string()
            server.sendmail(SENDER_EMAIL, recipient, text)

            print(f"Email successfully sent to {recipient}")
        except Exception as e:
            print(f"Failed to send email to {recipient}: {str(e)}")
        finally:
            server.quit()

# Schedule the task weekly on Monday at 09:00 AM
schedule.every().monday.at("09:00").do(send_weekly_email)

# For testing purposes, you can send emails every minute:
schedule.every(1).minutes.do(send_weekly_email)  # Uncomment for testing every minute

# Run scheduler
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait for 1 minute before checking again
