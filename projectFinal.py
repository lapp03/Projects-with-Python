"""
Course: CS101
File: projectFinal
Project: 14
Author: Alfredo Pena 

Description:
  It creates a shopping list according to what the user instructs.
"""

"""
Instructions:

Write a program that allows a user to create and use a shopping list.  Your
program will display a menu of options to the user.  The user is free
to select any option from the menu in any order.


Sample Output:

Welcome to the shopping list program.

Menu
   n - New shopping list item
   d - Display shopping list
   e - Edit an item in the list
   c - Check or remove item from list
   ? - Display this menu
   q - Quit program
> n
Enter shopping item: Bread
> n
Enter shopping item: Milk
> n
Enter shopping item: Eggs
> d
********* Shopping list *********
* 1  Bread                      *
* 2  Milk                       *
* 3  Eggs                       *
*********************************
> e
Which item do you want to change?: 2
Enter your change: Whole Milk
> d
********* Shopping list *********
* 1  Bread                      *
* 2  Whole Milk                 *
* 3  Eggs                       *
*********************************
> e
Which item do you want to change?: 10
Error: There is no item at that position
> e
Which item do you want to change?: 0
Error: There is no item at that position
> ?
Menu
   n - New shopping list item
   d - Display shopping list
   e - Edit an item in the list
   c - Check or remove item from list
   ? - Display this menu
   q - Quit program
> c
Which item do you want to check?: 10
Error: There is no item at that position
> c
Which item do you want to check?: 1
Item 1 was checked and removed
> d
********* Shopping list *********
* 1  Whole Milk                 *
* 2  Eggs                       *
*********************************
> n
Enter shopping item: Ice Cream
> d
********* Shopping list *********
* 1  Whole Milk                 *
* 2  Eggs                       *
* 3  Ice Cream                  *
*********************************
> q
Good bye

"""

# TODO - add your project code here

############################# FUNCTIONS ###############################

def displayMenu():
    print("Menu")
    print("   n - New shopping list item")
    print("   d - Display shopping list")
    print("   e - Edit an item in the list")
    print("   c - Check or remove item from list")
    print("   ? - Display this menu")
    print("   q - Quit program")

def welcomeMsg():
    print("Welcome to the shopping list program.")
    print()

def instruction():
    letter = input("> ")
    return letter

def newItem():
    item = input("Enter shopping item: ")
    return item

def correctItem():
    correction = shoppingList[int(input("Which item do you want to change?: "))]
    if correction in shoppingList:
        x = shoppingList.index(correction)
        correctedItem = input("Enter your change: ")
        shoppingList[x] = correctedItem

def checkItem():
    x = input("Which item do you want to check?: ")
    itemChecked = shoppingList[int(x)]
    if itemChecked in shoppingList:
        shoppingList.remove(itemChecked)
        print("Item",x,"was checked and removed")
        
def displayList():
    print('{:*^30}'.format(' Shopping List '))
    for item in shoppingList:
        print('* {: <27}*'.format(str(shoppingList.index(item))+ "  " + item))
    print ("{:*<30}".format ("*"))
    
    
def errorMsg():
    print("Error: There is no item at that position")
    
################################# MAIN CODE ###################################

welcomeMsg()

displayMenu()

shoppingList = []

selectedOption = 1
while selectedOption != "q":
    selectedOption = instruction()
    
    if selectedOption == "n":
        item = newItem()
        shoppingList.append(item)
    
    if selectedOption == "d":
        displayList()
    
    if selectedOption == "e":
        try:
            correctItem()
        except IndexError:
            errorMsg()
            
    if selectedOption == "c":
        try:
            checkItem()
        except IndexError:
            errorMsg()
    
    if selectedOption == "?":
        displayMenu()

if selectedOption == "q":
    print("Good bye")      
            
        
"""
Happy Spring break! :-D

"""
        
        
        
        
       
    

    



   