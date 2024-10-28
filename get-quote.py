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