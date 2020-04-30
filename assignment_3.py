"""
Name: Alfredo Pena
Class: CS 241
Prof.: Bro. Macbeth

This program models driving a robot around in an environment.
"""

##############################################################

class CrappyRobot():
    def __init__(self):                 ###Initializes the crappy robot. 
        self.xCoordinate = 10
        self.yCoordinate = 10
        self.fuel_amount = 100
    
    def useFuel(self):                  ###Lowers the robot's amount of fuel left. 
        self.fuel_amount -= 5
    
    def moveLeft(self):                 ###Moves the robot a unit to the left. 
        if self.fuel_amount < 5:
            print("Insufficient fuel to perform action")
        else:
            self.xCoordinate -= 1
            self.useFuel()
            
    def moveRight(self):                ####Moves the robot a unit to the right. 
        if self.fuel_amount < 5:
            print("Insufficient fuel to perform action")
        else:
            self.xCoordinate += 1
            self.useFuel()
    
    def moveUp(self):                   ###Moves the robot a unit up. 
        if self.fuel_amount < 5:
            print("Insufficient fuel to perform action")
        else:
            self.yCoordinate -= 1
            self.useFuel()
        
    def moveDown(self):                 ###Moves the robot a unit down. 
        if self.fuel_amount < 5:
            print("Insufficient fuel to perform action")
        else:
            self.yCoordinate += 1
            self.useFuel()
    
    def shoot(self):                    ###Shoots two bullets with the robot's shotgun.  
        if self.fuel_amount < 15:
            print("Insufficient fuel to perform action")
        else:
            for times in range(3):
                self.useFuel()
            print("Bam! Bam!")   
   
    def displayStatus(self):            ###Displays the robot's status. 
            print("({}, {}) - Fuel: {}".format(self.xCoordinate, self.yCoordinate, self.fuel_amount))
    


################################################################

def askforCommand():                    ###Prompts the user for a command. 
    command = input("Enter command: ")
    return command

def main():                             ###While there's fuel, allows the user to control the robot. 
    robot = CrappyRobot()
    command = None
    
    while command != 'quit':
        command = askforCommand()
        
        if command == 'left':
            robot.moveLeft()
             
        elif command == 'right':
            robot.moveRight()
            
        elif command == 'up':
            robot.moveUp()
           
        elif command == 'down':
            robot.moveDown()
            
        elif command == 'fire':
            robot.shoot()
                     
        elif command == 'status':
            robot.displayStatus()
        
        else:
            pass
    
    print('Goodbye.')
        
##############################################################        

if __name__ == "__main__":
    main()        
    
    
    
        
    
    
    
    
    