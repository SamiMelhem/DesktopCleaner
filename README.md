# Desktop Cleaner

## Description
Desktop Cleaner is a Python script designed to help organize files in your download folder by automatically moving them to predefined directories. It works by mapping file names to specific folders based on user-defined shortcuts at the end of file names.

## Features
* Automatically moves files from the download folder to specific directories.
* Supports custom folder mappings based on file name shortcuts.
* Handles duplicate files by renaming them to avoid overwriting.
* Logging for tracking file movements and potential issues.

## Installation
To use Desktop Cleaner, you need to have Python installed on your system. If you do not have Python installed, you can download it from [python.org](URL).

## Setup
1. Clone the Repository

&nbsp;&nbsp;&nbsp;Clone the repository to your local machine:

```markdown
git clone https://github.com/your-username/desktop-cleaner.git
cd desktop-cleaner
```

2. Configure Folder Paths

&nbsp;&nbsp;&nbsp;Open the 'desktop_cleaner.py' script in a text editor and set the 'download_folder' and &nbsp;&nbsp;&nbsp;'org_system_folder_names'&nbsp;to match your desired download folder and organization structure.

&nbsp;&nbsp;&nbsp;Example:
```python
download_folder = "C:\\Users\\username\\Downloads"
org_system_folder_names = {
    'shortcut': "C:\\Path\\To\\Your\\Folder",
    # Add more mappings here
}
```
## Usage
To run the script, use the following command in the terminal:

```bash
python desktop_cleaner.py
```

## Testing
It's recommended to test the script in a controlled environment with test files.
1. Set up a test environment with dummy download and destination folders.
2. Modify the script to point to these test folders.
3. Create test files with various names to cover different scenarios.
4. Run the script and verify that files are moved to the correct locations.

## Contributions
Contributions to Desktop Cleaner are welcome. Please ensure that your code adheres to the existing style and includes proper documentation.
