# Gmail Terminal Reader

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)  ![License](https://img.shields.io/badge/License-MIT-green) ![Gmail CLI](https://img.shields.io/badge/Gmail-CLI-red?style=flat&logo=gmail&logoColor=white&labelColor=gray)

![Gmail Python CLI](https://img.shields.io/badge/Gmail-Python%20CLI-red?style=flat&logo=gmail&logoColor=white&labelColor=blue)

![Gmail Python CLI](https://img.shields.io/badge/Gmail-Python%20CLI-blue?style=flat&logo=gmail&logoColor=white&labelColor=red)

![Gmail Python CLI](https://img.shields.io/badge/Gmail-Python%20CLI-white?style=flat&logo=gmail&logoColor=red&labelColor=blue)

![Gmail Python CLI](https://img.shields.io/badge/Gmail-Python%20CLI-fbbc04?style=flat&logo=gmail&logoColor=white&labelColor=ea4335)

A Python script to read unread Gmail messages directly from your terminal.

## Description

The Gmail Terminal Reader is a command-line tool that allows you to fetch and read your unread Gmail messages without leaving your terminal. It's perfect for users who prefer command-line interfaces or want to quickly check their emails without opening a web browser.

### Features:

- Connect securely to Gmail using IMAP
- Fetch unread emails from your inbox
- Display a summary of unread emails (sender, subject, and preview)
- Read full email content for selected messages
- Secure credential management using environment variables

## Prerequisites

- Python 3.7 or higher
- A Gmail account
- Less secure app access enabled for your Gmail account, or an App Password if using 2-factor authentication

## Installation

1. Clone this repository or download the `read_gmail_cli.py` file.
2. Install the required package:

   ```
   pip install python-dotenv
   ```
3. Create a `.env` file in the same directory as the script with the following content:

   ```
   GMAIL_USERNAME=your_email@gmail.com
   GMAIL_APP_PASSWORD=your_app_password
   ```

   Replace `your_email@gmail.com` with your Gmail address and `your_app_password` with your App Password.

## Setting up Gmail App Password

If you're using 2-Factor Authentication (recommended), you'll need to create an App Password:

1. Go to your [Google Account Security settings](https://myaccount.google.com/security).
2. Under "Signing in to Google," select "App Passwords" (you may need to enable 2-Step Verification first).
3. At the bottom, choose "Select app" and "Other (Custom name)".
4. Enter "Gmail Terminal Reader" or any name you prefer.
5. Click "Generate".
6. Use the 16-character password that appears.

## Usage

1. Ensure your `.env` file is set up with the correct credentials.
2. Run the script:

   ```
   python read_gmail_cli.py
   ```
3. The script will connect to your Gmail account and fetch unread emails.
4. You'll see a list of unread emails with their sender, subject, and a preview.
5. Enter the number of the email you want to read or '0' to exit.
6. The full content of the selected email will be displayed.
7. You can continue to read other emails or exit the program.

## Troubleshooting

If you encounter issues:

1. Ensure your `.env` file is correctly set up with your Gmail address and App Password.
2. Check that you're using the correct App Password if you have 2-Factor Authentication enabled.
3. Verify your internet connection.
4. If the script seems to hang, it might be due to a large number of unread emails. You can modify the script to limit the number of emails fetched.

## Security Notes

- This script requires access to your Gmail account. Always keep your `.env` file secure and never share it.
- Using an App Password is more secure than your regular Gmail password.
- The script does not store or send your credentials anywhere; they are only used to authenticate with Gmail.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](link-to-your-issues-page).

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - [your-email@example.com](mailto:your-email@example.com)

Project Link: [https://github.com/yourusername/gmail-terminal-reader](https://github.com/yourusername/gmail-terminal-reader)

---

Happy Email Reading!

Made with ❤️ by David
