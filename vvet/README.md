# VVET

Equals the WETH on Ethereum.

On Testnet:
Deployer: 0x422D582C08d7965cD5Fefef1572faaA15783f473
Deploy Tx: 0xad732d5799ed7239d2125125189611a070137c7884f1534f8777a550ea0159ec
Contract addr: 0x0685509C3e2492eB33084b2163c5f2F9971315B0

Operations:
Despoit 1 VET into it:
Tx: 0x5217ad4e51372bd04767c5389839f60dcc1ff4241915251185889b70a8c7fe3f

Problems:
```
// invalid opcode 0x47
// A new opcode, SELFBALANCE is introduced at 0x47

// https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1884.md

function totalSupply() public view returns (uint) {
        return address(this).balance;
}

// Fixed by:
Downgrade emv_verion from `Istanbul` to `Constantinople`
```