Project Summary: Automated Duplicate File Removal with Scheduling

This Python automation script allows users to clean up duplicate files within a specified directory. It offers the following key features:

1. Duplicate File Detection: The script traverses the user-specified directory, calculates the MD5 hash of each file, and identifies duplicate files based on their hash values.

2. Duplicate File Removal: Identified duplicate files are moved to a designated temporary directory, keeping only one copy in the original location. The path of each deleted file is logged in a history file.

3. Undo Functionality: Users can choose to undo the file deletions. The script moves the previously deleted files back to their original locations and updates the history file accordingly.

4. Scheduled Cleanup: Users can opt to schedule regular cleanup tasks. The script employs the schedule library to run the cleanup at a specified time daily.

This project is designed to help users efficiently manage their files by removing duplicates and can be a valuable addition to file management workflows.




