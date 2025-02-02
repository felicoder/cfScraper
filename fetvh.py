import requests

url = "http://127.0.0.1:1050/getCF"
payload = {
    "url": "https://fetlife.com/join",
    "delay": 5,
    "headless": False,
}

response = requests.post(url, json=payload)

# Print raw response for debugging
print("Raw Response:", response.text)

# Try to parse JSON only if response is not empty
if response.text.strip():
    print(response.json())
else:
    print("Empty response from server.")
