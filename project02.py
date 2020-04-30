"""
Course: CS101
File: <project02>
Project: <02>
Author: <Alfredo Pena Polanco>

Description:
  <What does your project/program do?>
"""
'It uses print() statements to complete a series of problems.'
"""
Instructions:

- Complete the following problems.
- Remember that coding style is worth 10%
  - Fill in code header
  - follow coding style outlined in the course

You must match the following output for full points:

Hello World
Hello World
Hello World is length 11
ABC
CBA
ABCBA
John
My name is John Brown and I'm 5' 8"
********** Options ***********
*                            *
*        1 - Display         *
*       2 - Play game        *
*     3 - Exit and Save      *
*                            *
******************************

"""

# Add your code below


# Problem 1: TODO -> display "Hello World" using one print() statement
print ("Hello World")

# Problem 2: TODO -> display "Hello World" using two print() statements
print ("Hello", end = " ")
print ("World") 

# Problem 3: TODO -> display "Hello World is length 11", using the len() function
print ("Hello World is length", len("Hello World"))

# Problem 4: TODO -> display "ABC", change the '?' string to get the output using {}
print("{}{}{}".format("A", "B", "C"))



# Problem 5: TODO -> Complete the following to display "CBA"
print('{2}{1}{0}'.format('C', 'B', 'A'))


# Problem 6: TODO -> Complete the following to display "ABCBA" 
print('{0}{1}{2}{1}{0}'.format('A', 'B', 'C'))


# Problem 7: TODO -> Complete the following to display "John"
print('{}{}{}{}'.format('J', 'o', 'h', 'n'))


# Problem 8: TODO -> Display your name and your height using the format() statement
# Example: My name is John Brown and I'm 5' 8"
print("My name is {} and I'm {}{}". format("Alfredo","6'",'2"')) 


# Problem 9: TODO -> Display the following.  You may use left aligned, centered
# and right aligned features of the format() function.
"""
Example output:

************ Options ************
*                               *
*          1 - Display          *
*         2 - Play game         *
*       3 - Exit and Save       *
*                               *
*********************************

"""
print('{:*^30}'.format(' Options '))
print("{:<29}*".format("*"))
print('*{: ^28}*'.format('1 - Display'))
print('*{: ^28}*'.format(' 2 - Play game '))
print('*{: ^28}*'.format(' 3 - Exit and Save '))
print ("{:<29}*".format ("*"))
print ("{:*<29}*".format ("*"))
