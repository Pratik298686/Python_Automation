Project Description:
The project focuses on automating the process of downloading email attachments from a designated email address and saving them to a specified folder on your local machine. It achieves this by connecting to an IMAP server, searching for emails from a specific sender, and downloading attachments of specific types (e.g., PDFs, images, HTML files) from those emails.

Key Components:

1. connect_to_imap Function: Establishes a secure connection to the IMAP server (in this case, Gmail) using provided credentials.

2. create_download_folder Function: Creates a download folder on your local machine if it doesn't already exist, where the downloaded attachments will be stored.

3. download_attachments Function: Searches for emails from a specified sender in the "Inbox" folder, retrieves attachments of specified types, and saves them to the designated download folder.

4. main Function: Configures the email account, specifies the sender's email address, defines the download folder path, and sets the types of attachments to be downloaded. It orchestrates the execution of the other functions to accomplish the task.

Usage:
To use this script, you need to provide your email address and password for authentication, specify the IMAP server details, set the sender's email address you want to filter by, and specify the folder where you want to save the downloaded attachments. Additionally, you can define the types of attachments you want to download.

Example:
In this specific example, the script is configured to download attachments from emails sent by "evoting@nsdl.com" and save them to the folder "C:\backup\Python\Testing folder\download." It is set to download attachments of types PDF, JPEG, PNG, and HTML.