# This script deploys only Uni V2
# Inputs: network url, json files, deployer wallet, VVET contract address
# Factory deploy: about 3690 VTHO
# Router deploy: about 5740 VHTO
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
ROUTER_FILE = sys.argv[4]
VVET_CONTRACT_ADDRESS = sys.argv[5]

# Prepare wallet and network
w = Wallet.fromPrivateKey(bytes.fromhex(PRIVATE_KEY))
c = Connect(NETWORK)
factory_contract = Contract.fromFile(FACTORY_FILE)
router_contract = Contract.fromFile(ROUTER_FILE)
vvet_contract_address = VVET_CONTRACT_ADDRESS
if not vvet_contract_address:
    raise Exception("Set vVET contract address first!")

# Detect if VVET contract is ready
a = c.get_account(vvet_contract_address)
if not utils.is_contract(a):
    raise Exception(f"{vvet_contract_address} is not a smart contract")

# Detect wallet balance
account = c.get_account(w.getAddress())
print('Wallet balance:')
print('VET:', int(account['balance'], 16) / (10 ** 18))
print('VTHO:', int(account['energy'], 16) / (10 ** 18))
print('Is human:', not utils.is_contract(account))

# Deploy Factory
fee_to_setter = w.getAddress() # fee to setter is me.
response = c.deploy(w, factory_contract, ['address', 'address'], [fee_to_setter, vvet_contract_address])
tx_id = response['id']
print('deploy_factory_tx:', tx_id)

# Wait for Receipt
receipt = c.wait_for_tx_receipt(tx_id, 30)
if not receipt:
    raise Exception(f"receipt not found! by tx id: {tx_id}")

# Print deployed address
if utils.is_reverted(receipt):
    print(c.replay_tx(tx_id))
    raise Exception(f"{tx_id} is reverted!")

deployed_factory_addresses = utils.read_created_contracts(receipt)
factory_address = deployed_factory_addresses[0]
print('factory_address:', factory_address)

# Deploy Router
response = c.deploy(w, router_contract, ['address','address'], [factory_address, vvet_contract_address])
tx_id = response['id']
print('deploy_router_tx:', tx_id)

# Wait for Receipt
receipt = c.wait_for_tx_receipt(tx_id, 30)
if not receipt:
    raise Exception(f"receipt not found! by tx id: {tx_id}")

# Print deployed address
if utils.is_reverted(receipt):
    print(c.replay_tx(tx_id))
    raise Exception(f"{tx_id} is reverted!")

deployed_router_addresses = utils.read_created_contracts(receipt)
router_address = deployed_router_addresses[0]
print('router_address:', router_address)
