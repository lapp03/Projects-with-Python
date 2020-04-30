"""
Course: CS101
File: project04
Project: 04
Author: Alfredo Pena Polanco

Description:
  My code prompts the user for the total of different expenses and displays a
  nice budget. 
"""

"""
Instructions:

1) You will be using the input() function to prompt the user for:

   a) Item name (as a string)
   b) Item monthly amount (as a float)

   You will calculate the yearly amount for each item.  Notice that
   all of the values are floats and are displayed with cents (this is
   money).

2) You will be displaying the min, max and average monthly values 
   At the end of the budget.

3) Reminder that the TA grading your project will be able to 
   enter any text for item name (under 15 characters) and monthly value.  
   ** Your project needs to handle the different sized item names and values. ** 

4) Note: you need to match the format of the following Example Output.
   Of course, you to handle different item names and amounts.

Example Output:

Enter Item 1: Food
Enter Item 1 monthly amount: 50.55
Enter Item 2: Coding
Enter Item 2 monthly amount: 5.02
Enter Item 3: Toothpaste
Enter Item 3 monthly amount: 0.02
Enter Item 4: Rent
Enter Item 4 monthly amount: 350
Enter Item 5: Yoga lessons
Enter Item 5 monthly amount: 9.95


Monthly Budget
=================================================
Item                    Month                Year
=================================================
Food               $    50.55           $  606.60
Coding             $     5.02           $   60.24
Toothpaste         $     0.02           $    0.24
Rent               $   350.00           $ 4200.00
Yoga lessons       $     9.95           $  119.40
=================================================
Totals             $   415.54           $ 4986.48

Min value     = 0.02
Max value     = 350.00
Average value = 83.11

"""

# Add your code here
item1 = input("Enter name of item 1: ")
price1 = float(input("Enter the cost of item 1 per month: "))
year1 = float("{:.2f}".format((price1*12)))

item2 = input("Enter name of item 2: ")
price2 = float(input("Enter the cost of item 2 per month: "))
year2 = float("{:.2f}".format((price2*12)))

item3 = input("Enter name of item 3: ")
price3 = float(input("Enter the cost of item 3 per month: "))
year3 = float("{:.2f}".format((price3*12)))

item4 = input("Enter name of item 4: ")
price4 = float(input("Enter the cost of item 4 per month: "))
year4 = float("{:.2f}".format((price4*12)))

item5 = input("Enter name of item 5: ")
price5 = float(input("Enter the cost of item 5 per month: "))
year5 = float("{:.2f}".format((price5*12)))


print("Monthly Budget")
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
minValue = min(price1, price2, price3, price4, price5)
maxValue = max(price1, price2, price3, price4, price5)
meanValue =  float("{:.2f}".format(totalPrice/5))

totals_table = [["Totals", str(totalPrice), str(totalYear)]]
for item in totals_table:
    print(item[0], " "*(21-len(item[0])), "$", " ",item[1]," "*(11-len(item[1])),"$", " ", item[2])

print()
print()
print()

print("Min value{:>12}".format("= "), minValue)
print("Max value{:>12}".format("= "), maxValue)
print("Average value{:>8}".format("= "), meanValue) 

