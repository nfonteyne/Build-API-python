import requests
import json
from tqdm import tqdm
import os

# Replace with the actual URL of your Flask API endpoint
url = 'http://127.0.0.1:5000/sortie_active'

# Define the path to your large JSON file
json_file_path = 'output.json'

# Get the total file size for the progress bar
file_size = os.path.getsize(json_file_path)

# Define a generator to stream the JSON data from the file
def stream_json_file(file_path):
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(1024), b''):
            yield chunk

# Send the JSON data from the file as part of the POST request with a progress bar
try:
    with tqdm(total=file_size, unit='B', unit_scale=True) as progress_bar:
        response = requests.post(url, data=stream_json_file(json_file_path), headers={'Content-Type': 'application/json'}, stream=True)
        response.raise_for_status()
        print("Request successful!")

        # Process the response here if needed

    print("Response:", response.text)
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
