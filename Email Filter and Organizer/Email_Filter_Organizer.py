import imaplib
import email
import smtplib
from email.mime.text import MIMEText

def connect_to_imap_server(IMAP_SERVER, EMAIL_ADDRESS, EMAIL_PASSWORD):
    imap_server = imaplib.IMAP4_SSL(IMAP_SERVER)
    imap_server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    return imap_server

def connect_to_smtp_server(SMTP_SERVER, EMAIL_ADDRESS, EMAIL_PASSWORD):
    smtp_server = smtplib.SMTP(SMTP_SERVER)
    smtp_server.starttls()
    smtp_server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    return smtp_server

def move_email_to_folder(imap_server, email_id, folder):
    # Move email to the specified folder
    imap_server.uid("COPY", email_id, folder)
    imap_server.uid("STORE", email_id, '+FLAGS', '(\Deleted)')
    imap_server.expunge()

def Fetch_and_Process(imap_server, smtp_server,EMAIL_ADDRESS, EMAIL_PASSWORD, FOLDER_TO_ORGANIZE):
    # select the inbox
    imap_server.select("inbox")

    # Search for emails from a specific sender
    sender = "evoting@nsdl.com"
    search_criteria = f'(FROM "{sender}")'
    status, email_ids = imap_server.search(None, search_criteria)
    # print(email_ids[0])
    # Fetch and Process emails
    if email_ids[0]:
        for email_id in email_ids[0].split():
            status, email_data = imap_server.fetch(email_id,"(RFC822)")
            raw_email = email_data[0][1].decode("utf-8", errors = 'ignore')
            email_message = email.message_from_string(raw_email)

            # Check if email meets criteria
            if sender in email_message["From"]:
                # Perform actions based on criteria
                msg = MIMEText("This email has been moved to the Important folder.")
                msg["Subject"] = email_message["Subject"]
                msg["From"] = EMAIL_ADDRESS
                msg["To"] = EMAIL_ADDRESS

                # Move the email to the specified folder
                move_email_to_folder(imap_server, email_id, FOLDER_TO_ORGANIZE)

def main():
    # Email account settings
    IMAP_SERVER = "imap.gmail.com"
    SMTP_SERVER = "smtp.gmail.com"
    EMAIL_ADDRESS = "pratikpadman125@gmail.com"
    EMAIL_PASSWORD = "maiy gyej qdil vmtu"
    FOLDER_TO_ORGANIZE = "Important"

    imap_server = connect_to_imap_server(IMAP_SERVER, EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp_server = connect_to_smtp_server(SMTP_SERVER, EMAIL_ADDRESS, EMAIL_PASSWORD)

    Fetch_and_Process(imap_server, smtp_server,EMAIL_ADDRESS, EMAIL_PASSWORD,FOLDER_TO_ORGANIZE)
    print("Email Processing Complete")
    imap_server.logout()
    smtp_server.quit()


if __name__ == "__main__":
    main()