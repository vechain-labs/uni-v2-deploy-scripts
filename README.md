# Uniswap V2

// **Please note this is a draft and this code is under heavy development. NOT to be used in production.**


```
├── core        # uniswap-core
├── periphery   # uniswap-periphery
└── vvet        # WETH9
```

## Local Development
```bash
# Make sure you have python3
$ python3 --version
# Install dependencies (virtual env)
$ make install
# Compile all the contracts
$ make
# Deploy the contacts (default: solo network, with deployer 0x7567d83b7b8d80addcb281a71d54fc7b3364ffed)
$ make deploy
# Deploy with other options
$ make deploy private={private_key} network={http://....} chaintag={0x..}
```

## Testnet

Some contracts are deployed on testnet:

| Contract       | Address                                    |
| -------------- | ------------------------------------------ |
| vVET           | 0x37a3e90ff4a6eb312097367e0210d7d7d9699fdd |
| vtho           | 0x0000000000000000000000000000456e65726779 |
| factory        | 0xa876ea32b4540780a51fdf795a28ba1930231aa9 |
| router02       | 0x2ea79c98350d7d2bec2225f1bb7587d3fd355fa0 |
| vVET/VTHO pool | 0xc6ff007b5e42c270089f120f485e184e52c50f4b |
