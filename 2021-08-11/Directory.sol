// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.7.0;
pragma experimental ABIEncoderV2;

contract Directory_v2{
    
    address owner;
    uint RelayUploadPeriod = 5;         // 5 minutes
    uint ClientUpdatePeriod = 60;       // 1 hour
    uint8 RIAlength = 6;
    uint16 relayIndex = 1;
    uint24 clientNum = 1;
    
    struct Client{
        bool registered;
        bool flag;
        uint24 clientIndex;
        uint16[] RIA;
    }
    mapping (address => Client) client;
    
    struct ClientKey {
        bytes publickey;
        mapping (uint16 => bytes) encryptedKey;
    }
    mapping (uint24 => ClientKey) clientKey;
    
    struct Relay{
        bool registered;
        bool flag;
        uint24[] clientlist;
        bytes encryptedSRI;
    }
    mapping (uint16 => Relay) relay;
    mapping (address => uint16) relayaddr;

    constructor(){
        owner = msg.sender;
    }
    fallback() external payable{}
    receive() external payable {}
    
    
    // ************************
    // Relay Method
    // ************************
    
    //Relay registration check.
    function relay_registration_check() public view returns (uint){
        if(relay[relayaddr[msg.sender]].registered == true){
            return 1;
        } else{
            return 0;
        }
    }
    
    //Relay registers.
    function relay_register() public{
        require(relay[relayaddr[msg.sender]].registered == false);
        uint16 num = relayIndex;
        relayaddr[msg.sender] = num;
        relay[num].registered = true;
        relay[num].flag = true;
        relay[num].clientlist = new uint24[](0);
        relayIndex++; 
    }
    
    //Relay gets SRI upload period (in minutes). 
    function relay_get_upload_period() view public returns (uint){
        return RelayUploadPeriod;
    }
    
    //Relay gets the length of its client list.
    function relay_get_clientlist_length() view public returns (uint){
        require(relay[relayaddr[msg.sender]].flag == true);
        return relay[relayaddr[msg.sender]].clientlist.length;
    }
    
    //Relay downloads public keys of clients (Loop download).
    function relay_download_clients_public_keys(uint i) view public returns (bytes memory){
        require(relay[relayaddr[msg.sender]].flag == true);
        require(i < relay[relayaddr[msg.sender]].clientlist.length);
        return clientKey[relay[relayaddr[msg.sender]].clientlist[i]].publickey;
    }
    
    //Relay incentive mechanism.
    function contract_transfer_to_relay(address payable addr) public payable{
        addr.transfer(0.0005 * 10**18);    //Transaction Fee (Gwei)
    }
    
    //Relay upload encrypted information and encrypted symmetric keys.
    function relay_upload_SRI_and_keys(bytes memory info, uint num, bytes[] memory keys) public{
        require(relay[relayaddr[msg.sender]].flag == true);
        uint16 index = relayaddr[msg.sender];
        relay[index].encryptedSRI = info;
        for(uint i=0; i<num; i++){
            clientKey[relay[index].clientlist[i]].encryptedKey[index] = keys[i];
        }        
        contract_transfer_to_relay(msg.sender);
    }
    
    //Relay upload encrypted symmetric keys.
    function relay_upload_keys(uint i, uint num, bytes[] memory keys) public{
        require(relay[relayaddr[msg.sender]].flag == true);
        require((i*5) <= relay[relayaddr[msg.sender]].clientlist.length);
        uint16 index = relayaddr[msg.sender];
        for(uint j=0; j<num; j++){
            clientKey[relay[index].clientlist[(i*5)+j]].encryptedKey[index] = keys[j];
        }
        contract_transfer_to_relay(msg.sender);
    }
    
    //Relay cancellation.
    function relay_cancellation() public{
        require(relay[relayaddr[msg.sender]].registered == true);
        delete relay[relayaddr[msg.sender]];
        delete relayaddr[msg.sender];
    }    
    
    
    // ************
    // Client
    // ************
    
    //Client registration check.
     function client_registration_check() public view returns (uint){
        if(client[msg.sender].registered == true){
            return 1;
        } else {
            return 0;
        }
    }
    
    //Client register.
    function client_register(bytes memory str) public{
        require(client[msg.sender].registered == false);
        client[msg.sender].registered = true;
        client[msg.sender].flag = true;
        client[msg.sender].clientIndex = clientNum;
        client[msg.sender].RIA = new uint16[](0);
        clientKey[client[msg.sender].clientIndex].publickey = str;
        clientNum++;
    }
    
    //Client gets RIA update period (in minutes). 
    function client_get_update_period() view public returns (uint){
        return ClientUpdatePeriod;
    }
    
    //Client gets the length of the RIA.
    function client_get_RIAlength() view public returns (uint8){
        require(client[msg.sender].flag == true);
        return RIAlength;
    }
    
    //Client gets the length of its current RIA.
    function client_get_current_RIA_length() view public returns (uint){
        require(client[msg.sender].flag == true);
        return client[msg.sender].RIA.length;
    }
    
    //PRIVATE: Create random number.
    function createRandom(address addr, uint8 j) private view returns (uint16){
        return uint16(uint(keccak256(abi.encodePacked(block.timestamp, block.difficulty, j, addr))) % (relayIndex-1) + 1);
    }
    
    //PRIVATE: Traverse an array to find duplicate values.
    function findIsIn(uint16[] storage array, uint16 key) private view returns (bool) {
    	if(array.length == 0){
    		return false;
    	}
    	for(uint i=0; i<array.length; i++){
    		if(array[i] == key){
    			return true;
    		}
    	}
    	return false;
    }

    //Generate random indexes for a client.
    function client_generate_random_index() public{
        require(client[msg.sender].flag == true);
        require(client[msg.sender].RIA.length < RIAlength);
        bool isIn;
        uint8 length = RIAlength + 2;
        uint16 a;
        for(uint8 i=0; i<length; i++){
            a = createRandom(msg.sender, i);
            if(relay[a].flag == true){
                isIn = findIsIn(client[msg.sender].RIA, a);
                if(!isIn){
        	        client[msg.sender].RIA.push(a);
        	        relay[a].clientlist.push(client[msg.sender].clientIndex);
                }
            }
            if(client[msg.sender].RIA.length == RIAlength){
                break;
            }
        }
    }
    
    //Clients download MSRI (Loop download).
    function client_download_MSRI(uint i) view public returns (bytes memory){
        require(client[msg.sender].flag == true);
        require(i < RIAlength);
        return relay[client[msg.sender].RIA[i]].encryptedSRI;
    }
 
    //Clients download symmetric keys (Loop download).
    function client_download_encrypted_keys(uint i) view public returns (bytes memory){
        require(client[msg.sender].flag == true);
        require(i < RIAlength);
        return clientKey[client[msg.sender].clientIndex].encryptedKey[client[msg.sender].RIA[i]];
    }
    
    //PRIVATE: Traverse an array to find duplicate values.
    function findIndexOf(uint24[] storage array, uint24 key) private view returns (uint) {
    	for(uint i=0; i<array.length; i++){
    		if(array[i] == key){
    			return i;
    		}
    	}
    	return array.length;
    }

    //Delete random indexes for a client and clientIndex in the corresponding clientlist.
    function client_delete_random_index() public{
        require(client[msg.sender].flag == true);
        require(client[msg.sender].RIA.length == RIAlength);
        uint locate;
        for(uint i=0; i<RIAlength; i++){
            locate = findIndexOf(relay[client[msg.sender].RIA[i]].clientlist, client[msg.sender].clientIndex);
            uint length = relay[client[msg.sender].RIA[i]].clientlist.length;
            if (locate < length-1){
                relay[client[msg.sender].RIA[i]].clientlist[locate] = relay[client[msg.sender].RIA[i]].clientlist[length-1];
                relay[client[msg.sender].RIA[i]].clientlist.pop();
            }
        }
        delete client[msg.sender].RIA;
    }
    
    //Client cancellation.
    function client_cancellation() public{
        require(client[msg.sender].registered == false);
        delete clientKey[client[msg.sender].clientIndex];
        delete client[msg.sender];
    } 
    
    
    // ************************
    // Manager Method
    // ************************
    
    //Get the number of clients.
    function getclientNum() view public returns (uint24){
        require(msg.sender == owner);
        return clientNum;
    }
    
    //Get the current index number.
    function getrelayIndex() view public returns (uint16){
        require(msg.sender == owner);
        return relayIndex;
    }
    
    //Set relay SRI upload period (in minutes).
    function setSRIperiod(uint period) public{
        require(msg.sender == owner);
        RelayUploadPeriod = period;
    }
        
    //Set client RIA generate period (in minutes).
    function setRIAperiod(uint period) public{
        require(msg.sender == owner);
        ClientUpdatePeriod = period;
    }

    //Set client RIA length.
    function setRIAlength(uint8 num) public{
        require(msg.sender == owner);
        RIAlength = num;
    }
    
    //Get the information about one relay.
    function getinfo(uint16 i) view public returns (bytes memory){
        require(msg.sender == owner);
        return relay[i].encryptedSRI;
    }    
    
   //Get random indexes.
    function getRIA(address addr) view public returns (uint16[] memory){
        require(msg.sender == owner);
        return client[addr].RIA;
    }
    
    //Get authflag of a relay.
    function getRelayFlag(uint16 i) view public returns (bool){
        require(msg.sender == owner);
        return relay[i].flag;
    }

    //Actively modify authflag of a malicious relay.
    function modifyRelayFlag(uint16 i, bool flag) public{
        require(msg.sender == owner);
        relay[i].flag = flag; 
    }
        
    //Get authflag of a client.
    function getClientFlag(address Addr) view public returns (bool){
        require(msg.sender == owner);
        return client[Addr].flag;
    }
    
    //Actively modify authflag of a malicious client.
    function modifyClientFlag(address Addr, bool flag) public{
        require(msg.sender == owner);
        client[Addr].flag = flag;
    }
}
