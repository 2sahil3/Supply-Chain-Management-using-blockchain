// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract supplychain
{
    
    string public timestamp;
    string public itemName;
    string public mfgDate;
    string public expiryDate;
    string public batchNo;
    

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
   

    function generateQrCode() public 
    {

    }

    function verifyForDistributor() public
    {

    }
    function verifyForPharmacist() public
    {

    }

    function signDigitally() public{}

}



