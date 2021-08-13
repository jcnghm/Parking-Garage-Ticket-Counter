# Your parking gargage class should have the following methods:

# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1




# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True




# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)



# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

# NOTE: Use VSCode for this project starting with the following files below. Also, each person in the group should list the portion of the project they were responsible for inside of the python file and inside the README file.



# problems:
# need to access take_space from other function
# garage capacity True False     

# Parking Garage Group Project

class Garage():

    def __init__(self, capacity, tickets, currentTicket = False):
        self.capacity = capacity
        self.tickets = tickets
        self.currentTicket = currentTicket

# Enter the parking garage method

    def takeTicket(self):
        print('These are the available parking spaces: {self.tickets}')
        if self.capacity == 0:
            print('Sorry! There are no available spaces to park in!')
        else:   
            take_space = input('What space number would you like to take? ')
            print('Thank you! Please proceed to space {take_space}')
            self.tickets.remove(take_space)
            self.capacity -= 1

# Pay for parking method

    def payTicket(self):
        print('Your total for parking is $10, Please enter your payment. ($10)')
        payment = input('Enter payment: ($10) ')
        if payment == '$10':
            self.currentTicket = True
            print('Thank you for your payment!')
        else:
            print('Incorrect payment amount!')
            

# Leave the parking garage (returns ticket to available)

    # def returnTicket(self, capacity):
    #     self.capacity = capacity

    def leaveGarage(self, changed_capacity = 1):
        if self.currentTicket == False:
            print('You need to pay before you can leave!')
        elif self.currentTicket == True:
            print('Thank you, have a nice day!')
            self.tickets.append(take_space)
            self.capacity += changed_capacity

        



car = Garage(10, [1,2,3,4,5,6,7,8,9,10])



def run():
    while True:
        response = input('What would you like to do? (Enter, Pay, or Leave')

        if response.lower == 'enter':
            car.takeTicket()
        elif response.lower == 'pay':
            car.payTicket()
        elif response.lower == 'leave':
            if car.payTicket.currentTicket == False:
                print('You must pay before leaving!')
            elif car.payTicket == True:
                car.leaveGarage()
                break
                
               
        
run()





