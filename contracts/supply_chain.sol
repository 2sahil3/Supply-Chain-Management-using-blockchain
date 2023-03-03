// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract Item
{
    
    string public timestamp;
    string public itemName;
    string public mfgDate;
    string public expiryDate;
    string public batchNo;
    uint public numberOfItem;


    constructor(string memory item_name,string memory time_stamp,string memory mfg_date, string memory expiry_date, string memory batch_no,uint numOfItem )
    {
        timestamp = time_stamp;
        itemName = item_name;
        mfgDate = mfg_date;
        expiryDate = expiry_date;
        batchNo = batch_no;
        numberOfItem = numOfItem;

    }

    function setTimeStamp(string memory time) public
    {
        timestamp  = time;
    }
    function setMfgDate(string memory date) public
    {
        mfgDate = date;
    }
    function setExpiryDate(string memory date) public
    {
        expiryDate  = date;
    }

    function getTimeStamp() public view returns(string memory)
    {
        return timestamp;
    }
    function getName() public view returns(string memory)
    {
        return itemName;
    }
    function getMfgDate() public view returns(string memory)
    {
        return mfgDate;
    }
    function getExpiryDate() public view returns(string memory)
    {
        return expiryDate;
    }
   

    function createHash(string memory item_name,string memory time_stamp,string memory mfg_date, string memory expiry_date, string memory batch_no ) public pure returns(bytes32)// allowed only for manufacturer and distributer
    {
        bytes32 hash1 = keccak256(abi.encode(item_name,time_stamp,mfg_date, expiry_date, batch_no ));
        return getEthSignedMessageHash(hash1);

    }

    function getEthSignedMessageHash(
        bytes32 _messageHash
    ) public pure returns (bytes32) {
        /*
        Signature is produced by signing a keccak256 hash with the following format:
        "\x19Ethereum Signed Message\n" + len(msg) + msg
        */
        return
            keccak256(
                abi.encodePacked("\x19Ethereum Signed Message:\n32", _messageHash)
            );
    }

    // function verifyForDistributor() public
    // {

    // }
    // function verifyForPharmacist() public
    // {

    // }

    // function signDigitally() public{}
    

    // bytes32 hash = createHash(itemName, timestamp, mfgDate, expiryDate, batchNo);

}




