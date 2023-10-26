import sys
import json
from flask import Flask, request, jsonify, send_file
from waitress import serve
import pandas as pd
import ssl

from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'my_secret_key'
jwt = JWTManager(app)

@app.route("/sortie_active", methods=['GET', 'POST'])
def path_active():
    if request.method == 'GET':
        # Handle GET request
        # You can perform actions specific to GET requests here
        return jsonify({"message": "This is a GET request"})

    elif request.method == 'POST':
        try:
            if not request.is_json:
                return jsonify({"error": "Request does not contain JSON data"}), 400

            # Define a generator to stream and save the JSON data to a file
            json_file_path = 'Data///received_data.json'
            with open(json_file_path, 'wb') as json_file:
                for chunk in request.stream:
                    json_file.write(chunk)

            # Process the saved JSON file
            with open(json_file_path, 'rb') as json_file:
                json_data = json.load(json_file)
                df = pd.json_normalize(json_data)

            # Perform operations on the DataFrame 'df' as needed
            print("Received JSON Data:")
            print(df.to_string())

            # Return a response for POST requests
            return jsonify({"message": "Data received and processed successfully"})

        except json.decoder.JSONDecodeError as e:
            return jsonify({"error": "Invalid JSON format in the request"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500


# if __name__ == "__main__":
#     app.run(debug=True)

if __name__ == "__main__":
    # Define the paths to your SSL certificate and key files
    cert_path = 'path_to_your_certificate.crt'
    key_path = 'path_to_your_private_key.key'

    # Create an SSL context
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    ssl_context.load_cert_chain(cert_path, key_path)

    # Serve the app using Waitress with HTTPS
    serve(app, host='0.0.0.0', port=8000, url_scheme='https', ssl_context=ssl_context)