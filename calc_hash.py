import json
import sys
from thor_devkit import cry

def read_json_file(path_like: str) -> dict:
    ''' Read json file '''
    with open(path_like, 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    file_path = './core/build/contracts/UniswapV2Pair.json'
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    b = read_json_file(file_path)
    h = bytes.fromhex(b['bytecode'])
    digest, _ = cry.keccak256([h])
    print('UniswapV2Pair init_code_hash:', digest.hex())
