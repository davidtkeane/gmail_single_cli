# Gmail Sender Script

A Python script for sending emails through Gmail, with support for attachments.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)  ![License](https://img.shields.io/badge/License-MIT-green)  ![Gmail CLI](https://img.shields.io/badge/Gmail-CLI-red?style=flat&logo=gmail&logoColor=white&labelColor=gray)

![Gmail Python CLI](https://img.shields.io/badge/Gmail-Python%20CLI-red?style=flat&logo=gmail&logoColor=white&labelColor=blue)

![Gmail Python CLI](https://img.shields.io/badge/Gmail-Python%20CLI-blue?style=flat&logo=gmail&logoColor=white&labelColor=red)

![Gmail Python CLI](https://img.shields.io/badge/Gmail-Python%20CLI-white?style=flat&logo=gmail&logoColor=red&labelColor=blue)

![Gmail Python CLI](https://img.shields.io/badge/Gmail-Python%20CLI-fbbc04?style=flat&logo=gmail&logoColor=white&labelColor=ea4335)

## Description

This Gmail Sender Script is a versatile Python tool designed to send emails via Gmail's SMTP server. It provides a user-friendly interface for sending emails with or without attachments, making it suitable for various use cases such as automated notifications, personal communication, or integration into larger projects.

### Key Features:

- Send plain text emails through Gmail
- Option to include file attachments
- Interactive command-line interface for entering email details
- Error handling for failed email attempts

## Prerequisites

- Python 3.6 or higher
- A Gmail account
- Less secure app access enabled for your Gmail account, or an App Password if using 2-factor authentication
- Active internet connection

## Installation

1. Clone this repository or download the `send_cli_gmail2.py` file.
2. No additional Python packages are required as the script uses only standard library modules.

## Usage

1. Run the script:

   ```
   python send_cli_gmail2.py
   ```
2. Follow the prompts to enter:

   - Recipient's email address
   - Your Gmail address
   - Your Gmail password (or App Password)
   - Email subject
   - Email message
3. The script will attempt to send the email and will print a success message or an error if something goes wrong.

### Sending an Email with Attachment

To send an email with an attachment, modify the script slightly:

1. Open `send_cli_gmail2.py` in a text editor.
2. Find the line:
   ```python
   send_email(to_email)
   ```
3. Replace it with:
   ```python
   attachment_path = input("Enter the path to the attachment file (or press Enter to skip): ")
   send_email(to_email, attachment_path if attachment_path else None)
   ```

Now, when you run the script, it will ask for an attachment file path. You can either provide a path or press Enter to send without an attachment.

## Security Notes

- This script requires you to input your Gmail password. Make sure you're using this script in a secure environment.
- It's recommended to use an App Password instead of your main Gmail password.
- Never share your script or password with others.
- Be cautious when sending sensitive information via email.

## Troubleshooting

If you encounter issues:

1. Ensure that less secure app access is enabled in your Google Account settings, or use an App Password.
2. Check your internet connection.
3. Verify that you're using the correct email and password.
4. If using an attachment, make sure the file path is correct and the file exists.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/yourusername/gmail-sender-script/issues).

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

David Keane - [your-email@example.com](mailto:your-email@example.com)

Project Link: [https://github.com/yourusername/gmail-sender-script](https://github.com/yourusername/gmail-sender-script)

---

Made with ❤️ by David
