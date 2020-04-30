"""
Course: CS101
File: Project 06
Project: 06
Author: Alfredo Pena

Description:
Prompts the user for information in order to create a budget.
This project uses functions.
  
"""


"""
Instructions:

1) Create a function to display the welcome message at the start of the program.
2) Create a function that prompts the user for the current month.
3) Create a function that prompts the user for the items' name.
4) Create a function that prompts the user for the items' monthly amount.
5) Create a function to prompt the users' first name.
6) Create a function to prompt the users' surname name.
7) Call the functions above appropriately to produce output like the example below.
   NOTE: Your functions should be created above the main code that calls them and
         may need to return values to be stored in variables in your main code.

You will end up with 6 functions in this project. Name these functions
correctly (ie., use full words that describe what they do)

Example Output:

Welcome to the monthly budget program
-------------------------------------

Enter month: March
Enter first name: John
Enter surname: Brown
Enter Item name: Food
Enter Item monthly amount: 50.55
Enter Item name: Coding
Enter Item monthly amount: 5.02
Enter Item name: Toothpaste
Enter Item monthly amount: 0.02
Enter Item name: Rent
Enter Item monthly amount: 350
Enter Item name: Yoga lessons
Enter Item monthly amount: 9.95

March Monthly Budget for John Brown
=================================================
Item                     Month               Year
=================================================
Food               $    50.55           $  606.60
Coding             $     5.02           $   60.24
Toothpaste         $     0.02           $    0.24
Rent               $   350.00           $ 4200.00
Yoga lessons       $     9.95           $  119.40
=================================================
Totals             $   415.54           $ 4986.48

"""

# ====================================================================================
# Add your functions below. You should call your functions in the main code after the
# the functions are created.

def displayWelcome():
    print("Welcome to the monthly budget program")

def inputMonth():
    m = input("Enter month: ")
    return m 
    
def inputItem():
    a = input("Enter Item name: ")
    return a
   
def inputAmount():
    x = float(input("Enter Item monthly amount: "))
    return x

def inputFirstName():
    n = input("Enter first name: ")
    return n

def inputSurname():
    s = input("Enter surname: ")
    return s

#Main code

displayWelcome()
print("-------------------------------------")
print()
month = inputMonth()
name = inputFirstName()
surname = inputSurname()
item1 = inputItem()
price1 = inputAmount()
item2 = inputItem()
price2 = inputAmount()
item3 = inputItem()
price3 = inputAmount()
item4 = inputItem()
price4 = inputAmount()
item5 = inputItem()
price5 = inputAmount()
year1 = float("{:.2f}".format((price1*12)))
year2 = float("{:.2f}".format((price2*12)))
year3 = float("{:.2f}".format((price3*12)))
year4 = float("{:.2f}".format((price4*12)))
year5 = float("{:.2f}".format((price5*12)))
print()
print("{} Monthly Budget for {} {}".format(month,name,surname))
print("{:=<48}".format("="))
print("Item{:<19}".format(" "),"{:<20}Year".format("Month"))
print("{:=<48}".format("="))


budget_table = [[item1, str(price1), str(year1)],
                [item2, str(price2), str(year2)],
                [item3, str(price3), str(year3)],
                [item4, str(price4), str(year4)],
                [item5, str(price5), str(year5)]]
for item in budget_table:
    print(item[0]," "*(21-len(item[0])), "$", " ", item[1]," "*(11-len(item[1])),"$", " ", (item[2]))
    
print("{:=<48}".format("="))

totalPrice =  float("{:.2f}".format(price1 + price2 + price3 + price4 + price5))
totalYear =  float("{:.2f}".format(year1 + year2 + year3 + year4 + year5))

totals_table = [["Totals", str(totalPrice), str(totalYear)]]
for item in totals_table:
    print(item[0], " "*(21-len(item[0])), "$", " ",item[1]," "*(11-len(item[1])),"$", " ", item[2])








