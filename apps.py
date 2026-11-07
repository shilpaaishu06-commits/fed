from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# n8n Webhook URL
webhook_url = "PASTE_YOUR_N8N_TEST_URL_HERE"

@app.route('/send', methods=['POST'])
def send_data():

    data = request.get_json()

    # Send data to n8n
    response = requests.post(
        webhook_url,
        json=data
    )

    # Print response
    print("n8n Response:", response.text)

    return jsonify({
        "message": "Data sent to n8n successfully",
        "response": response.json()
    })

if __name__ == '__main__':
    app.run(debug=True)