# Author  : Samuel Lamb
# Date    : 11/6/2020
# Purpose : Playing around with dict hashtables and their uses, for fun

# Future implementation of this file would be to read/write the table to/from a text file so that you could store
# info like a database. Also the ability to delete hashes and make a menu setup for the app. 

# Dict is an implementation of a hash table in python that can manage collisions
# You can nest dictionaries inside other dictionaries

Aitems = {
  "Apple":1.26,
  "Asparagus":1.54,
  "Avocado":2.79
}
Bitems = {
  "Banana":1.34,
  "Bagel":1.57
}
Citems = {}
Ditems = {}
Eitems = {}
Fitems = {}
Gitems = {}
Hitems = {}
Iitems = {}
Jitems = {}
Kitems = {}
Litems = {}
Mitems = {}
Nitems = {}
Oitems = {}
Pitems = {}
Qitems = {}
Ritems = {}
Sitems = {}
Titems = {}
Uitems = {}
Vitems = {}
Witems = {}
Xitems = {}
Yitems = {}
Zitems = {}

GroceryList = {
  'A':Aitems,
  'B':Bitems,
  'C':Citems,
  'D':Ditems,
  'E':Eitems,
  'F':Fitems,
  'G':Gitems,
  'H':Hitems,
  'I':Iitems,
  'J':Jitems,
  'K':Kitems,
  'L':Litems,
  'M':Mitems,
  'N':Nitems,
  'O':Oitems,
  'P':Pitems,
  'Q':Qitems,
  'R':Ritems,
  'S':Sitems,
  'T':Titems,
  'U':Uitems,
  'V':Vitems,
  'W':Witems,
  'X':Xitems,
  'Y':Yitems,
  'Z':Zitems,
}


# print(GroceryList) # Prints off the entire Hashtable
# print("Cost of a Banana: $",GroceryList['B']['Banana']) # Prints off just the cost of a Banana

while True:
  priceCheck = []
  priceCheck.append(input("Enter the item you wish to search for: "))
  # print(priceCheck[0][0]) # Prints first letter of the string entered
  if GroceryList.get(priceCheck[0][0]) == None:
    print("We currently do not support this, sorry!")
  else:
    if GroceryList[priceCheck[0][0]].get(priceCheck[0]) == None:
      if input("This item is not in our database, would you like to add it? (Y/N): ") == "Y":
        price = input('What is the price per item? : ')
        price = float(price)
        # print (price)
        GroceryList[priceCheck[0][0]][priceCheck[0]] = price
        print(GroceryList)
      else:
        print("Fair enough")
    else:
      print('Cost of',priceCheck[0],': $',GroceryList[priceCheck[0][0]][priceCheck[0]])
  
