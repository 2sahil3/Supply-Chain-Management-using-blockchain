pragma solidity >=0.4.22 <0.7.0;
pragma experimental ABIEncoderV2;

contract Parcel
{
        uint16 id;
        string name;
    
    
    constructor(uint16 _id, string memory _name) public 
    {  
        id=_id;
        name = _name;
    }

    function setParcelName(string memory _name)  public 
    {
        name = _name;
    }

    function gerParcelName() view public returns(string memory) 
    {
        return name;
    }
}


contract dusra 
{
        Parcel par = new Parcel(1,"parcel1");

        function printName(Parcel par) public 
        {
            // string memory name = par.getParcelName();

        }
    

    

    
}