# Overview
The project is a decentralized anonymity network based on blockchain and smart contracts.

# Function
The project focuses on improving the directory functionality of the Tor system, and the main improvements include:
1. Use smart contracts to reconstruct the core functions of Tor directory authority to realize a decentralized directory authority (DDA);
2. Relays upload "descriptor" to DDA, and clients fetch directories from DDA;
3. Add some auxiliary functions on the basis of Tor (e.g., entity registration, random directory, data protection) to improve the system's resistance to directory attacks.

# Code
1. The client and relay of the system use the same code, named "BADNet.zip";
2. DDA is implemented by the Ethereum smart contract (Solidity language), and the code is shown in "Directory.sol".

# Deployment Method
1. The client and relay have their own deployment documents, respectively;
2. The code of DDA needs to be deployed on the Ethereum blockchain. Considering the cost of the system, it is recommended to deploy DDA on the Ethereum Ropsten Testnet, and the required transaction fees can be obtained through the “ETH Faucet”.

# Test method 1: Build your own private anonymity network
Users can download the source code and deploy their own DDA and relays to build a private anonymity network.

# Test method 2: Use the anonymous network system built by the project team

The project is currently maintaining a small anonymity network, including smart contract-based DDA that provides directory services, onion routers that provides relay services, and the client program for testing the network functionality.

The prototype system is still being continuously updated, and information about the currently available system is as follows:
- Source code: "2021-08-11" folder;
- DDA’s smart contract address: 0xC8fE2CEAc93Ad50e496B497357AE5385192Dd28D;
- Number of relays: 32;
- Relay "descriptor" update period: 10 minutes.

DDA update records:
1. Contract address: 0x459e359817606d22693eC6360960C9b8bCa254Ec;
Deployment date: July 15, 2021;
Status: discontinued operations as of July 20, 2021, with a total of 337 transactions.
2. Contract address: 0x376b3bc1c18809600ae5f0d9d82dbea8f31525cb;
Deployment date: July 20, 2021;
Status: discontinued operations as of August 10, 2021, with a total of 4,427 transactions.
3. Contract address: 0x1ed3b4ae0bcf62164a2622e3d357c68f09bc0fc4;
Deployment date: August 10, 2021;
Status: discontinued operations as of August 15, 2021, with a total of 5,608 transactions.
4. Contract address: 0xC8fE2CEAc93Ad50e496B497357AE5385192Dd28D;
Deployment date: August 15, 2021;
Status: this smart contract is in operation.

# Others

- rETH (Ropsten Ethereum) Faucet: 
https://faucet.dimensions.network/ or https://teth.bitaps.com/

- TESTNET Ropsten (ETH) Blockchain Explorer: 
https://ropsten.etherscan.io/
