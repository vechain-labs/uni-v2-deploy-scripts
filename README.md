# Uniswap V2 Deployement Tools.

Please clone `uni-v2` and `vvet` repos alongside repo.

// **Please note this is a draft and this code is under heavy development. NOT to be used in production.**

## Local Development
```bash
# Make sure you have python3
$ python3 --version
# Install dependencies (virtual env)
$ make install
# Compile all the contracts
$ make deploy
# Calculate init code hash from given json file
$ make hash compiledfile={solc_output_file.json}
# Deploy with other options
$ make deploy private={private_key} network={http://....} chaintag={0x..}
```

## Testnet

Currently, some contracts are deployed on `testnet`:

| Contract       | Address                                    |
| -------------- | ------------------------------------------ |
| vVET           | 0x535b9a56c2f03a3658fc8787c44087574eb381fd |
| vtho           | 0x0000000000000000000000000000456e65726779 |
| factory        | 0x8d77f31c128c88b52a148167cdc5439cb4bb11db |
| router02       | 0x4c2204ebc042197a728bfe1a771301177d018e32 |
| vVET/VTHO pool | 0x40d1a9b8b27d4f6799513575b957aaf1e0688d8a |
