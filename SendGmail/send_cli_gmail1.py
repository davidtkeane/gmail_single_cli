#!/usr/bin/env python3
# Created by Ranger

# This works on Windows and Linux systems.
# This is a Python script that connects to your gmail account and sends an email.

# Usage information
# python send_cli_gmail.py

# What this script does:
# Modify the send_email function to handle attachments.
# The script requires an active internet connection to send the email.
# The script requires a Gmail address and password to send the email.

import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get email credentials from environment variables
from_email = os.getenv("EMAIL_USER_David")
password = os.getenv("EMAIL_PASS_David")
to_email = os.getenv("TO_EMAIL")

subject = "Email sent by Python Script"
body = "This email was sent using a Python script!"

# Create the email message
message = f"Subject: {subject}\n\n{body}"

try:
    # Create an SMTP object
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp_obj:
        # Start TLS encryption
        smtp_obj.starttls()
        
        # Login to the email account
        smtp_obj.login(from_email, password)
        
        # Send the email
        smtp_obj.sendmail(from_email, to_email, message)
    
    print("Email sent successfully!")

except Exception as e:
    print(f"An error occurred: {e}")