# Uniswap V2

```
├── core        # uniswap-core
├── periphery   # uniswap-periphery
└── vvet        # WETH9
```

### Deploy steps:

0. Deploy vVET.sol (WETH9)
1. Deploy Factory.sol
2. Deploy Router02.sol
3. Since VTHO is already VIP180/ERC20, we don't need to deploy it. (address: 0x0000000000000000000000000000456e65726779)
4. Create a pair of vVET/VTHO on factory.sol
5. Approve vVET to router02.sol
6. Approve VTHO to router02.sol
7. Call "addLiquidity(tokenA, tokenB)" on router02.sol
8. Get Quote from the router02.sol
9. Swap vVET and VTHO.

### Testnet

0. vVET.sol:
```
deployer: 0x422D582C08d7965cD5Fefef1572faaA15783f473
tx_id: 0xbe319f78cf32bd728bbbb2632f4c3678d6c0745e253863c9450072c1a763cc08
contract_addr: 0xcFc6be8bB30FBAc8cECF8f943810eE0C561b4F7a
```

1. factory.sol:
```
deployer: same above
tx_id: 0xa7852d00bb21d958aa8f08fbe21314b5214a762626bc71a000abb58a33080b68
contract_addr: 0xfa00742a63f20B4a867cfd0758bf3bd39B5ce6af
```

2. router02.sol:
```
deployer: same above
tx_id: 0xb821efaef2e1ced5608a8a80b4bb30f05d54e9f0778369565a649833e63a72ec
contract_addr: 0x084b404b3A75e22Aa015b88eb160D22D3a81e719
```

3. vtho.sol:
```
contract_addr: 0x0000000000000000000000000000456e65726779
```

4. Create vVET/VTHO pair:
```
Created:

vVET/VTHO pair contract_addr: 0x306adfec67692dc0a3c4a6b2282be1d4877d98ca
```

5. Create 1000 vVET and approve 1000 vVET to router:
```
Call "deposit()" on vVET.sol and send 1000 VET to it, then it mints 1000 vVET.
then call "approve()" on vVET.sol to approve 1000 vVET to router02.
mint tx_id: 0x53c7bbe65cd7cb1549dba0e98a843d33b269408b5339ea866d7d04d019158d78
approve tix_id: 0x2d6a854aa67dae834de2db22de96c44c5c685794d9a6d6592e31e421f34afe96
```

6. Approve 1000 VTHO to router:
```
tx_id: 0x424aed831aea9efb7a45cb8bca0d1671c0623b291778d553e9b0ca058154e27a
```

7. Call addLiquidity() (vVET=1000, VTHO=1000) on router:
```
tx_id: 0x2fcafd793aff52e978ee57ba29ad962e108374529f4f7b98da5e1b242bff27fc
```

8. Call getAmountsIn / getAmountsOut on router to get price quote:
```
view type function won't need a tx_id
```
