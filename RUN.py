# As a senior member of the airport staff, i want to register a plane.
import PlaneClass
import PeopleClass
import FlightClass


while True:
    user_answer = input('Hello, what would you like to do?\nType Help for help\nType Exit for exit').strip().lower()

    if user_answer == 'exit':
        break

    elif user_answer == 'help':
        print('The Commands\nHelp for help\nExit to break')

    elif user_answer == 'register plane':
        #adds a plane

    elif user_answer == 'add passenger':
        #adds passenger

    elif user_answer == 'add passenger to flight':
        #adds passenger to flight

    elif user_answer == 'boarding list':
        #checks boarding list

    elif user_answer == 'planes':
        #gives list of planes as plane ids

    elif user_answer == 'destinations':
        #checks destinations

    else:
        print('Please choose a valid command')
