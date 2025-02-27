from flask import Flask, request, jsonify

app = Flask(__name__)

# Text processing decorator
def ed(func):
    def wrapper(*args, **kwargs):
        # Retrieve the result from the decorated function
        result = func(*args, **kwargs)
        # You could add additional processing to the result here if needed
        return result
    return wrapper

# Text processing function that will be used with requests
@ed
def process_text(text):
    # This is where you would implement your text processing logic
    # For this example, we'll just return the text in uppercase
    return text.upper()

@app.route('/process', methods=['GET'])
def handle_request():
    # Get the text parameter from the query string
    text = request.args.get('text', '')
    
    if not text:
        return jsonify({"error": "No text provided. Use the 'text' query parameter."}), 400
    
    # Process the text using our function
    processed_text = process_text(text)
    
    # Return the processed text
    return jsonify({"original": text, "processed": processed_text})

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)