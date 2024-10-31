import requests
url = "https://quote-api.jup.ag/v6/quote"

spl_token_mint_address = '7WdDyHa7GDuAvYZAGFGEbDoBUka1S8YvbPgTW2WPpump'
buy_amount_in_sol = 1
buy_amount_correct_units = buy_amount_in_sol*1000

slippage_percent = 20

params = {'inputMint': 'So11111111111111111111111111111111111111112',
'outputMint': spl_token_mint_address,
'amount': buy_amount_correct_units, #units of sol/1000 - so here we are asking to buy 1 sol worth
"slippageBps": slippage_percent * 100} #1 basis point (bps) is equal to 0.01%

response = requests.request("GET", url, params=params)

print(response.text)

import requests

def get_circulating_supply(token_address):
    url = f"https://api.solscan.io/token/metadata?tokenAddress={token_address}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        
        # Check if the data contains 'data' field
        if 'data' in data and 'circulatingSupply' in data['data']:
            circulating_supply = data['data']['circulatingSupply']
            return circulating_supply
        else:
            print("No circulating supply data found.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Example token address (replace with the actual token mint address)
token_address = "7WdDyHa7GDuAvYZAGFGEbDoBUka1S8YvbPgTW2WPpump"  # Replace with the token mint address
circulating_supply = get_circulating_supply(token_address)

if circulating_supply is not None:
    print(f"Circulating Supply: {circulating_supply}")
