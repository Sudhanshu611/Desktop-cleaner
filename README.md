# Desktop Cleaner

Desktop Cleaner is a Python application that organizes your desktop by moving, deleting, or cleaning up specific file types according to user-defined configurations. Built with a simple graphical interface using Tkinter, the program sorts files into designated folders (e.g., Images, Documents, Videos, Music) and can remove old or unused files based on their age or type. 

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Logging](#logging)
- [Troubleshooting](#troubleshooting)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Features

- **File Organization**: Automatically moves files into folders based on their extensions.
- **File Deletion**: Deletes specified file types (e.g., `.exe`, `.iso`) and archives (e.g., `.zip`, `.rar`).
- **Old File Cleanup**: Removes files older than a user-defined threshold (default: 30 days).
- **User-Friendly GUI**: Tkinter-based interface for easy directory selection and program execution.
- **Logging**: Logs all actions to a `desktop_cleaner.log` file for tracking purposes.

## Installation

1. **Clone the Repository**:
   ```
   git clone https://github.com/Sudhanshu611/desktop_cleaner.git
   cd desktop_cleaner
   ```
2. **Install Dependencies**:
This application requires tkinter for the GUI and logging for action tracking, both included in Python's standard library.

3. **Run the Program**:
    ```
    python desktop_cleaner.py
    ```
## Usage
1. **Launch the Application**:
Run desktop_cleaner.py to open the desktop cleaner interface.

2. **Choose Directories**:
- Use the interface to set folders for organizing files:
    - Main Directory (the source for file cleanup)
    - Images Folder
    - Documents Folder
    - Music Folder
    - Videos Folder
3. **Execute the Cleanup**:

- Click Run the Program to start the cleanup process.
- The program will:
    - Delete files with unwanted extensions.
    - Move files with specific extensions to designated folders.
    - Remove files older than a defined threshold (default is 30 days).
## Configuration
- File Extensions: The program targets specific file extensions for deletion or sorting. Modify these in the code to suit different needs:

    - Delete: .exe, .iso, .zip, .rar
    - Move to Documents: .pdf, .docx, .ppt, .txt
    - Move to Images: .jpg, .jpeg, .png
- File Age: Modify the days_old parameter in older_file_remover() to set how old a file should be before it’s automatically removed.

## Logging
The program logs all activities in desktop_cleaner.log, including:

- Files that were deleted or moved
- Errors and warnings during execution
## Troubleshooting
- Tkinter Errors: Ensure tkinter is installed. If not included in your Python installation, run:

```
Copy code
sudo apt-get install python3-tk  # For Ubuntu
```
- Permission Errors: Make sure you have appropriate read/write permissions for the directories used.

## Dependencies
- `tkinter` - For the graphical interface
- `logging` - For logging activity
- `os`, `shutil`, `datetime`, `time` - Standard libraries for file operations
## Contributing
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed explanation of your changes.