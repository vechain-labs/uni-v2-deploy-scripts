# This example script deposit intial funds into the pool.
# Costs: about  VTHO

import sys
import time
from thor_requests.connect import Connect
from thor_requests.wallet import Wallet
from thor_requests.contract import Contract
from thor_requests import utils

# Read in Params
SCRIPT_NAME = sys.argv[0]
NETWORK = sys.argv[1] # eg. 'https://solo.veblocks.net'
PRIVATE_KEY = sys.argv[2]
ROUTER02_FILE = sys.argv[3]
ROUTER02_ADDRESS = sys.argv[4]
token_1_address = sys.argv[5]
token_2_address = sys.argv[6]
ERC20_FILE = sys.argv[7]
token_1_amount = int(sys.argv[8])
token_2_amount = int(sys.argv[9])

if not token_1_address:
    raise Exception("fill out the token 1 smart contract address")

if not token_2_address:
    raise Exception("fill out the token 2 smart contract address")

# Prepare wallet, network, contract
w = Wallet.fromPrivateKey(bytes.fromhex(PRIVATE_KEY))
c = Connect(NETWORK)
router02_contract = Contract.fromFile(ROUTER02_FILE)
erc20_contract = Contract.fromFile(ERC20_FILE)

if not utils.is_contract(c.get_account(ROUTER02_ADDRESS)):
    raise Exception(f"{ROUTER02_ADDRESS} is not a smart contract")

if not utils.is_contract(c.get_account(token_1_address)):
    raise Exception(f"{token_1_address} is not a smart contract")

if not utils.is_contract(c.get_account(token_2_address)):
    raise Exception(f"{token_2_address} is not a smart contract")

# Call to approve() vtho to be used by router02
response = c.transact(w, erc20_contract, 'approve', [ROUTER02_ADDRESS, token_2_amount], token_2_address)
tx_id = response['id']
receipt = c.wait_for_tx_receipt(tx_id, 30)
if not receipt:
    raise Exception(f"receipt not found! by tx id: {tx_id}")

assert utils.is_reverted(receipt) == False
print(tx_id)


# Call to deposit vet and vtho
response = c.transact(w, router02_contract, 'addLiquidityETH', [token_2_address, token_2_amount, round(token_2_amount * 0.9), round(token_1_amount * 0.9), w.getAddress(), int(time.time()) + 1000], ROUTER02_ADDRESS, token_1_amount)
tx_id = response['id']
receipt = c.wait_for_tx_receipt(tx_id, 30)
if not receipt:
    raise Exception(f"receipt not found! by tx id: {tx_id}")

assert utils.is_reverted(receipt) == False
print(tx_id)
