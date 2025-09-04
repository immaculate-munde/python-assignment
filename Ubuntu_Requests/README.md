# 🌍 Ubuntu Image Fetcher  

> *“I am because we are” – Ubuntu Philosophy*  

The **Ubuntu Image Fetcher** is a mindful Python tool for downloading and organizing images from the web.  
It connects respectfully to the global community of shared resources, fetches images, and saves them for later sharing.  

---

## ✨ Features  

- 📥 Fetch images from one or multiple URLs  
- 📂 Saves all downloads in a `Fetched_Images/` directory  
- 🛡 Handles errors gracefully (e.g., bad URLs, connection issues)  
- 🔎 Extracts file names automatically (or generates one if missing)  
- 🖼 Prevents duplicate downloads  
- 🌐 Uses respectful headers to avoid 403 Forbidden errors  

---

## 🚀 Usage  

### 1. Clone the repository  
```bash

git clone https://github.com/your-username/Ubuntu_Requests.git
cd Ubuntu_Requests
2. Install dependencies
Make sure you have Python 3.10+ and install requests:
pip install requests

3. Run the program
python fetch_image.py

Enter one or more image URLs (comma separated):
https://upload.wikimedia.org/wikipedia/commons/3/3f/Fronalpstock_big.jpg, https://upload.wikimedia.org/wikipedia/commons/1/17/Google-flutter-logo.png

✅ Example Output
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter image URLs (comma separated): https://assets.ubuntu.com/v1/29985a98-ubuntu-logo32.png
✓ Successfully fetched: 29985a98-ubuntu-logo32.png
✓ Image saved to Fetched_Images/29985a98-ubuntu-logo32.png

Connection strengthened. Community enriched.
🌐 Example URLs for Testing
Nature photo:
https://upload.wikimedia.org/wikipedia/commons/3/3f/Fronalpstock_big.jpg

Flutter logo:
https://upload.wikimedia.org/wikipedia/commons/1/17/Google-flutter-logo.png

React logo:
https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg

Ubuntu logo:
https://assets.ubuntu.com/v1/29985a98-ubuntu-logo32.png

🔒 Precautions
Always verify sources before downloading images

Avoid overloading servers with too many requests

Respect copyright and licensing

💡 Ubuntu Principles in Code
Community → Connect to the wider web

Respect → Handle errors gracefully

Sharing → Save and organize fetched images

Practicality → Provide a useful real-world tool

