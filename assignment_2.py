"""
Name: Alfredo Pena
Class: CS 241
Professor: Bro. Macbeth

This program reads from a .csv file containing rates from power companies.
It determines the average commercial rate, and also displays the information
for the highest and lowest rates found.
"""

##################################### FUNCTIONS ###########################################

"""This function prompts the user for the name of the file to be analyzed and returns it"""

def get_file():                                        
    file = input("Please enter the data file: ")   #Asks the user for the name of the file.
    return file


"""This function parse throught the file the user entered and finds the average commercial rate
and which company has the maximum and minimum commercial rate while displaying its information"""

def analysis():
    original = get_file()                          #Gets the name of the file to be analysed.
    print()
    
    commRates = []                                 #Lists of all the commercial rates(as FLOAT)contained in the file.
    businessPartners = []                          #Contains a list with business info. as STRINGS for each company contained in the file. 
    
    with open(original, "r") as file:
        next(file)                                 #Skips the first line or header. 
        for line in file:                          #For each line(business)in the file, it will add that line as a LIST to a bigger list: businessPartners.
            company = line.split(',')
            businessPartners.append(company)
    
    for company in businessPartners:               #It adds the commercial rate (as FLOAT) of each company to the commercialRates list.
        comm_rate = float(company[6])
        commRates.append(comm_rate)
    
    average = sum(commRates)/len(commRates)        #It calculates the mean of all values contained in the list call commRates.
    maxRate = str(max(commRates))                  #It finds the maximum value of the CommRates list.
    minRate = str(int(min(commRates)))             #It finds the minimum value of the CommRates list.
    
    
    
    for company in businessPartners:               #It finds the maximum/minimum rate among all companies (lists) in the businessPartners lists
        if maxRate == company[6]:                  #and, using the index, prints out the name, zipcode, state and commercial rate of the selected
            nameMax = company[2]                   #company. 
            zipMax = company[0]
            stateMax = company[3]
            commrateMax = company[6]
            print("The average commercial rate is: {}".format(average))
            print()
            print("The highest rate is:")
            print("{} ({}, {}) - $0.{}".format(nameMax, zipMax, stateMax, commrateMax))
            print()
            break
        else:
            pass
        
    for company in businessPartners:      
        if minRate == company[6]:
            nameMin = company[2]
            zipMin = company[0]
            stateMin = company[3]
            commrateMin = company[6]
            print("The lowest rate is:")
            print("{} ({}, {}) - $0.{}".format(nameMin, zipMin, stateMin, commrateMin))
            break
        else:
            pass

"""To be used as the general code; it call the analysis function"""
def main():
    analysis()
    
############################ MAIN CODE ##################################

if __name__ == '__main__':
    main()    
    
 
    



    
    







        
        






    
    







        
        



