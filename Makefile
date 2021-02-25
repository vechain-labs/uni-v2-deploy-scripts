SHELL=/bin/bash

export network=http://solo.veblocks.net
export chaintag=0xa4
export private=dce1443bd2ef0c2631adc1c67e5c93f13dc23a41c18b536effbbdcbcdb96fb65 # address: 0x7567d83b7b8d80addcb281a71d54fc7b3364ffed
export vvet=vvet/build/contracts/VVET9.json
export factory=core/build/contracts/UniswapV2Factory.json
export router=periphery/build/contracts/UniswapV2Router02.json

# default: compile all contracts
contracts:
	. .env/bin/activate && cd core && brownie compile
	. .env/bin/activate && cd periphery && brownie compile
	. .env/bin/activate && cd vvet &&  brownie compile

# clean up
clean:
	rm -r core/build/*
	rm -r vvet/build/*
	rm -r periphery/build/*

# install compiler tools
install:
	python3 -m venv .env
	. .env/bin/activate && pip3 install wheel
	. .env/bin/activate && pip3 install -r requirements.txt

# Deploy contracts to networks
deploy:
	. .env/bin/activate && python3 deploy.py $(private) $(network) $(chaintag) $(vvet) $(factory) $(router)
