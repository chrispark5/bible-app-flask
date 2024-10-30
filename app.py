from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)

@app.route('/api/books', methods=['GET'])
def get_external_verse():
    # Get the API key from the request headers
    api_key = os.getenv('API_KEY')
    if not api_key:
        return jsonify({'error': 'API key is missing'}), 400  # Return error if API key is not provided

    # Replace this URL with the actual API endpoint you want to call
    api_url = 'https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/books'
    print(api_url)
    try:
        # Set the API key in the request header for the external API call
        headers = {
            'api-key': api_key  # Use the API key from the request
        }
        response = requests.get(api_url, headers=headers)  # Pass the headers
        response.raise_for_status()  # Raise an error for bad responses
        verse_data = response.json()  # Assuming the response is JSON
        return jsonify(verse_data)  # Return the data from the external API
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/books/<bookId>', methods=['GET'])
def get_book_details(bookId):
    # Get the API key from the request headers
    print(bookId)
    api_key = os.getenv('API_KEY')
    if not api_key:
        return jsonify({'error': 'API key is missing'}), 400  # Return error if API key is not provided

    # Replace this URL with the actual API endpoint you want to call
    api_url = f'https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/books/{bookId}/chapters'
    print(api_url)
    try:
        # Set the API key in the request header for the external API call
        headers = {
            'api-key': api_key  # Use the API key from the request
        }
        response = requests.get(api_url, headers=headers)  # Pass the headers
        response.raise_for_status()  # Raise an error for bad responses
        verse_data = response.json()  # Assuming the response is JSON
        return jsonify(verse_data)  # Return the data from the external API
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500
@app.route('/api/books/chapter/<chapterId>', methods=['GET'])
def get_book_details_2(chapterId):
    # Get the API key from the request headers
    print(chapterId)
    api_key = os.getenv('API_KEY')
    if not api_key:
        return jsonify({'error': 'API key is missing'}), 400  # Return error if API key is not provided

    # Replace this URL with the actual API endpoint you want to call
    api_url = f'https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/chapters/{chapterId}'
    print(api_url)
    try:
        # Set the API key in the request header for the external API call
        headers = {
            'api-key': api_key  # Use the API key from the request
        }
        response = requests.get(api_url, headers=headers)  # Pass the headers
        response.raise_for_status()  # Raise an error for bad responses
        verse_data = response.json()  # Assuming the response is JSON
        return jsonify(verse_data)  # Return the data from the external API
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)