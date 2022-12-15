from datetime import datetime

from deliveryservice import run_truck_one_route, run_truck_two_route, run_truck_three_route, packageHash, truck_one, \
    truck_two, truck_three


# O(1). Function takes 2 inputs and outputs package result for the package number inputted.
def user_interface_single_package(time_input, package_number_input):
    run_truck_one_route(time_input)
    run_truck_two_route(time_input)
    run_truck_three_route(time_input)
    search_result = packageHash.search(package_number_input)
    print('ID: ', search_result.ID, '  STATUS: ', search_result.status, '  TIME: ', search_result.delivery_time)


# O(N). Takes an input and prints out all packages at that time inputted.
def user_interface_all_packages(time_input):
    run_truck_one_route(time_input)
    run_truck_two_route(time_input)
    run_truck_three_route(time_input)
    print('ID            STATUS                        TIME')
    for i in range(40):
        search_result = packageHash.search(i + 1)
        print(search_result.ID, '          ', search_result.status, '          ', search_result.delivery_time)


# O(1) Starts command line interface
def user_cli():
    print("~*~*~ WELCOME TO THE WGU CHRISTMAS PACKAGE DELIVERY SERVICE ~*~*~")
    print('')
    print('It is December 15, 2021 and WGU is sending christmas gifts to the local business in the Salt Lake City Area')
    print('The delivery service must deliver all packages during normal working hours')
    print('')
    user_input = ''
    # O(1) Main Menu for CLI
    while user_input != '3':
        print("To Find Information on a Package at a specific time, enter 1")
        print("To Find Information on All packages at a Specific Time, enter 2")
        print("To Exit, enter 3")
        user_input = int(input("CHOICE: "))
        # O(1) User input 1 menu. User gives the package ID and time, and the user_interface_single_package function
        # runs with given inputs
        if user_input == 1:
            package_id = int(input("Enter Package ID: "))
            search_hour = int(input("Enter Hour in 24 Hour Format:  "))
            search_minute = int(input("Enter Minute (1-60):  "))
            print('')
            print('~*~*SEARCH RESULT~*~*')
            user_interface_single_package(datetime(2021, 12, 15, search_hour, search_minute), package_id)
            print('~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*')
            print('')
            continue
        # O(1) User input 3 menu. User gives the package ID and time, and the user_interface_all_packages function
        # runs with given inputs
        if user_input == 2:
            search_hour = int(input("Enter Hour in 24 Hour Format:  "))
            search_minute = int(input("Enter Minute (1-60):  "))
            print('')
            print('~*~*SEARCH RESULT~*~*')
            user_interface_all_packages(datetime(2021, 12, 15, search_hour, search_minute))
            print('~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*')
            print('')
            continue
        # O(1) User input 3 exits program
        if user_input == 3:
            print("Goodbye")
            print('~*~*~*~')
            print("TRUCK MILES")
            print("Truck One: ", truck_one.total_miles, "Truck Two: ", truck_two.total_miles, "Truck Three: ",
                  truck_three.total_miles)
            print("Total Miles: ", truck_one.total_miles + truck_two.total_miles + truck_three.total_miles)
            exit()


# O(1)
if __name__ == '__main__':
    user_cli()

