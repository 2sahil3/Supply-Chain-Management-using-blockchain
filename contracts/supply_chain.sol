// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract Contract_supplychain
{
    struct Product
    {
        string itemName;
        string mfgDate;
        string expiryDate;
        string batchNo;
        string current_history;
        uint ID;
        uint numberOfItem;
    }
 
    uint public runningProductId=0;
    mapping(address=>Product[]) findMap;
    Product[] public products;
    function createProduct(string memory item_name,string memory mfg_date, string memory expiry_date, string memory batch_no,uint numOfItem, string memory history,int parent,address user_address ) public returns(uint)
    {
        if(parent==-1)
        {
            Product memory p1;
            p1.itemName = item_name;
            p1.mfgDate = mfg_date;
            p1.expiryDate = expiry_date;
            p1.batchNo = batch_no;
            p1.current_history=history;
            p1.numberOfItem = numOfItem;
            p1.ID = runningProductId;
            runningProductId++;
            findMap[user_address].push(p1);
            products.push(p1);
            return p1.ID;
       
        }
        else{
            for(int i=0;uint(i)<findMap[user_address].length;i++){
                if(findMap[user_address][uint(i)].ID==uint(parent))
                {   parent=i;
                    break;
                }
            }
            require(findMap[user_address][uint(parent)].numberOfItem>=numOfItem);
            Product memory p1;  
            p1.itemName = item_name;
            p1.mfgDate = mfg_date;
            p1.expiryDate = expiry_date;
            p1.batchNo = batch_no;
            p1.current_history=history;
            p1.numberOfItem = numOfItem;
            p1.ID = runningProductId;
            runningProductId++;
            products.push(p1);
            findMap[user_address].push(p1);
            findMap[user_address][uint(parent)].numberOfItem-=numOfItem;
            return p1.ID;
        }

        
    }

    function findProduct(address person) public view returns (Product[] memory){
        if(findMap[person].length!=0)
        {
            return findMap[person];
        }
        Product[] memory arr;
        return arr;
    }


    function getLastIndex() public view returns(uint)
    {
        return runningProductId;
    }
    function getProductDetails(uint productId) public view returns( Product memory) 
    {
        return products[productId];
    }

    function getLastProductId(address addr) public view returns(uint)
    {
        Product[] memory p =  findMap[addr];
        uint id = findMap[addr][p.length-1].ID;
        return id;
    }

}