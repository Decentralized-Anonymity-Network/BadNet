// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.7.0;
pragma experimental ABIEncoderV2;

contract DirectoryContractV3{
    
    address owner;
    uint RelayUploadPeriod = 60; // 1 hour
    uint16 relayIndex = 1;
    uint16[] public unhealthyRelaySet;
    uint8 CurrentCounter = 1;
    mapping (uint8 => bool) CounterOP;
    mapping (uint8 => uint16[]) CounterList;
    
    struct Relay{
        bool registered;
        bool healthflag;
        uint8 counter;
        bytes Hdr;
        bytes encryptedSRI;
        bytes NSD;
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
    
    // Relay registration check.
    function relay_registration_check() public view returns(uint16) {
        if(relay[relayaddr[msg.sender]].registered == true) {
            return relayaddr[msg.sender];
        } else {
            return 0;
        }
    }
    
    // Relay registration.
    function relay_register() public {
        require(relay[relayaddr[msg.sender]].registered == false);
        relayaddr[msg.sender] = relayIndex;
        relay[relayIndex].registered = true;
        relay[relayIndex].healthflag = true;
        CounterOP[CurrentCounter] = true;
        CounterList[CurrentCounter] = [relayIndex];
        relayIndex++;
        CurrentCounter++;
    }
    
    // Relay gets SRI upload period (in minutes). 
    function relay_get_upload_period() view public returns(uint) {
        require(relay[relayaddr[msg.sender]].registered == true);
        return RelayUploadPeriod;
    }

    // Relay gets the subset S of relays used for broadcast encryption.
    function relay_get_index_set() view public returns(uint16, uint16[] memory) {
        require(relay[relayaddr[msg.sender]].registered == true);
        return (relayIndex, unhealthyRelaySet);
    }

    // Relay gets the current counter. 
    function relay_get_current_counter() view public returns(uint8) {
        require(relay[relayaddr[msg.sender]].registered == true);
        return CurrentCounter;
    }

    // Relay incentive mechanism.
    function contract_transfer_to_relay(address payable addr) public payable {
        addr.transfer(0.0005 * 10**18);    //Transaction Fee (Gwei)
    }
    
    // Relay uploads counter, Hdr, encrypted SRI, and the plaintext NSD.
    function relay_upload_SRI_and_NSD(uint8 _counter, bytes memory _Hdr, bytes memory _encryptedSRI, bytes memory _NSD) public {
        require(relay[relayaddr[msg.sender]].healthflag == true);
        uint16 index = relayaddr[msg.sender];
        relay[index].counter = _counter;
        relay[index].Hdr = _Hdr;
        relay[index].encryptedSRI = _encryptedSRI;
        relay[index].NSD = _NSD;
        // contract_transfer_to_relay(msg.sender);
    }

    // Relay downloads SRI (Loop download).
    function relay_download_SRI(uint16 i) view public returns(uint8, bytes memory, bytes memory) {
        require(relay[relayaddr[msg.sender]].registered == true);
        require(i < relayIndex && relay[i].healthflag == true);
        return(relay[i].counter, relay[i].Hdr, relay[i].encryptedSRI);
    }

    // Relay gets the historical list of counter.
    function relay_get_counter_list(uint8 counter) view public returns(bool[] memory, uint16[][] memory) {
        require(relay[relayaddr[msg.sender]].registered == true);
        require(counter < CurrentCounter);
        bool[] memory operation = new bool[](CurrentCounter-counter);
        uint16[][] memory alterSet = new uint16[][](CurrentCounter-counter);
        for(uint8 i=counter; i<CurrentCounter; i++) {
            operation[CurrentCounter-i-1] = CounterOP[i];
            alterSet[CurrentCounter-i-1] = CounterList[i];
        }
        return (operation, alterSet);
    }
 
    // Relay cancellation.
    function relay_cancellation() public {
        require(relay[relayaddr[msg.sender]].registered == true);
        delete relay[relayaddr[msg.sender]];
        delete relayaddr[msg.sender];
    }    
    
    
    // ************************
    // Client Method
    // ************************
    
    // Client downloads NSD.
    function client_download_NSD() view public returns(bool[] memory, bytes memory) {
        bool[] memory NSDIndex = new bool[](relayIndex-1);
        bytes memory NSDbytes;
        for(uint16 i=1; i<relayIndex; i++) {
            if(relay[i].healthflag == true) {
                NSDIndex[i-1] = true;
                NSDbytes = abi.encodePacked(NSDbytes, relay[i].NSD);
            }
            else {
                NSDIndex[i] = false;
            }
        }
        return (NSDIndex, NSDbytes);
    }        
    

    // ************************
    // Manager Method
    // ************************
    
    // Set relay SRI upload period (in minutes).
    function setSRIperiod(uint period) public {
        require(msg.sender == owner);
        RelayUploadPeriod = period;
    }

    // Get the current index number.
    function getrelayIndex() view public returns(uint16) {
        require(msg.sender == owner);
        return relayIndex;
    }

    // Get the information about one relay.
    function getinfo(uint16 i) view public returns(uint8, bytes memory, bytes memory, bytes memory) {
        require(msg.sender == owner);
        return (relay[i].counter, relay[i].Hdr, relay[i].encryptedSRI, relay[i].NSD);
    } 
    
    // Get healthflag of a relay.
    function getHealthFlag(uint16 i) view public returns(bool) {
        require(msg.sender == owner);
        return relay[i].healthflag;
    }

    // Actively modify healthflag of an unhealthy relay to *FALSE*.
    function modifyHealthFlag(uint16 size, uint16[] memory list) public {
        require(msg.sender == owner);
        for(uint16 i=0; i<size; i++) {
            require(relay[list[i]].healthflag == true);
            relay[list[i]].healthflag = false;
            unhealthyRelaySet.push(list[i]);
        }
        CounterOP[CurrentCounter] = false;
        CounterList[CurrentCounter] = list;
        CurrentCounter++;
    }
}
