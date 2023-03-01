//SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.4 <0.7.0;

contract newaddress {
    // contract address
    // 0x1e97137f0a9684e236A5a16bafa770D7C18C00d7
    address public myContract = address(this);
    // balance function returns balance of smart contract
    uint public myBalance = address(this).balance;

    // msg - global variable which handles everything related to blockchain properties
    address public mySender = msg.sender;
    uint public value = msg.value;
    uint public senderBalance = msg.sender.balance;

    // function updatesenderbalance() public returns(uint)
    // { 
    //     uint senderBalance1 = address(msg.sender).balance;
    //     return senderBalance1;
    // }


    // senderBalance = updatesenderbalance();

}

contract MyBasicContract {
    Person[] public people;

    uint public peopleCount = 0;
    // Struct in solidity allows you to create complex data type that can have 
    // multiple datatypes. Using struct you can define your own data type.
    struct Person{
        string _firstName;
        string _lastName;
    }

    function addPerson (string memory _firstName, string memory _lastName) public {
        // people.push() is an array type function to add data
        people.push(Person(_firstName, _lastName));

        peopleCount += 1;
    }
}

contract Calculator {
    // function is a return type , this returns an uint value
    function sum (uint _a, uint _b) public pure returns(uint) {
        uint c;
        c = _a + _b;
        return c;
    }

    function sub (uint _a, uint _b) public pure returns(uint) {
        uint c;
        c = _a - _b;
        return c;
    }

    function mul (uint _a, uint _b) public pure returns(uint) {
        uint c;
        c = _a * _b;
        return c;
    }

    function div (uint _a, uint _b) public pure returns(uint) {
        uint c;
        c = _a / _b;
        return c;
    }

    function mod (uint _a, uint _b) public pure returns(uint) {
        uint c;
        c = _a % _b;
        return c;
    }
}




