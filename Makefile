SHELL=/bin/bash

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
	. .env/bin/activate && pip3 install -r requirements.txt