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

class Garage():



    def __init__(self, parkingSpaces, tickets, currentTicket):
        self.parkingSpaces = parkingSpaces
        self.tickets = tickets
        self.currentTicket = currentTicket

    def takeTicket(self):
        print("Available spaces:  ")
        print(self.tickets)
        takeSpace = input('Please select a parking space:  ')
        self.tickets.remove(takeSpace)
        self.parkingSpaces.remove
        




Garage(10,[1,2,3,4,5,6,7,8,9,10])