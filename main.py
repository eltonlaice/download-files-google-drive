import os
import requests
import re

def extract_file_id(url):
    # Extract file ID from Google Drive link
    match = re.search(r'/d/([a-zA-Z0-9_-]+)', url)
    if match:
        return match.group(1)
    return None

def download_file(file_id, output_path):
    url = f"https://drive.google.com/uc?id={file_id}&export=download"
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {output_path}")
    else:
        print(f"Failed to download file with ID: {file_id}")

def main():
    # Create data directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    try:
        with open('links.txt', 'r') as f:
            links = f.readlines()
    except FileNotFoundError:
        print("Error: 'list.txt' not found. Please make sure the file exists in the current directory.")
        return

    # Download each file
    for link in links:
        file_id = extract_file_id(link.strip())
        if file_id:
            output_path = os.path.join('data', f"{file_id}.file")
            download_file(file_id, output_path)
        else:
            print(f"Invalid link: {link.strip()}")

if __name__ == "__main__":
    main()

