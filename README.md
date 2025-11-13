# CSV_Manager
A Python-based command-line tool for performing cleaning, searching, replacing, and displaying operations on CSV files using pandas.
🧾 CSV File Manager
A powerful Python-based command-line tool for efficiently managing and cleaning CSV files.
It provides a safe and interactive environment for performing essential operations like data cleaning, record searching, value replacement, and file saving, with built-in backup and recovery features.
🚀 Features
File Validation – Ensures the entered CSV file exists and loads correctly.
Data Cleaning –
Remove rows containing missing values.
Delete unnecessary columns.
Restore from the previous backup if needed.
Search Functionality – Instantly locate records using the “Name” index.
Value Replacement – Replace specific values across any column with summary counts.
Display Options – Show either the complete dataset or a structured preview.
Backup and Restore – Automatically keeps a copy of the previous dataset before major modifications.
Save Changes – Option to safely write all in-memory changes back to the original CSV file.
Robust Error Handling – Prevents crashes through detailed input validation and exception handling.
⚙️ Technologies Used
Language: Python 3.10+
Libraries:
pandas — for data manipulation and file operations
os — for file path validation
sys — for safe exits and control flow
🧠 How It Works
The user provides a valid CSV file path.
The program loads the dataset and sets "Name" as the index.
Users can choose from operations like cleaning, searching, replacing, displaying, saving, or restoring data.
Before destructive changes, a backup is automatically created.
The user can choose to save modifications to disk anytime.
🧰 Future Enhancements
Add column-based search across all fields (not just index).
Include logging and user action tracking.
Provide more advanced filtering and sorting options.
👤 Author
Developed by Shravan Mahale.