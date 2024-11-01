from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Webhook server is running!"

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.json
    print("Received webhook data: ", data)

    # Example of processing data
    if data.get('transactionType') == 'Any':
        # Process the transfer data as neededs
        print("Processing transfer transaction...")
    
    return jsonify({"status": "received"}), 200

if __name__ == '__main__':
    app.run(port=5000)