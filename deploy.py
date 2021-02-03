'''
Deploy the Uniswap automatically on VeChain.
'''
import time
import secrets
import json
import requests
from thor_devkit import abi, cry, transaction

NETWORK = 'https://solo.veblocks.net'
CHAIN_TAG = int('a4', 16)

DEVELOPER = {
    'address': '0x7567d83b7b8d80addcb281a71d54fc7b3364ffed',
    'private': 'dce1443bd2ef0c2631adc1c67e5c93f13dc23a41c18b536effbbdcbcdb96fb65'
}

TARGETS = {
    'vvet': 'vvet/build/contracts/VVET9.json',
    'factory': 'core/build/contracts/UniswapV2Factory.json',
    'router': 'periphery/build/contracts/UniswapV2Router02.json'
}

VTHO_CONTRACT = '0x0000000000000000000000000000456e65726779'


def read_json_file(path_like: str) -> dict:
    with open(path_like, 'r') as f:
        return json.load(f)


def get_bytecode(contract_meta: dict, key: str = 'bytecode') -> bytes:
    ''' Get bytecode from contract meta data '''
    return bytes.fromhex( contract_meta[key] )


def build_params(types: list, args: list) -> bytes:
    ''' ABI encode params '''
    return abi.Coder.encode_list(types, args)


def _build_url(base: str, tail: str) -> str:
    return base.rstrip('/') + '/' + tail.lstrip('/')


def best_block(network: str) -> dict:
    ''' Get best block '''
    url = _build_url(network, 'blocks/best')
    r = requests.get(url, headers={'accept':'application/json'})
    if not (r.status_code == 200):
        raise Exception(f'Cant connect to {url}')
    return r.json()


def _calc_blockRef(block: dict) -> str:
    ''' Calculate blockRef from a block '''
    return block['id'][0:18]


def _calc_nonce() -> str:
    return int(secrets.token_hex(8), 16)


def build_tx(priv:str, network:str, chainTag: int, to: str, value: int, data: str, gas: int, dependsOn=None) -> str:
    block = best_block(network)
    blockRef = _calc_blockRef(block)
    nonce = _calc_nonce()
    body = {
        "chainTag": chainTag,
        "blockRef": blockRef,
        "expiration": 32,
        "clauses": [
            {
                "to": to,
                "value": value,
                "data": data
            }
        ],
        "gasPriceCoef": 0,
        "gas": gas,
        "dependsOn": dependsOn,
        "nonce": nonce
    }

    tx = transaction.Transaction(body)
    priv_key = bytes.fromhex(priv)
    message_hash = tx.get_signing_hash()
    signature = cry.secp256k1.sign(message_hash, priv_key)
    tx.set_signature(signature)

    return '0x' + tx.encode().hex()


def post_tx(network: str, raw: str) -> str:
    ''' Post tx, get tx id '0x...' '''
    url = _build_url(network, 'transactions')
    r = requests.post(
        url,
        headers={
            'accept': 'application/json',
            'Content-Type': 'application/json'
        },
        json={"raw": raw }
    )
    if not (r.status_code == 200):
        raise Exception(f"Creation error? HTTP: {r.status_code} {r.text}")

    return r.json()['id']


def tx_receipt(network: str, tx_id: str) -> dict:
    url = _build_url(network, f'transactions/{tx_id}/receipt')
    r = requests.get(url, headers={'accept':'application/json'})
    if not (r.status_code == 200):
        raise Exception(f"Creation error? HTTP: {r.status_code} {r.text}")

    return r.json()


def is_reverted(receipt: dict) -> bool:
    return receipt['reverted']


def _find_created_contracts(receipt: dict) -> list:
    ''' Return a list of contract addresses created '''
    a = []
    for x in receipt['outputs']:
        if x.get('contractAddress'):
            a.append(x.get('contractAddress'))
    
    return a


def wait_for_receipt(network: str, tx_id: str):
    receipt = None
    for _ in range(5):
        if not receipt:
            time.sleep(3)
            receipt = tx_receipt(network, tx_id)
        else:
            break
    if not receipt:
        raise Exception("Cannot get receipt after a while, tx dropped?")
    else:
        return receipt


def deploy(network: str, chainTag: int, contract_meta: dict, types: list, params: list, priv: str, to: str, value: int, gas: int) -> str:
    print(f'Deploy: {contract_meta["contractName"]}')
    if not types:
        data_bytes = get_bytecode(contract_meta)
    else:
        data_bytes = get_bytecode(contract_meta) + build_params(types, params)
    data = '0x' + data_bytes.hex()
    # print(f'data: {data}')
    raw = build_tx(priv, network, chainTag, to, value, data, gas, None)
    tx_id = post_tx(network, raw)
    print(f'tx: {tx_id}')

    receipt = wait_for_receipt(network, tx_id)

    if is_reverted(receipt):
        raise Exception('reverted')
    else:
        addrs = _find_created_contracts(receipt)
        print(f"deployed on: {addrs[0]}")
        return addrs[0]


def call_function(network:str, chainTag: str, abi_dict: dict, func_params: list, priv: str, to: str, value: int, gas: int) -> str:
    f1 = abi.FUNCTION(abi_dict)
    print(f'call contract: {to} func: {f1["name"]} with params:', func_params)
    f = abi.Function(f1)
    data = f.encode(func_params, to_hex=True)

    raw = build_tx(priv, network, chainTag, to, value, data, gas, None)
    tx_id = post_tx(network, raw)
    print(f'tx: {tx_id}')

    receipt = wait_for_receipt(network, tx_id)

    if is_reverted(receipt):
        raise Exception('reverted')
    else:
        print('Call success')
    
    return tx_id


def find_func_abi(contract_meta: dict, func_name: str) -> dict:
    abis = contract_meta["abi"]
    for each in abis:
        if each.get('name') == func_name:
            return each


if __name__ == "__main__":
    # Deploy VVET
    vvet = read_json_file(TARGETS['vvet'])
    vvet_contract_addr = deploy(NETWORK, CHAIN_TAG, vvet, None, None, DEVELOPER['private'], None, 0, 3000000)
    
    # Deploy Factory
    factory = read_json_file(TARGETS['factory'])
    fee_to_setter = DEVELOPER['address']
    factory_contract_addr = deploy(NETWORK, CHAIN_TAG, factory, ['address'], [fee_to_setter], DEVELOPER['private'], None, 0, 3000000)

    # Deploy Router
    router = read_json_file(TARGETS['router'])
    router_contract_addr = deploy(NETWORK, CHAIN_TAG, router, ['address','address'], [factory_contract_addr, vvet_contract_addr], DEVELOPER['private'], None, 0, 5000000)
    
    # Create VVET/VTHO pair
    createPair_abi = find_func_abi(factory, 'createPair')
    if not createPair_abi:
        raise Exception("Cannot find createPair abi")
    
    call_function(NETWORK, CHAIN_TAG, createPair_abi, [vvet_contract_addr, VTHO_CONTRACT], DEVELOPER['private'], factory_contract_addr, 0, 2500000)
