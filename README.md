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

### Solo mode (https://solo.veblock.net)

0. vVET.sol:
deployer: 0x7567D83b7b8d80ADdCb281A71d54Fc7B3364ffed
tx_id: 0x06cdcde9746f32f4f6d59a3653a84647a2390776949dc240a879123cc785bdb0
contract_addr: 0xBC16695F74BA53E1a24e6c4aAbf3d5a09A9717CB

1. factory.sol:
deployer: same
tx_id: 0x8f31c394c28c94967ab4d1c417757ff8bfb8e193af89c80d9388fbd6c6911c91
contract_addr: 0x66433286EA26c5a3c96dE14DF4439D500aE64577

2. router02.sol:
deployer: same
tx_id: 0x123078e355a90194ae32cbe93b774fe6f4913f274a88966a542af25455aa777b
contract_addr: 0x9f69AdDD37560a131Dcc8f4a36dB366AE0157627

3. vtho.sol:
contract_addr: 0x0000000000000000000000000000456e65726779

4. create vVET/VTHO pair:
vVET/VTHO pair contract_addr: 0x4b99961a3e7fd07001d6f0af91edf4d27b3203a1

5. Create 500 vVET and approve 100 vVET to router:
Call "deposit()" on vVET.sol and send some VET to it,
then call "approve()" on vVET.sol to approve.
tx_id: 0x0cab372aa9ca77d0c724fa2774bca208324a8c03648fbf02c3b14fecf2b05a56

6. Approve 100 VTHO to router:
tx_id: 0xd3c67b520bca9603e0630515a866b284b9f75737ac73836c36c826729b3da4e7

7. Call addLiquidity() (vVET=100, VTHO=100) on router:
tx_id: 0xdc1f2929866e7fe8067a3f6a3e312eba77b9ba6bf9b24665b422f43ea2589b01

8. Call getAmountsIn / getAmountsOut on router to get price quote:
view type function won't need a tx_id

9. Swap 30 VTHO for VET (actually got 23 VET):
tx_id: 0xfb1ef1bccbf9623a1215480b148d2ed526e44c2e60e548ba627a228a30bb7317