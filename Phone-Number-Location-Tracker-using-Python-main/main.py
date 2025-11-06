import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium
import webbrowser

# User input
number_input = input("Enter phone number with country code (e.g., +917XXXXXXXXX): ")

try:
    parsed_number = phonenumbers.parse(number_input, None)
    region = geocoder.description_for_number(parsed_number, "en")
    service_provider = carrier.name_for_number(parsed_number, "en")

    print(f"Region: {region}")
    print(f"Carrier: {service_provider}")

    # OpenCage API key
    key = '3accd70e9136410889a6f91e739b591f'  # Replace with your working key
    geocoder_oc = OpenCageGeocode(key)

    # Get approximate lat/lng of the region
    result = geocoder_oc.geocode(region)
    if result:
        lat = result[0]['geometry']['lat']
        lng = result[0]['geometry']['lng']
        print(f"Latitude: {lat}, Longitude: {lng}")

        # Folium map
        map_ = folium.Map(location=[lat, lng], zoom_start=6)
        folium.Marker([lat, lng], popup=f"{region} ({service_provider})").add_to(map_)
        map_.save('location.html')
        print("Map saved as location.html and opening in browser...")
        webbrowser.open('location.html')

        # Open Google Maps
        webbrowser.open(f"https://www.google.com/maps?q={lat},{lng}")

    else:
        print("Could not find coordinates for this location.")

except phonenumbers.NumberParseException:
    print("Invalid phone number. Make sure to include country code.")
except Exception as e:
    print("Error:", e)
