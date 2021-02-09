import json
from thor_devkit import cry

def read_json_file(path_like: str) -> dict:
    ''' Read json file '''
    with open(path_like, 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    b = read_json_file('./core/build/contracts/UniswapV2Pair.json')
    h = bytes.fromhex(b['bytecode'])
    digest, _ = cry.keccak256([h])
    print('UniswapV2Pair init_code_hash:', digest.hex())
