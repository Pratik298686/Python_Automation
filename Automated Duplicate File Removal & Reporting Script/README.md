- Project Name: File Duplicate Finder and Cleanup

- Purpose: This Python script is designed to help users find and manage duplicate files in a specified directory, and it provides the option to clean up those duplicates by moving them to a temporary trash directory.

- Features:

  - Scans a user-specified directory for duplicate files based on their content (using MD5 hashes).
  - Presents a list of duplicate files found in the directory.
  - Offers the option to move duplicate files to a temporary trash directory.
  - Maintains a log of deleted files in a text file with timestamps.
  - Provides an "Undo" feature to restore deleted files to their original locations.
  - Allows users to schedule regular cleanup tasks for deleted files.

- Usage:

  - Run the script with the absolute path of the target directory as a command-line argument.
  - Users can specify options like "-h" for help or "-u" for usage information.

- Cleanup Scheduling:

  - Users can choose to schedule regular cleanup tasks that run daily at a specific time (midnight by default) using the 'schedule' library.
  - The script offers the flexibility to enable or disable scheduled cleanup.

- Author: Developed by Marvellous Infosystems, attributed to Piyush Khairnar.

- Note: The script helps users manage duplicate files efficiently and provides an additional layer of safety by allowing file restoration through the "Undo" feature.
