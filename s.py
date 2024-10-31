from helius import BalancesAPI

# Initialize the Balances API
balances_api = BalancesAPI("6e573dd9-f81c-4190-9661-db87c88a1bf4")

# Get the balances for the specified account
s = balances_api.get_balances("CrTU5929Vnk4sb7Cyfyo1M63JvzgSpFPm58JSyajDbd8")

# Print the entire dictionary to inspect its structure
print("Response structure:", s)

# Access the tokens list (adjust the key based on your structure)
tokens = s.get('tokens', [])  # Replace 'tokens' with the actual key if different

# Filter the tokens where the amount is greater than 100
filtered_tokens = [token for token in tokens if token['amount'] > 100]

# Print the filtered tokens
print(filtered_tokens)
