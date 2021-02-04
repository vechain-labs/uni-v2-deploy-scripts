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
| vVET           | 0xcFc6be8bB30FBAc8cECF8f943810eE0C561b4F7a |
| vtho           | 0x0000000000000000000000000000456e65726779 |
| factory        | 0xfa00742a63f20B4a867cfd0758bf3bd39B5ce6af |
| router02       | 0x084b404b3A75e22Aa015b88eb160D22D3a81e719 |
| vVET/VTHO pool | 0x306adfec67692dc0a3c4a6b2282be1d4877d98ca |
