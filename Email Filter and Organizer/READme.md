This Python script connects to an IMAP and SMTP server, specifically Gmail in this example, to automate the processing of emails from a specific sender ("evoting@nsdl.com") in the "inbox" folder. Here's a short summary of what each function does:

1. connect_to_imap_server: Connects to the IMAP server using SSL and logs in with the provided email address and password.

2. connect_to_smtp_server: Connects to the SMTP server using TLS and logs in with the provided email address and password.

3. move_email_to_folder: Moves an email to a specified folder by copying it to the folder and then marking it as deleted before expunging it.

4. Fetch_and_Process: Selects the "inbox" folder, searches for emails from the specific sender, and processes them based on certain criteria. It extracts email content, creates a new email message, and moves the processed email to a folder named "Important."

5. main: Configures the email account settings (IMAP and SMTP server details, email address, and password), connects to the servers, and executes the Fetch_and_Process function to automate the processing of emails. Finally, it logs out of both servers.





