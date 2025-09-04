import requests
import os
import hashlib
import csv
from urllib.parse import urlparse
import uuid
from datetime import datetime

LOG_FILE = "download_log.csv"

def init_log():
    """Initialize CSV log file with headers if it doesn't exist"""
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp", "URL", "Filename", "Status", "Message"])

def log_entry(url, filename, status, message):
    """Write a log entry to the CSV file"""
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().isoformat(), url, filename, status, message])

def generate_filename(url):
    """Extract filename from URL or generate a unique one"""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename:  # If URL has no filename, create one
        filename = f"image_{uuid.uuid4().hex}.jpg"
    return filename

def file_already_exists(filepath, content):
    """Check if a file with the same content already exists"""
    if not os.path.exists(filepath):
        return False
    
    # Compare file hash to prevent duplicates
    with open(filepath, "rb") as f:
        existing_hash = hashlib.md5(f.read()).hexdigest()
    new_hash = hashlib.md5(content).hexdigest()
    return existing_hash == new_hash

def fetch_image(url, directory="Fetched_Images"):
    """Download and save an image from the web"""
    filename = generate_filename(url)
    filepath = os.path.join(directory, filename)

    try:
        # Ensure directory exists
        os.makedirs(directory, exist_ok=True)

        # Add a User-Agent header to avoid 403 Forbidden errors
        headers = {"User-Agent": "Mozilla/5.0 (UbuntuFetcher/1.0)"}
        response = requests.get(url, headers=headers, timeout=10, stream=True)
        response.raise_for_status()

        # Check important headers (content-type must be image/*)
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipping: URL is not an image ({content_type})")
            log_entry(url, filename, "Skipped", f"Not an image ({content_type})")
            return

        # Prevent duplicates
        if file_already_exists(filepath, response.content):
            print(f"⚠ Skipping duplicate image: {filename}")
            log_entry(url, filename, "Skipped", "Duplicate image")
            return

        # Save image
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        log_entry(url, filename, "Success", f"Saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
        log_entry(url, filename, "Error", str(e))
    except Exception as e:
        print(f"✗ An error occurred: {e}")
        log_entry(url, filename, "Error", str(e))

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    init_log()  # Make sure log file exists

    # Allow multiple URLs
    urls = input("Please enter image URLs (comma separated): ").split(",")

    for url in [u.strip() for u in urls if u.strip()]:
        fetch_image(url)

    print("\nConnection strengthened. Community enriched.")
    print(f"📑 Log saved to {LOG_FILE}")

if __name__ == "__main__":
    main()
