# File Hash Checker

This Python script allows you to check the integrity of files by calculating their SHA-256 hash and storing it in a JSON file. You can check if files are new, unchanged, or have been modified based on their hashes. It supports both individual file processing and recursive folder scanning.

## Features
- Calculate SHA-256 hash of files.
- Track changes to files by comparing current hashes with stored hashes.
- Process individual files or entire folders.
- Store hash data in a JSON file for persistent tracking.

## Requirements
- Python 3.x
- `os`, `hashlib`, and `json` modules (included in Python's standard library)

## Installation

1. Clone or download the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project_directory>
   ```

## Usage

### Run the script
To start the script, simply run the Python file:
```bash
python file_hash_checker.py
```

### Options
When you run the script, you’ll be prompted with the following options:
1. **Process a single file**: This option allows you to check the hash of a specific file.
2. **Process all files in a folder**: This option will recursively process all files within a specified folder.
3. **Exit**: Exit the program.

### How It Works

- **Single File**: The script will prompt you to enter the full path of a file. It will then calculate its SHA-256 hash and compare it with any existing hash stored in the `file_hashes.json` file.
  - If the file is new, it will be marked as "NEW FILE".
  - If the file's hash has changed, it will be marked as "CHANGED".
  - If the file’s hash is the same as the stored one, it will be marked as "UNCHANGED".

- **Folder**: You can also process an entire folder recursively. All files within the folder will be checked for changes, newness, or unchanged status.

### Hash Storage
The hashes of processed files are stored in a JSON file (`file_hashes.json`). This file is updated each time you run the script and track the changes to files.

## Example

```bash
Select an option:
1. Process a single file
2. Process all files in a folder
3. exit
Enter your choice (1/2/3): 2
Enter the full path to the folder: /path/to/folder
```

### Output
The script will print the status of each file as it processes them:
- `NEW FILE: <file_path>`
- `CHANGED: <file_path>`
- `UNCHANGED: <file_path>`

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Your Name (or Organization)
```

This README file provides an overview of the project, installation instructions, usage details, and how the script works, along with an example of interaction.
