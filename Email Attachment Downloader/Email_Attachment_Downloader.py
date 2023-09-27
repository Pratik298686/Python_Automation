import email
import os
import imaplib

def connect_to_imap(EMAIL_ADDRESS,EMAIL_PASSWORD,IMAP_SERVER,IMAP_PORT):
    # Connect to the IMAP server
    imap = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    imap.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    return imap

def create_download_folder(download_folder):
    # Create the download folder if it doesnt exist
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

def download_attachments(imap, FOLDER_NAME, SAVE_FOLDER, attachment_types,sender_email):
    # Select the folder to seracch for emails
    imap.select('Inbox')

    # Search for emails with specific attachment types
    search_criteria = f'(FROM "{sender_email}")'
    result, email_ids = imap.search(None, search_criteria)

    # Iterate through the found email IDs and download attachments
    for email_id in email_ids[0].split():
        email_data = imap.fetch(email_id, "(BODY.PEEK[])")[1][0][1]
        msg = email.message_from_bytes(email_data)

        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type.lower() in attachment_types:
                filename = part.get_filename()
                if filename:
                    filepath = os.path.join(SAVE_FOLDER, filename)
                    f = open(filepath, 'wb')
                    f.write(part.get_payload(decode=True))
                    print(f"Downloaded attachment: {filename}")

def main():
    # Email account configuration
    EMAIL_ADDRESS = 'pratikpadman125@gmail.com'
    EMAIL_PASSWORD = 'maiy gyej qdil vmtu'
    IMAP_SERVER = 'imap.gmail.com'
    IMAP_PORT = 993
    FOLDER_NAME = "INBOX" 
    SENDER_EMAIL = "evoting@nsdl.com"

    # Folder to save attachments
    SAVE_FOLDER = r'C:\backup\Python\Testing folder\download'

    # Types of attachments to download (e.g, PDF, images)
    attachment_types = ["application/pdf", "image/jpeg", "image/png","text/html"]

    imap = connect_to_imap(EMAIL_ADDRESS,EMAIL_PASSWORD,IMAP_SERVER,IMAP_PORT)
    create_download_folder(SAVE_FOLDER)
    download_attachments(imap, FOLDER_NAME, SAVE_FOLDER, attachment_types,SENDER_EMAIL)

if __name__ == '__main__':
    main()