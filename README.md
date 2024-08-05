
# Gmail Sender Script

A Python script for sending emails through Gmail, with support for attachments.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)  ![License](https://img.shields.io/badge/License-MIT-green)  ![Gmail CLI](https://img.shields.io/badge/Gmail-CLI-red?style=flat&logo=gmail&logoColor=white&labelColor=gray)

![Gmail Python CLI](https://img.shields.io/badge/Gmail-Python%20CLI-red?style=flat&logo=gmail&logoColor=white&labelColor=blue)

![Gmail Python CLI](https://img.shields.io/badge/Gmail-Python%20CLI-blue?style=flat&logo=gmail&logoColor=white&labelColor=red)

![Gmail Python CLI](https://img.shields.io/badge/Gmail-Python%20CLI-white?style=flat&logo=gmail&logoColor=red&labelColor=blue)

![Gmail Python CLI](https://img.shields.io/badge/Gmail-Python%20CLI-fbbc04?style=flat&logo=gmail&logoColor=white&labelColor=ea4335)

send_cli_gmail.py is a simple, secure Python script for sending emails through Gmail's SMTP server.

## Description

This Gmail Sender Script is a lightweight, easy-to-use Python tool designed to send emails via Gmail's SMTP server. It leverages environment variables for secure credential management and provides a straightforward way to send emails programmatically.

Key features:

- Secure handling of email credentials using environment variables
- Simple interface for sending emails
- Built-in error handling for robust operation
- Uses Gmail's SMTP server for reliable email delivery

Whether you're looking to send notifications from your applications, automate email responses, or just learn about sending emails with Python, this script provides a solid foundation to build upon.

## Prerequisites

- Python 3.7 or higher
- A Gmail account
- Less secure app access enabled for your Gmail account, or an App Password if using 2-factor authentication

## Installation

1. Clone this repository or download the `send_cli_gmail.py` file.
2. Install the required package:

   ```
   pip install python-dotenv
   ```
3. Create a `.env` file in the same directory as the script with the following content:

   ```
   FROM_EMAIL=your_email@gmail.com
   EMAIL_PASSWORD=your_app_password
   TO_EMAIL=recipient@example.com
   ```

   Replace the values with your actual email addresses and app password.

## Usage

1. Ensure your `.env` file is set up correctly with your email credentials.
2. Run the script:

   ```
   python send_cli_gmail.py
   ```
3. The script will attempt to send an email and will print a success message or an error if something goes wrong.

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

Your Name - [your-email@example.com](mailto:your-email@example.com)

Project Link: [https://github.com/yourusername/gmail-sender-script](https://github.com/yourusername/gmail-sender-script)

Made with ❤️ by David
