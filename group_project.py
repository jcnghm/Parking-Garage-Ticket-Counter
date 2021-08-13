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




class Inventory():
    """
    The Inventory class will have a capacity and items that we can place inside of it
    Attributes for the class:
    -capacity: expected to be a string OR integer
    -items: expected to be a list 
    """
    def __init__(self, capacity, items):
        self.capacity = capacity
        self.items = items
    # Method that shows our inventory
    def showInventory(self):
        print("Here are your adventuring supplies: ")
#         for item in self.items:
#             print(item)
        if self.items == []:
            print("You have no loots!")
        else:
            for item in self.items:
                print(item)
    # Show the capacity of our inventory
    def showCapacity(self):
        print(f"Your carrying capacity is: {self.capacity}")
    # Add items to your items list for your inventory
    def addToInventory(self):
        supplies = input("What dank lootz have you gathered? ")
        self.items.append(supplies)
    # Change the capacity of our inventory
    def changeInventoryCapacity(self, capacity):
        self.capacity = capacity
    # Increase Capacity of our Inventory by 10 -- default
    def increaseCapacity(self, changed_capacity=10):
        if self.capacity == isinstance(self.capacity, str):
            print("You  shall not pass... that into your inventory")
        else:
            self.capacity += changed_capacity
# Create an instance of our Inventory Class
wizard_bag = Inventory(10, [])
# Create a function that will run the inventory(wizard_bag) methods
def run():
    while True:
        response = input("What would like to do? add/show/quit")
        if response.lower() == 'quit':
            wizard_bag.showInventory()
            print("ONWARD!")
            break
        elif response.lower() == "add":
            wizard_bag.addToInventory()
        elif response.lower() == "show":
            wizard_bag.showInventory()
run()
# show capacity function
# wizard_bag = Inventory(10, [])
# wizard_bag.showCapacity()
# print(f"Capacity AFTER the change...")
# wizard_bag.changeInventoryCapacity(15)
# wizard_bag.showCapacity()
# Incrementing an Attributes value through a method function
# wizard_bag.showCapacity()
# print("Capacity after increment method change: ")
# wizard_bag.increaseCapacity()
# wizard_bag.showCapacity()