# This example script create a pool between 2 tokens.
# Uni v2 contracts shall be already deployed.
# 2 tokens contracts shall be already deployed.
# Costs: about 2510 VTHO

import sys
from thor_requests.connect import Connect
from thor_requests.wallet import Wallet
from thor_requests.contract import Contract
from thor_requests import utils

# Read in Params
SCRIPT_NAME = sys.argv[0]
NETWORK = sys.argv[1] # eg. 'https://solo.veblocks.net'
PRIVATE_KEY = sys.argv[2]
FACTORY_FILE = sys.argv[3]
FACTORY_ADDRESS = sys.argv[4]
token_1_address = sys.argv[5]
token_2_address = sys.argv[6]

if not token_1_address:
    raise Exception("fill out the token 1 smart contract address")

if not token_2_address:
    raise Exception("fill out the token 2 smart contract address")

# Prepare wallet and network
w = Wallet.fromPrivateKey(bytes.fromhex(PRIVATE_KEY))
c = Connect(NETWORK)
factory_contract = Contract.fromFile(FACTORY_FILE)

if not utils.is_contract(c.get_account(FACTORY_ADDRESS)):
    raise Exception(f"{FACTORY_ADDRESS} is not a smart contract")

if not utils.is_contract(c.get_account(token_1_address)):
    raise Exception(f"{token_1_address} is not a smart contract")

if not utils.is_contract(c.get_account(token_2_address)):
    raise Exception(f"{token_2_address} is not a smart contract")

# Call on factory to create a pool of token 1 and token 2
response = c.commit(w, factory_contract, 'createPair', [token_1_address, token_2_address], FACTORY_ADDRESS)
tx_id = response['id']

# Wait for Receipt
receipt = c.wait_for_tx_receipt(tx_id, 30)
if not receipt:
    raise Exception(f"receipt not found! by tx id: {tx_id}")

# Print deployed address
if utils.is_reverted(receipt):
    print(c.replay_tx(tx_id))
    raise Exception(f"{tx_id} is reverted!")

print('createPair() call success, tx_id:', tx_id)
