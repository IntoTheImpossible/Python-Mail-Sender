# Project Name

Python-Mail-Sender

## Description

A simple Python script to send emails to multiple recipients using the `smtplib` library. The script reads a list of email addresses from a file, sends an email to each recipient, and records the email addresses along with the timestamp in a separate file to keep track of the sent emails.

## Installation

 Installation if Missing: If you encounter import errors, it's likely that the modules are missing. In that case, you might need to reinstall Python with the required modules or install them separately. For Python 3.x, you typically don't need to install anything extra to get these modules.

## Usage

1. **Setting up your email configuration**:
   - Replace the placeholder values for `sender_email`, `sender_password`, `smtp_server`, and `smtp_port` with your actual email credentials and SMTP server details. Make sure to use an email account that allows access for less secure apps or generate an app password if using Gmail.

2. **Preparing the email content**:
   - Define the email body and subject according to your requirements. You can customize the `body` and `subject` variables within the loop or keep them static if sending the same email content to all recipients.

3. **Reading email addresses from a file**:
   - Replace `""` with the path to the file containing the list of email addresses. Make sure each email address is on a separate line in the file.

4. **Sending emails**:
   - The script iterates through each email address read from the file, sends an email with the defined subject and body using the `send_email()` function, and records the email addresses along with the timestamp in a file named "hasBeenSend".

5. **Customizing pause time**:
   - Adjust the `time.sleep()` duration according to your preference. This time interval determines how long the script waits before sending the next email, helping to avoid spamming.

6. **Running the script**:
   - Run the script using `python send_emails.py`.

7. **Monitoring sent emails**:
   - After running the script, you can check the "hasBeenSend" file to verify which emails have been successfully sent.



