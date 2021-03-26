SHELL=/bin/bash

export solo_network=http://solo.veblocks.net
export solo_chaintag=0xa4
export solo_private=dce1443bd2ef0c2631adc1c67e5c93f13dc23a41c18b536effbbdcbcdb96fb65 # address: 0x7567d83b7b8d80addcb281a71d54fc7b3364ffed
export vvet=../vvet/vvet/build/contracts/VVET9.json
export factory=../uni-v2/uniswap-v2-core/build/UniswapV2Factory.json
export router=../uni-v2/uniswap-v2-periphery/build/UniswapV2Router02.json
export compiledfile=../uni-v2/uniswap-v2-core/build/UniswapV2Pair.json

# install compiler tools
install:
	python3 -m venv .env
	. .env/bin/activate && pip3 install wheel
	. .env/bin/activate && pip3 install -r requirements.txt

# Deploy Uni v2 + vVET contracts to networks
deploysolo:
	. .env/bin/activate && python3 deploy.py $(solo_private) $(solo_network) $(solo_chaintag) $(vvet) $(factory) $(router)

# Compute the bytecode hash of bytecode
hash:
	. .env/bin/activate && python3 calc_hash.py $(compiledfile)
