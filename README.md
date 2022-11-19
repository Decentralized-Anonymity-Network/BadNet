# BADNET
BADNET: A Blockchain-Based Decentralized Anonymity Network

### Overview
The project is a decentralized anonymity network based on onion routing and blockchain, which makes use of two open source projects, Tor and Ethereum.

### BADNET-1.0
BADNET (version 1.0) is build on top of Tor version 0.4.6.5 and the Goerli Ethereum Testnet. The onion routing technique is derived from the Tor source code, but BADNET hides the Tor Directory Authority (DirAuth) behind an Ethereum system. More concretely, directory services are not provided directly by the DirAuth, but are supported through an Ethereum smart contract (SC) written in Solidity. The code for the directory contract is in *DirectoryContract.sol*. We also provide a patch file *badnet.patch* for readers to track our changes to the Tor code.

### Setup
1. The client and relay have their own setup documents, respectively (see the folder *Setup*).
2. The code of the SC needs to be deployed on an Ethereum blockchain. We currently deploy the SC on the Goerli Testnet and the required transaction fees can be obtained through the "ETH Faucet".

### Test method 1: Build your own private anonymity network
Users can download the source code and then build a private anonymity network by creating their own smart contracts and running a number of relays.

### Test method 2: Use the anonymity network built by our team
Our project is currently maintaining a small-scale anonymity network, including a smart contract that provides directory services, onion routers that provides relay services, and the client program for testing the network functionality.

The prototype system is still being tested and continuously updated. Details of the current system are as follows:
- Source Code: BADNET
- Contract Address: [0x2C6DBBdB60C75d4E72ACfba11d2e5FCaf25F25c1](https://goerli.etherscan.io/address/0x2c6dbbdb60c75d4e72acfba11d2e5fcaf25f25c1)
- Deployment Date: November 19th, 2022
- Number of Relays: 12
- Descriptor's Upload Period: 1 hour

Update records (BADNET-0.3):
- Contract Address: [0xC8fE2CEAc93Ad50e496B497357AE5385192Dd28D](https://ropsten.etherscan.io/address/0xC8fE2CEAc93Ad50e496B497357AE5385192Dd28D)
- Ethereum: Ropsten Testnet (already discontinued in October 2022)
- Deployment Date: August 15th, 2021
- Status: discontinued on October 5th, 2022
- Total Number of transactions: 9,204

### Others
- Goerli Faucet: [FAUCETLINK](https://faucetlink.to/goerli)
- Goerli Testnet Explorer: [Etherscan](https://goerli.etherscan.io/)
