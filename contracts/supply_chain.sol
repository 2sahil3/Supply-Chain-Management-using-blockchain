// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract Contract_supplychain
{
    struct Product
    {
        string  timestamp;
        string  itemName;
        string mfgDate;
        string expiryDate;
        string batchNo;
        uint  numberOfItem;
        uint productId;
    }
    uint public runningProductId = 0;
    // mapping(uint=>Product) map ;
    Product[] public products;



    function createProduct(string memory item_name,string memory time_stamp,string memory mfg_date, string memory expiry_date, string memory batch_no,uint numOfItem ) public returns(uint)
    {
        Product memory p1;
        p1.timestamp = time_stamp;
        p1.itemName = item_name;
        p1.mfgDate = mfg_date;
        p1.expiryDate = expiry_date;
        p1.batchNo = batch_no;
        p1.numberOfItem = numOfItem;
        p1.productId = products.length;
        products.push(p1);
        return p1.productId;
        // map[runningProductId+1] = p1;
    }

    function getProductDetails(uint productId) public view returns( Product memory) 
    {
        return products[productId];
        // return map[productId];
    }

    // function setTimeStamp(string memory time) public
    // {
    //     timestamp  = time;
    // }
    // function setMfgDate(string memory date) public
    // {
    //     mfgDate = date;
    // }
    // function setExpiryDate(string memory date) public
    // {
    //     expiryDate  = date;
    // }

    // function getTimeStamp() public view returns(string memory)
    // {
    //     return timestamp;
    // }
    // function getName() public view returns(string memory)
    // {
    //     return itemName;
    // }
    // function getMfgDate() public view returns(string memory)
    // {
    //     return mfgDate;
    // }
    // function getExpiryDate() public view returns(string memory)
    // {
    //     return expiryDate;
    // }
   

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




