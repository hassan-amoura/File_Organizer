# File Organizer

## Overview
This script automates file organization by monitoring a specified directory and moving files into designated folders based on their extensions. It utilizes **Python's Watchdog** library to track file changes in real-time and **PyYAML** for configurable settings.

## Features
- **Real-time file monitoring** using Watchdog
- **Configurable destination folders** via `config.yaml`
- **Automatic renaming of duplicate files** to avoid overwrites
- **Multi-threaded execution** for efficiency
- **Command-line argument support** for flexibility

## Installation
### Prerequisites
Ensure you have Python installed (version 3.7+ recommended). Install the required dependencies:
```bash
pip install watchdog pyyaml
```

## Configuration
Edit `config.yaml` to customize directories:
```yaml
source_dir: "/users/hassan/Downloads"
dest_dirs:
  pdf: "/users/hassan/Hassan's Resumes"
  docx: "/users/hassan/Other Documents"
  jpg: "/users/hassan/Downloads/Pictures"
  jpeg: "/users/hassan/Downloads/Pictures"
  png: "/users/hassan/Downloads/Pictures"
  mp4: "/users/hassan/Downloads/Videos"
  mov: "/users/hassan/Downloads/Videos"
```

## Usage
Run the script with:
```bash
python file_organizer.py
```
Or specify a custom config file:
```bash
python file_organizer.py --config my_config.yaml
```

## How It Works
1. **Monitors** the `source_dir` for new or modified files.
2. **Moves files** to the appropriate destination folder based on extension.
3. **Renames duplicates** by appending a number to the filename.
4. **Runs in the background** until manually stopped.

## Stopping the Script
Press `CTRL + C` to terminate the script safely.

## License
This project is open-source and available for personal and professional use.


**Author:** Hassan

I am always learning and growing from the developers that I meet! If you have any suggestions on how to improve this, do not hesitate to reach out!

# file_organizer
