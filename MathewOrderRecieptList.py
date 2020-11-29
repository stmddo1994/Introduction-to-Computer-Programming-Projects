# File: MathewOrderReciept.py
# Project: CSIS2101 Assignment 11
# Author: Mathew Doty
# History: Version 1.0 November 10, 2020

#This program will call the item class with 4 different items using a list

#Import Item Class from Class function
import Item

#Define maine function
def main():
    #Four items with call functions         
    item1 = Item.Item(9.99, 5, "Cloth Masks Packet")         
    item2 = Item.Item(11.49, 27, "Hand Sanitizer")         
    item3 = Item.Item(24.99, 15, "Head Shield")         
    item4 = Item.Item(8.91, 7, "Eye protection Goggles")
    #Mutate quantity to 2 for the fourth item
    item4.set_quantity(2)

    #Create a list featuring each item
    itemlist = [item1, item2, item3, item4]
    #Create lists for price and weights to be added from each item
    dTotalPrice = []
    iTotalWeight = []

    print("Here are your shopping cart contents: ")

    #Make loop to print the string function and add to the lists for each item
    #To show details of each order
    for aitem in itemlist:
        print(aitem)
        dTotalPrice.append(aitem.get_order_price())
        iTotalWeight.append(aitem.get_order_weight_in_ounces())

    #Give the sum of the price and weight lists as further details
    print("The price of your order is $" + str(f"{sum(dTotalPrice):0.2f}"))         
    print("The shipping weight is", (sum(iTotalWeight) // 16),
          "pounds", sum(iTotalWeight) % 16 , "ounces")

#Call main function
if __name__ == "__main__":
    main()
