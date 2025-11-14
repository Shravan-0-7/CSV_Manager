# CSV_Manager

A Python-based command-line tool for performing cleaning, searching, replacing, and displaying operations on CSV files using pandas.

## Features

### ✔️ File Validation
- Ensures the entered CSV file exists and loads correctly.

### 🧹 Data Cleaning
- Remove rows containing missing values.
- Delete unnecessary columns.
- Restore from previous backup.

### 🔍 Search Functionality
- Instantly locate records using the “Name” index.

### 🔄 Value Replacement
- Replace specific values across any column with summary counts.

### 📊 Display Options
- Show either the complete dataset or a structured preview.

### 💾 Backup and Restore
- Automatically keeps a copy of the previous dataset before major modifications.

### 💽 Save Changes
- Option to safely write all in-memory changes back to the original CSV file.

### 🛡 Robust Error Handling
- Prevents crashes through detailed input validation and exception control.
