# Factory + Pair

## Code

Level with:

uniswap-v2-core

https://github.com/Uniswap/uniswap-v2-core/commit/4dd59067c76dea4a0e8e4bfdda41877a6b16dedc

## Problems

EVM not compatible
```
chainid OPCODE is not available.

Fixed chainid = 1 in the constructor.
```

Deploy by hand the factory.sol constructor
```
Deploy with a constructor that has parameter: 

try to assemble the creation data as: <byte code><ABI encoded params list>

manually assemble via thor-devkit and upload by inspector
```
