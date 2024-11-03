import requests
import sys
from urllib.parse import quote

def send_request(url, payload):
    # URL encode the payload
    encoded_payload = quote(payload)
    # Construct the full URL with the encoded payload
    full_url = f"{url}?input={encoded_payload}"
    
    try:
        response = requests.get(full_url)
        print(f"Response Code: {response.status_code}")
        print(f"Response Body: {response.text[:500]}")  # Print first 500 chars of the response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python waf_bypass.py <url> <payload>")
        sys.exit(1)

    url = sys.argv[1]
    payload = sys.argv[2]

    print(f"Sending payload to {url}...")
    send_request(url, payload)

if _name_ == "_main_":
    main()