# Secret Santa Generator

This is a Python script that uses the Streamlit library to create a web-based Secret Santa generator. The script allows users to add participants, generate pairs, and send emails to participants with their Secret Santa assignments.

## Dependencies

- streamlit
- random
- smtplib
- pandas
- email.mime.multipart
- email.mime.text

## Classes

- `SessionState`: This class is used to maintain the state of the session. It stores the participants and pairs.

## Functions

- `create_message(to_name, from_name, budget, date, location)`: This function creates the message to be sent in the email.
- `get_state(**kwargs)`: This function gets the current state of the session.
- `send_email(to_name, to_email, from_name)`: This function sends an email to the participant with their Secret Santa assignment.

## Usage

1. Run the script.
2. Add participants either by uploading a CSV file or manually entering their names and email addresses.
3. Click 'Generate' to generate the Secret Santa pairs.
4. Click 'Send Emails' to send the emails to the participants.


```python
server.login('Your-Gmail-Email', 'Your-App-Password')
```

## SMTP Credentials

- Add SMTP credentials in the `send_email` function.

### Gmail SMTP Credentials:

- **SMTP Server:** `smtp.gmail.com`
- **Port:** `587`
- **Login:** Your Gmail email address
- **Password:** Your Gmail password

### App Password Generation (If 2-Step Verification is enabled):

- Go to your Google Account > Security > App Passwords.
- If not available, check if:
  - 2-Step Verification is set up for your account.
  - It's only set up for security keys.
  - Your account is through work, school, or another organization.
  - Advanced Protection is turned on.
- Choose the app and device, then Generate.
- Follow instructions to enter the 16-character App Password.

### Configuration and Security:

- Ensure proper permissions and settings in your email account for SMTP.
- For Gmail, consider enabling “Less secure app access” (not recommended) or use third-party services like SendGrid, Mailgun, or AWS SES.

### Disclaimer:

- Keep SMTP credentials secure.
- Do not share them or push to public repositories.

### Note:

- Verify necessary permissions and settings for sending emails through SMTP.
