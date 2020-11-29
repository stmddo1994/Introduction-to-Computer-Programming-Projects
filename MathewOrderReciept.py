# File: MathewOrderReciept.py
# Project: CSIS2101 Assignment 11
# Author: Mathew Doty
# History: Version 1.0 November 10, 2020

import Item

def main():
    dTotalPrice = 0.0         
    iTotalWeight = 0
    # Put the 4 items being ordered in item1 through item 4         
    item1 = Item.Item(9.99, 5, "Cloth Masks Packet")         
    item2 = Item.Item(11.49, 27, "Hand Sanitizer")         
    item3 = Item.Item(24.99, 15, "Head Shield")         
    item4 = Item.Item(8.91, 7, "Eye protection Goggles")         
    item4.set_quantity(2)   
		
    # Show the details of the order using:         
    print("Here are your shopping cart contents.")         
    print(item1)         
    print(item2)        
    print(item3)         
    print(item4) 
		
    # Compute the total price and total weight in this section        
    dTotalPrice += item1.get_order_price()         
    dTotalPrice += item2. get_order_price()         
    dTotalPrice += item3. get_order_price()         
    dTotalPrice += item4. get_order_price()         
    iTotalWeight += item1.get_order_weight_in_ounces()        
    iTotalWeight += item2. get_order_weight_in_ounces ()         
    iTotalWeight += item3. get_order_weight_in_ounces ()         
    iTotalWeight += item4. get_order_weight_in_ounces ()         
    # Here we show the order details        
    print("The price of your order is $"+ str(dTotalPrice))         
    print("The shipping weight is", (iTotalWeight // 16),
          "pounds", iTotalWeight % 16 , "ounces")     
    #End of main
   
if __name__ == "__main__":
    main()	
