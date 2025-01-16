# Gmail Sender Reader README

A Python script for sending emails through Gmail, with support for attachments.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)  ![License](https://img.shields.io/badge/License-MIT-green)  ![Gmail CLI](https://img.shields.io/badge/Gmail-CLI-red?style=flat&logo=gmail&logoColor=white&labelColor=gray) ![Gmail Python CLI](https://img.shields.io/badge/Gmail-Python%20CLI-blue?style=flat&logo=gmail&logoColor=white&labelColor=red)

# Master README

Welcome to the Gmail CLI Utilities repository. This repository contains tools for reading and sending Gmail messages via command line interfaces (CLIs). Below is a detailed guide on how to use each tool and additional information on setup and usage.

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
  - [Environment Variables](#environment-variables)
  - [Google App Password](#google-app-password)
- [Tools](#tools)
  - [ReadGmail](#readgmail)
    - [README_read_gmail_cli.md](#readme_read_gmail_climd)
    - [read_gmail_cli.py](#read_gmail_clip)
  - [SendGmail](#sendgmail)
    - [README1_send_cli_gmail1.md](#readme1_send_cli_gmail1md)
    - [send_cli_gmail1.py](#send_cli_gmail1py)
    - [README2_send_cli_gmail2.md](#readme2_send_cli_gmail2md)
    - [send_cli_gmail2.py](#send_cli_gmail2py)

## Overview

This repository includes tools for interacting with Gmail through the command line. The tools are organized into two main categories: **ReadGmail** and **SendGmail**. Each category contains a README file and corresponding Python scripts.

## Setup

### Environment Variables

To use these tools, you need to configure environment variables. The required variables include:

- `EMAIL_USER`: Your Gmail address
- `EMAIL_PASS`: Your Gmail password (use an [App Password](#google-app-password) if two-factor authentication is enabled)

Create a `.env` file in the root of the directory with the following structure:

```env
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
```

Ensure this file is correctly placed and not shared publicly.

### Google App Password

To use Gmail with these scripts, you must generate an App Password. This is especially important if you have two-factor authentication enabled. Follow these steps:

1. Go to your Google Account settings.
2. Navigate to **Security** and find the **App passwords** section.
3. Create a new App Password, which will be displayed as a 16-character string. It should be divided into 4 groups of 4 characters (e.g., `abcd-efgh-ijkl-mnop`).

Use this App Password in the `.env` file instead of your regular Gmail password.

## Tools

### ReadGmail

This directory contains tools for reading Gmail messages from the command line.

#### README_read_gmail_cli.md

This file provides detailed instructions on how to use the `read_gmail_cli.py` script. It covers setup, usage, and troubleshooting tips. Refer to this document for comprehensive guidance.

#### read_gmail_cli.py

This script allows you to read emails from your Gmail inbox. It connects to Gmail via IMAP, fetches messages, and displays them in the terminal. You can specify filters to search for specific messages.

### SendGmail

This directory contains tools for sending emails via Gmail from the command line.

#### README1_send_cli_gmail1.md

Provides instructions for the `send_cli_gmail1.py` script, detailing how to send emails with subject and body from the CLI.

#### send_cli_gmail1.py

A script for sending simple text emails. It prompts the user for the recipient's email address, subject, and message body, then sends the email via Gmail's SMTP server.

#### README2_send_cli_gmail2.md

This document explains the usage of `send_cli_gmail2.py`, including how to attach files and send emails with attachments.

#### send_cli_gmail2.py

Similar to `send_cli_gmail1.py` but with additional functionality for sending emails with attachments. Users can specify a file path to attach to the email.

## Important Notes

- Always keep your `.env` file secure and do not share it publicly.
- For more detailed information, refer to the specific README files in each subdirectory.

---

This structure ensures a clean and organized master README, directing users to specific sub-README files for more details and providing essential setup instructions. Let me know if there's anything specific you'd like to add or modify!

## Customization

You can easily customize the email subject and body by modifying the `subject` and `body` variables in the script.

## Security Notes

- Never commit your `.env` file to version control. Add it to your `.gitignore` file to prevent accidental commits.
- Use an App Password instead of your main Gmail password for added security.
- Ensure your email credentials are kept confidential.

## Troubleshooting

If you encounter issues:

1. Check that your Gmail account settings allow for less secure app access or that you're using a valid App Password.
2. Verify that your `.env` file is correctly formatted and contains the right credentials.
3. Ensure you're not being blocked by any firewall or antivirus software.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](link-to-your-issues-page).

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - [rangersmyth.74@gmail.com](mailto:your-email@example.com)

Project Link: [https://github.com/davidtkeane/gmail_single_cli/](https://github.com/yourusername/gmail-sender-script)

Made with ❤️ by David
