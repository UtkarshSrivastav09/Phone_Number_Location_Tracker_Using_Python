📍 Phone Number Location Tracker (Python)

A simple Python project that allows you to track the approximate location and carrier details of a phone number using the phonenumbers library. This tool fetches publicly available geographical information based on the country/region prefix of the number — it does NOT access GPS or real-time location.

🚀 Features

Detects country/region of the phone number

Identifies the mobile carrier/service provider

Fetches approximate geographical area

Simple to use — just input a phone number with country code

Works on Windows / Linux / MacOS

🛠️ Technologies Used

Python 3.x

phonenumbers library

geocoder (for approximate location lookup)

folium (optional - for map visualization)

📦 Installation
git clone https://github.com/your-username/phone-number-location-tracker.git
cd phone-number-location-tracker
pip install -r requirements.txt

▶️ Usage
python main.py


Enter a phone number in international format, for example:

+1 202-555-0147
+91 9876543210
