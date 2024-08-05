#!/usr/bin/env python3
# Created by Ranger

# This works on Windows and Linux systems.
# This is a Python script that connects to your gmail account and gets your inbox emails.

# Usage information
# python read_gmail_cli.py

# What this script does:
# Modify the fetch_unread_emails function to handle attachments.
# The script requires an active internet connection to get the emails.
# The script requires a Gmail address and password to get the emails.

import imaplib
import email
import os
import socket
from email.header import decode_header
from dotenv import load_dotenv

def fetch_unread_emails():
    # Load environment variables
    load_dotenv()

    # Define the IMAP server and port
    IMAP_SERVER = "imap.gmail.com"
    IMAP_PORT = 993

    # Get credentials from environment variables
    USERNAME = os.getenv('GMAIL_USERNAME')
    PASSWORD = os.getenv('GMAIL_APP_PASSWORD')

    if not USERNAME or not PASSWORD:
        print("Error: Gmail credentials not found in environment variables.")
        print("Please set GMAIL_USERNAME and GMAIL_APP_PASSWORD in your .env file.")
        return

    try:
        # Connect to the IMAP server with a timeout
        print("Connecting to Gmail...")
        socket.setdefaulttimeout(30)  # 30 seconds timeout
        mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
        mail.login(USERNAME, PASSWORD)

        print("Connected successfully. Fetching unread emails...")
        # Select the inbox
        mail.select("inbox")

        # Search for unread emails
        status, messages = mail.search(None, 'UNSEEN')
        unread_messages = messages[0].split()

        # Check if there are any unread emails
        if not unread_messages:
            print("No unread emails found.")
            return

        print(f"Found {len(unread_messages)} unread emails. Fetching details...")
        email_summary = []
        for i, message in enumerate(unread_messages, 1):
            print(f"Fetching email {i} of {len(unread_messages)}...")
            # Fetch the email message by ID
            status, msg_data = mail.fetch(message, "(BODY.PEEK[])")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    subject = decode_header_str(msg["Subject"])
                    from_ = decode_header_str(msg.get("From"))
                    body = get_email_body(msg)
                    email_summary.append((from_, subject, body))

        # List the unread emails
        for i, summary in enumerate(email_summary, 1):
            print(f"{i}. From: {summary[0]}, Subject: {summary[1]}, Preview: {' '.join(summary[2].split()[:10])}")

        while True:
            try:
                choice = int(input("Enter the number of the email you want to read (or 0 to exit): ")) - 1
                if choice == -1:
                    print("Exiting...")
                    break
                elif 0 <= choice < len(email_summary):
                    print(f"\nFrom: {email_summary[choice][0]}\nSubject: {email_summary[choice][1]}\nBody: {email_summary[choice][2]}\n")
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    except imaplib.IMAP4.error as e:
        print(f"An IMAP error occurred: {e}")
        print("Please check your credentials and ensure you're using an App Password if 2FA is enabled.")
    except socket.timeout:
        print("Connection timed out. Please check your internet connection and try again.")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        try:
            print("Logging out...")
            mail.logout()
        except:
            pass

def decode_header_str(header):
    decoded, encoding = decode_header(header)[0]
    if isinstance(decoded, bytes):
        return decoded.decode(encoding if encoding else 'utf-8', errors='replace')
    return decoded

def get_email_body(msg):
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                return part.get_payload(decode=True).decode(errors='replace')
    else:
        return msg.get_payload(decode=True).decode(errors='replace')

if __name__ == "__main__":
    fetch_unread_emails()