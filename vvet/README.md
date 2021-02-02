# VVET

## Veiled VET

Level with:

WETH9

https://github.com/gnosis/canonical-weth/commit/0dd1ea3e295eef916d0c6223ec63141137d22d67

## Problems:
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