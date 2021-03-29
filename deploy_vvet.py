# This script only deploys VVET smart contract.
# Inputs: network url, json file, deployer wallet
import sys
from thor_requests.connect import Connect
from thor_requests.wallet import Wallet

SCRIPT_NAME = sys.argv[0]
NETWORK = sys.argv[1] # eg. 'https://solo.veblocks.net'
PRIVATE_KEY = sys.argv[2]
VVET_FILE = sys.argv[3]

w = Wallet.fromPrivateKey(bytes.fromhex(PRIVATE_KEY))
c = Connect(NETWORK)

