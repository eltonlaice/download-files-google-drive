# Download Files from Google Drive

This Python script allows you to download files from Google Drive using file IDs.

## Features

- Read a list of Links from a text file
- Download specified files from Google Drive
- Save downloaded files to a local directory

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.7 or higher

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/eltonlaice/download-files-google-drive.git
   cd download-files-google-drive
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration

Create a file named `list.txt` in the project directory. Each line should contain a Google Drive file ID that you want to download.

## Usage

1. Ensure your `list.txt` file is populated with the Google Drive file IDs you wish to download.

2. Run the script using:
   ```
   python main.py
   ```

The script will read the file IDs from `list.txt` and download the specified files to a `downloads` directory in the project folder.

## Important Notes

- This script assumes that the files you're trying to download are publicly accessible or that you have the necessary permissions to access them.
- Make sure you have sufficient storage space for the files you're downloading.
- Be aware of Google Drive's usage limits and policies when using this script.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or feedback, please contact Elton Laice through GitHub [@eltonlaice](https://github.com/eltonlaice).