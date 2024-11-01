import requests

# Set your Helius API key and other parameters
API_KEY = "6e573dd9-f81c-4190-9661-db87c88a1bf4"
WEBHOOK_URL = "https://d66b-88-97-51-83.ngrok-free.app/webhook" 
WALLET_ADDRESS = "CrTU5929Vnk4sb7Cyfyo1M63JvzgSpFPm58JSyajDbd8" 

# Define the endpoint and request payload
url = f"https://api.helius.xyz/v0/webhooks?api-key={API_KEY}"

payload = {
    "webhookURL": WEBHOOK_URL,
    "accountAddresses": [WALLET_ADDRESS],
    "transactionTypes": ["SWAP"],
}
# Make the request to register the webhook
response = requests.post(url, json=payload)

# Check if the webhook was successfully registered
if response.status_code == 200:
    print("Webhook successfully registered!")
    print("Response:", response.json())
else:
    print("Failed to register webhook:", response.status_code, response.text)
