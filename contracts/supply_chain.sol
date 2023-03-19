// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract Contract_supplychain
{

    struct State
    {
        string timestamp;
        string location;
    }

    struct Product
    {
        string  itemName;
        // string  timestamp;
        string mfgDate;
        string expiryDate;
        string batchNo;
        uint  numberOfItem;
        uint productId;
        State[] history;
    }

    // mapping(address => role)


    uint public runningProductId=0;
    Product[] public products;
    function createProduct(string memory item_name,string memory mfg_date, string memory expiry_date, string memory batch_no,uint numOfItem ) public
    {
        Product memory p1;
        // p1.timestamp = time_stamp;
        p1.itemName = item_name;
        p1.mfgDate = mfg_date;
        p1.expiryDate = expiry_date;
        p1.batchNo = batch_no;
        p1.numberOfItem = numOfItem;
        p1.productId = runningProductId;
        runningProductId++;
        // require(msg.sender == manufacturer);
        // addstate() call this function to add the state
    }

    function addState(uint product_id, string memory timestamp, string memory location) public 
    {
        State memory s1;
        s1.timestamp = timestamp;
        s1.location = location;
        products[product_id].history.push(s1);
    }

    function getLastIndex() public view returns(uint)
    {
        return runningProductId;
    }

    function getLastProduct() public view returns(Product memory){
        Product memory xero;
        xero.productId=1;
        if(products.length==0)return xero;
        return products[products.length-1];
    }

    function getProductDetails(uint productId) public view returns( Product memory) 
    {
        return products[productId];
    }
    function createHash(string memory item_name,string memory time_stamp,string memory mfg_date, string memory expiry_date, string memory batch_no ) public pure returns(bytes32)// allowed only for manufacturer and distributer
    {
        bytes32 hash1 = keccak256(abi.encode(item_name,time_stamp,mfg_date, expiry_date, batch_no ));
        return getEthSignedMessageHash(hash1);
    }

    function getEthSignedMessageHash(
        bytes32 _messageHash
    ) public pure returns (bytes32) {
        
        return
            keccak256(
                abi.encodePacked("\x19Ethereum Signed Message:\n32", _messageHash)
            );
    }

}
