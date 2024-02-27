from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import time


# Function to send email
def send_email(to_address, subject, body):
    # Your email credentials
    sender_email = " "  # Your email address
    sender_password = " "  # Your email password

    # Setup the SMTP server
    smtp_server = ""
    smtp_port = 0

    # Create the MIME message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_address
    message["Subject"] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, "plain", "utf-8"))

    # Connect to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Log in to email account
        server.starttls()
        server.login(sender_email, sender_password)
        # Send the email
        server.sendmail(sender_email, to_address, message.as_string())


# Read email addresses from the file
with open("", "r") as file:
    email_addresses = file.readlines()

# Loop through each email address and send an email
for email_address in email_addresses:
    # Clean the email address (remove leading/trailing whitespaces)
    email_address = email_address.strip()
    # Email body
    body = f""" """  # Email body

    # Email subject
    subject = " "

    # Send email to each address
    send_email(email_address, subject, body)
    # Print the email address and the time the email was sent
    data = (
        "Email to "
        + email_address
        + ", has been send successfully at "
        + time.strftime("%Y-%m-%d %H:%M")
    )

    with open("/home/kali/Documents/hasBeenSend", "a") as file:
        file.write(data + "\n")
    # pause for * seconds for the next email to be sent (to avoid spamming)
    time.sleep(1000)
