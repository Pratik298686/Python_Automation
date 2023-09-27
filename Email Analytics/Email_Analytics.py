import imaplib
import email
from email.header import decode_header
from nltk import FreqDist, word_tokenize



def main():
    # Define email credentials and server settings
    email_address = "pratikpadman125@gmail.com"
    emai_password = "maiy gyej qdil vmtu"
    imap_server = "imap.gmail.com"

    # Connect to the IMAP server
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(email_address, emai_password)
    mail.select("Inbox")

    # Fetch email IDs
    result, email_ids = mail.search(None, "ALL")
    email_id_list = email_ids[0].split()

    # Initialize data structures for analysis
    sender_frequency = {}
    common_keyword = []

    # Iterate through emails and analyze content
    for email_id in email_id_list:
        result, data = mail.fetch(email_id, "(RFC822)")
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)

        # Get the sender's email address
        sender = msg["From"]

        # Initialize the sender count to 0 if not already in the dictionary
        if sender not in sender_frequency:
            sender_frequency[sender] = 0
        
        sender_frequency[sender] += 1 

        # Parse the email subject and body
        subject = msg["Subject"]
        body = ""

        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))

                if "attachment" not in content_disposition:
                    payload = part.get_payload(decode=True)
                    if payload is not None:
                        body += payload.decode("UTF-8", "ignore")


        # Tokenize and analyze the email content

        tokens = word_tokenize(body.lower())
        common_keyword.extend(tokens)

    # Calculate the most common Keywords
    kkeyword_freq = FreqDist(common_keyword)
    most_common_keywords = kkeyword_freq.most_common(10)

if __name__ == "__main__":
    main()