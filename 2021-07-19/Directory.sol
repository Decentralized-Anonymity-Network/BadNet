pragma solidity ^0.4.11;

contract Directory{
    
    address owner;
    uint16 relayIndex = 0;
    uint24 clientNum = 0;
    uint8 RIAnum = 6;
    
    struct Client{
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
        bool flag;
        uint24[] clientlist;
        bytes encryptedSRI;
    }
    mapping (uint16 => Relay) relay;
    mapping (address => uint16) relayaddr;

    //Set the address of the network manager.
    constructor() public{
        owner = msg.sender;
    }
    
    
    // ************
    // Relay
    // ************
    
    //Relay registration check.
     function relay_registration_check() public view returns (uint){
        if(relay[relayaddr[msg.sender]].flag == true){
            return 1;
        } else {
            return 0;
        }
    }
    
    //Relay registers, and returns its index.
    function relay_register() public{
        require(!relay[relayaddr[msg.sender]].flag);
        uint16 num = relayIndex;
        relayaddr[msg.sender] = num;
        relay[num].flag = true;
        relay[num].clientlist = new uint24[](0);
        relayIndex++; 
    }
    
    //Relay gets the length of its client list.
    function relay_get_clientlist_length() view public returns (uint){
        require(relay[relayaddr[msg.sender]].flag == true);
        return relay[relayaddr[msg.sender]].clientlist.length;
    }
    
    //Relay downloads public keys of clients (Loop download).
    function relay_download_clients_public_keys(uint i) view public returns (bytes){
        require(relay[relayaddr[msg.sender]].flag == true);
        return clientKey[relay[relayaddr[msg.sender]].clientlist[i]].publickey;
    }
    
    //Upload encrypted relay information and encrypted symmetric keys.
    function relay_upload_SRI_and_keys(bytes info, bytes keys) public{
        require(relay[relayaddr[msg.sender]].flag == true);
        relay[relayaddr[msg.sender]].encryptedSRI = info;
        uint16 num = relayaddr[msg.sender];
        for(uint i=0; i<relay[num].clientlist.length; i++){
            clientKey[relay[num].clientlist[i]].encryptedKey[num] = keys;
        }
        delete relay[num].clientlist;
    }    
    
    
    // ************
    // Client
    // ************
    
    //Client registration check.
     function client_registration_check() public view returns (uint){
        if(client[msg.sender].flag == true){
            return 1;
        } else {
            return 0;
        }
    }
    
    //Client register.
    function client_register(bytes str) public{
        require(!client[msg.sender].flag);
        client[msg.sender].flag = true;
        client[msg.sender].clientIndex = clientNum;
        client[msg.sender].RIA = new uint16[](0);
        clientKey[client[msg.sender].clientIndex].publickey = str;
        clientNum++;
    }
    
    //Create random number.
    function createRandom(address addr, uint8 j) private view returns (uint16){
        return uint16(uint(keccak256(abi.encodePacked(block.timestamp, block.difficulty, now + j, addr))) % relayIndex);
    }
    
    //Traverse an array to find duplicate values.
    function firstIndexOf(uint16[] storage array, uint16 key) private view returns (bool) {
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
        bool isIn;
        uint16 a;
        for(uint8 j=0; j<RIAnum; j++){
            a = createRandom(msg.sender, j);
            if(relay[a].flag == true){
                isIn = firstIndexOf(client[msg.sender].RIA, a);
                if(!isIn){
        	        client[msg.sender].RIA.push(a);
        	        relay[a].clientlist.push(client[msg.sender].clientIndex);
                }
            }
        }
    }
    
    //Delete random indexes for a client.
    function client_delete_random_index() public{
        require(client[msg.sender].flag == true);
        delete client[msg.sender].RIA;
    }
  
    //Client gets the length of its RIA.
    function client_get_RIA_length() view public returns (uint){
        require(client[msg.sender].flag == true);
        return client[msg.sender].RIA.length;
    }   
    
    //Clients download MSRI (Loop download).
    function client_download_MSRI(uint i) view public returns (bytes){
        require(client[msg.sender].flag == true);
        return relay[client[msg.sender].RIA[i]].encryptedSRI;
    }
 
    //Clients download symmetric keys (Loop download).
    function client_download_encrypted_keys(uint i) view public returns (bytes){
        require(client[msg.sender].flag == true);
        return clientKey[client[msg.sender].clientIndex].encryptedKey[client[msg.sender].RIA[i]];
    }   
    
    
    // ************
    // Manager
    // ************
    
    //Get the number of clients. (only called by manager)
    function getclientNum() view public returns (uint24){
        require(msg.sender == owner);
        return clientNum;
    }
    
    //Get the current index number. (only called by manager)
    function fetchIndex() view public returns (uint16){
        require(msg.sender == owner);
        return relayIndex;
    }
        
    //Set the current index number. (only called by manager)
    function setindex(uint16 x) public{
        require(msg.sender == owner);
        relayIndex = x;
    }
    
    //Download the information about one relay. (only called by manager)
    function getinfo(uint16 i) view public returns (bytes){
        require(msg.sender == owner);
        return relay[i].encryptedSRI;
    }

    //Set RIA number. (only called by manager)
    function setRIAnum(uint8 num) public{
        require(msg.sender == owner);
        RIAnum = num;
    }
    
   //Get random indexes. (only called by manager)
    function getRandom(address addr) view public returns (uint, uint16[]) {
        require(msg.sender == owner);
        return (client[addr].RIA.length, client[addr].RIA);
    }
    
    //Get authflag of a relay. (only called by manager)
    function getRelayFlag(uint16 i) view public returns (bool){
        require(msg.sender == owner);
        return relay[i].flag;
    }
        
    //Get authflag of a client. (only called by manager)
    function getClientFlag(address Addr) view public returns (bool){
        require(msg.sender == owner);
        return client[Addr].flag;
    }
    
    //Actively modify authflag of a malicious relay. (only called by manager)
    function modifyRelayFlag(uint16 i, bool flag) public{
        require(msg.sender == owner);
        relay[i].flag = flag; 
    }
    
    //Actively modify authflag of a malicious client. (only called by manager)
    function modifyClientFlag(address Addr, bool flag) public{
        require(msg.sender == owner);
        client[Addr].flag = flag;
    }
    
    //Delete the whole information about one relay. (only called by manager)
    function deleteinfo(uint16 i) public{
        require(msg.sender == owner);
        delete relay[i];
    }
}
