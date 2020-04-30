"""
Course: CS101
File: Project12
Project: 12
Author: Alfredo Pena 

Description:
  It creates a wallet, like a budget more or less, which tells the user
  the money that's left after buying something. 
"""

"""
Instructions:

- You will implement a wallet as a Python list.
- This wallet will contain change.
- For this program:
     a penny will be represented as 1
     a nickel as 5
     a dime as 10, 
     a quarter as 25
     a dollar as 100
- You will be implementing the function buyItem() that will take the 
  current wallet and the purchase amount for an item.  You will
  make the correct change for the cost of the item with the
  change in the wallet.
- The program will continue to buy an item of 13 cents while there 
  is enough money in the wallet to purchase that item.
- Review how floor divide (//) and modulus (%) work with numbers.

Sample Output:

     Cents   Nickels     Dimes  Quarters   Dollars : total
         0         0         0         0         1 :   100 cents
         2         0         1         3         0 :    87 cents
         4         0         2         2         0 :    74 cents
         1         0         1         2         0 :    61 cents
         3         0         2         1         0 :    48 cents
         0         0         1         1         0 :    35 cents
         2         0         2         0         0 :    22 cents
         4         1         0         0         0 :     9 cents
remaining wallet
         4         1         0         0         0 :     9 cents

"""


def canAfford(wallet, amount):
    """ Returns True if the wallet has enough money for the amount"""
    return (sum(wallet) >= amount)



def buyItem(wallet, amount):
    
    
    newAmount = sum(wallet) - amount
    newWallet= []
    originalMoney = newAmount
    firstStep = (originalMoney/25)
    quarters = int(firstStep)
    remainder1 = (originalMoney%25)
    dimes = remainder1//10
    remainder2 = remainder1%10
    nickels = remainder2//5
    remainder3 = remainder2%5
    pennies = remainder3
    for numbers in range(pennies):
        newWallet.append(1)
    for numbers in range(nickels):
        newWallet.append(5)
    for numbers in range(dimes):
        newWallet.append(10)
    for numbers in range(quarters):
        newWallet.append(25)
    return newWallet
        
    



def displayWallet(wallet):
    """ Displays the current coins in a wallet - Don't change """
    print('{:>10}{:>10}{:>10}{:>10}{:>10} : {:>5} cents'.format(wallet.count(1), 
                      wallet.count(5), wallet.count(10), wallet.count(25), 
                      wallet.count(100), sum(wallet)))

# ===========================================================================
# Main code - Don't change this code

# set wallet with 1 dollar
wallet = [100]

# Display headers for wallet change
print('{:>10}{:>10}{:>10}{:>10}{:>10} : {:>5}'.format('Cents', 'Nickels', 'Dimes', 'Quarters', 'Dollars', 'total'))

displayWallet(wallet)

amountOfItem = 13
while (canAfford(wallet, amountOfItem)):
    wallet = buyItem(wallet, amountOfItem)
    displayWallet(wallet)

print('remaining wallet')
displayWallet(wallet)