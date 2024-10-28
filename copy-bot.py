from solana.rpc.api import Client
from solders.pubkey import Pubkey


client = Client("https://api.mainnet-beta.solana.com")
wallet_address = "CrTU5929Vnk4sb7Cyfyo1M63JvzgSpFPm58JSyajDbd8"
pubkey = Pubkey.from_string(wallet_address)
balance_response = client.get_balance(pubkey)

# Access the balance value using the correct attribute
balance_lamports = balance_response.value

# Convert lamports to SOL
balance_sol = balance_lamports / 1_000_000_000

print(f"Balance: {balance_sol:.9f} SOL")