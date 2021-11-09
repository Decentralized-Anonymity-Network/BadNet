# BADNet
BADNet: A Blockchain-Based Anti-Attack Decentralized Anonymity Network

### Overview
The project is a decentralized anonymity network based on blockchain and smart contracts, which makes use of two open source projects, Tor and Ethereum.

### BADNet-0.3
BADNet (version 0.3) is build based on Tor version 0.4.6.5 and Ropsten Ethereum Testnet. Specifically, circuit-related operations are derived from the Tor source code, but Tor Directory Authority is replaced by DDA written in Solidity (DDA's code is in Directory.sol). We also provide a patch file (badnet.patch) for readers to track our changes to the Tor code.

### Function
The project focuses on improving the directory functionality of the Tor network, and the main improvements include:
1. Use smart contracts to reconstruct the core functions of Tor directory authority to realize a decentralized directory authority (DDA).
2. Relays upload server descriptors to DDA, and clients fetch directories from DDA.
3. Add some auxiliary functions on the basis of Tor (e.g., entity registration, random directory, data protection) to improve the system's resistance to directory attacks.

### Setup
1. The client and relay have their own setup documents, respectively.
2. The code of DDA needs to be deployed on the Ethereum blockchain. Considering the cost of the system, it is recommended to deploy DDA on the Ropsten Ethereum Testnet, and the required transaction fees can be obtained through the "ETH Faucet".

### Test method 1: Build your own private anonymity network
Users can download the source code and deploy their own DDA and relays to build a private anonymity network.

### Test method 2: Use the anonymous network system built by the project team
The project is currently maintaining a small anonymity network, including smart contract-based DDA that provides directory services, onion routers that provides relay services, and the client program for testing the network functionality.

The prototype system is still being continuously updated, and information about the currently available system is as follows:
- Source Code: BADNet
- DDA’s Contract Address: [0xC8fE2CEAc93Ad50e496B497357AE5385192Dd28D](https://ropsten.etherscan.io/address/0xC8fE2CEAc93Ad50e496B497357AE5385192Dd28D)
- Deployment Date: August 15, 2021
- Number of Relays: 12
- Descriptor's Upload Period: 10 minutes

DDA update records:
- Contract Address: [0x1ed3b4ae0bcf62164a2622e3d357c68f09bc0fc4](https://ropsten.etherscan.io/address/0x1ed3b4ae0bcf62164a2622e3d357c68f09bc0fc4)
- Deployment Date: August 10, 2021
- Status: discontinued operations as of August 15, 2021
- Total Number of transactions: 5,608

### Others
- Ropsten Ethereum (rETH) Faucet: [Faucet1](https://faucet.dimensions.network/)
 or [Faucet2](https://teth.bitaps.com/)
- [Ropsten Testnet Explorer](https://ropsten.etherscan.io/)
