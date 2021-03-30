# This script only deploys VVET smart contract.
# Usually costs 691 VTHO.
# Inputs: network url, json file, deployer wallet
import sys
from thor_requests.connect import Connect
from thor_requests.wallet import Wallet
from thor_requests.contract import Contract
from thor_requests import utils
# Read in Params
SCRIPT_NAME = sys.argv[0]
NETWORK = sys.argv[1] # eg. 'https://solo.veblocks.net'
PRIVATE_KEY = sys.argv[2]
VVET_FILE = sys.argv[3]

# Prepare wallet and network
w = Wallet.fromPrivateKey(bytes.fromhex(PRIVATE_KEY))
c = Connect(NETWORK)
vvet_contract = Contract.fromFile(VVET_FILE)

# Detect wallet balance
account = c.get_account(w.getAddress())
print('Wallet:')
print('VET:', int(account['balance'], 16) / (10 ** 18))
print('VTHO:', int(account['energy'], 16) / (10 ** 18))
print('Is human:', not utils.is_contract(account))

# Deploy
response = c.deploy(w, vvet_contract, None, None)
tx_id = response['id']
print('deploy_vvet_tx:', tx_id)

# Wait for Receipt
receipt = c.wait_for_tx_receipt(tx_id, 30)
if not receipt:
    raise Exception(f"receipt not found! by tx id: {tx_id}")

# Print deployed address
if utils.is_reverted(receipt):
    raise Exception(f"{tx_id} is reverted!")

deployed_addresses = utils.read_created_contracts(receipt)
for each in deployed_addresses:
    print('contract_vvet_created:', each)
