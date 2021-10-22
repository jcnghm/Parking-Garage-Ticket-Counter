   
# Parking Garage Ticket Counter

class Garage():

    def __init__(self, capacity, tickets, currentTicket = False):
        self.capacity = capacity
        self.tickets = tickets
        self.currentTicket = currentTicket

# Enter the parking garage method

    def takeTicket(self):
        print(f'These are the available parking spaces: {self.tickets}')
        if self.capacity == 0:
            print('Sorry! There are no available spaces to park in!')
        else:   
            take_space = int(input('What space number would you like to take? '))
            print(f'Thank you! Please proceed to space {take_space}')
            self.tickets.remove(take_space)
            self.capacity -= 1

# Pay for parking method

    def payTicket(self):
        space_used = int(input('Which parking spot did you occupy? '))
        print('Your total for parking is $10, Please enter your payment. ($10)')
        payment = input('Enter payment: ($10) ')
        if payment == '$10':
            self.currentTicket = True
            self.tickets.append(space_used)
            self.tickets.sort()
            print('Thank you for your payment!')
        else:
            print('Incorrect payment amount!')
            
# Leave the parking garage (returns ticket to available)

    def leaveGarage(self, changed_capacity = 1):
        if self.currentTicket == True:
            print('Thank you, have a nice day!')
            self.capacity += changed_capacity
        elif self.currentTicket == False:
            print('You must pay before leaving!')


car = Garage(10, [1,2,3,4,5,6,7,8,9,10],)


def run():
    while True:
        response = input('What would you like to do? (Enter, Pay, or Leave)')
        if response.lower() == 'enter':
            car.takeTicket()
        elif response.lower() == 'pay':
            car.payTicket()
        elif response.lower() == 'leave':
            car.leaveGarage()
            
                    
run()





