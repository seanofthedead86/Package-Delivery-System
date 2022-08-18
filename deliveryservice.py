import csv

from hashTable import ChainingHashTable
from packages import Package
from truck import DeliveryTruck
from datetime import datetime, timedelta
from clock import clock

truck_one = DeliveryTruck([1, 21, 4, 26], [13, 14, 15, 20, 16, 19, 37, 40, 34, 29, 30], 'At Hub',
                          datetime(2021, 12, 15, 8, 00), 0)
truck_two = DeliveryTruck([3, 18, 36, 38, 28, 2], [6, 25, 31, 32], 'At Hub', datetime(2021, 12, 15, 8, 00), 0)
truck_three = DeliveryTruck([9], [5, 7, 8, 10, 11, 12, 17, 22, 23, 24, 27, 33, 35, 39], 'At Hub',
                            datetime(2021, 12, 15, 8, 00), 0)

running_clock = clock(datetime(2021, 12, 15, 8, 00))

# O(n). Takes csv and parses it to create a package object that gets added into a hash table.
def load_package_data(filename):
    with open(filename) as PackageCSV:
        package_data = csv.reader(PackageCSV, delimiter=',')
        next(package_data)  # skip header
        for package in package_data:
            p_id = int(package[0])
            p_address = package[1]
            p_city = package[2]
            p_state = package[3]
            p_zip_code = package[4]
            p_deadline = package[5]
            p_mass = package[6]
            p_notes = package[7]
            p_status = package[8]
            p_delivery_time = package[9]

            p = Package(p_id, p_address, p_city, p_state, p_zip_code, p_deadline, p_mass, p_notes, p_status,
                        p_delivery_time)
            packageHash.insert(p_id, p)


# O(1) CSV reader reads Address.CSV into a list
with open('Addresses.csv') as csvfile_2:
    addressData = list(csv.reader(csvfile_2, delimiter=','))


# O(1)
def distance_csv(filename):
    with open(filename, newline='') as f_input:
        return [list(map(float, row)) for row in csv.reader(f_input)]


# Chaining Hast Table object is created.
packageHash = ChainingHashTable()

# O(1) Packages.csv in read into load_package_data
load_package_data('Packages.csv')

# O(1)
distance_data = distance_csv('Distances.csv')


# O(1): package_address takes a package number input and outputs a single entry list with the name of the address from
# the package hash table
def package_address(package_number):
    address_list = []
    address = packageHash.search(package_number)
    address_list.append(address.__getattribute__('address'))
    return address_list


# O(1): Takes two address inputs and outputs the distance between the two address via the distance_data list, using
# address 1 as the chosen row, and address 2 as the chosen column
def distance_between(address1, address2):
    return distance_data[address1][address2]


# O(n) Takes the list of packages that a truck is scheduled to deliver and looks up the corresponding address index to
# create a list of destinations, r. If a package has the same address index that a previous package already looked up,
# it continues on without adding that index to list r to prevent duplicate drop off spots.
def route_index(truck_packages):
    route_list = []
    for location in truck_packages:
        r1 = int(addressData.index(package_address(location)))
        if r1 in route_list:
            continue
        route_list.append(r1)
    return route_list


# Truck One Start
# O(n^2) Truck One route.
def run_truck_one_route(input_time):
    start_time = datetime(2021, 12, 15, 8, 00)
    current_time = datetime(2021, 12, 15, 8, 00)
    queue = route_index(truck_one.packages)
    priority_queue = route_index(truck_one.priority_packages)
    truck_one_packages = truck_one.packages
    truck_one_packages_high = truck_one.priority_packages
    truck_one.location = "On Route"
    total_distance = []
    current_location = 0
    lowest_location = 500
    # For each package in both queues, change status to "On Truck, Waiting For Delivery"
    for i in truck_one_packages + truck_one_packages_high:
        package_status_object = packageHash.search(i)
        package_status_object.status = "On Truck, Waiting For Delivery"
    # while priority queue length is greater than 1, check users input time. If input time is greater than the current \
    # time, stop the algorithm Otherwise, continue.
    while len(priority_queue) > 0:
        default_distance = 500
        if input_time < current_time:
            return
            # for each location in the priority queue, get the distance between it and the current location. If that
        # distance is the shortest distance between the 2 locations, that location becomes lowest_location.
        for loc in priority_queue:
            graph_distance = distance_data[current_location][loc]
            if graph_distance < default_distance:
                default_distance = graph_distance
                lowest_location = loc
        current_distance = default_distance
        total_distance.append(current_distance)
        current_location = lowest_location
        # for each item in the high priority list, get the current locations address and compare it to the package
        # address. If they are the same, change the package status delievered and time to current time, and truck's
        # total distance is changed to the sum of all distances traveled.
        for x in truck_one_packages_high:
            address_string = ' '.join(addressData[current_location])
            package_object = packageHash.search(x)
            package_object_address = package_object.__getattribute__('address')
            if address_string == package_object_address:
                package_object.status = 'Delivered'
                time_traveled = (current_distance / 18) * 60
                travel_delta = timedelta(minutes=time_traveled)
                time_delivered = current_time + travel_delta
                current_time = time_delivered
                running_clock.current_time = current_time
                package_object.delivery_time = time_delivered
                sum_total_distance = sum(total_distance)
                truck_one.total_miles = sum_total_distance
        # Remove package from queue
        priority_queue.remove(lowest_location)
    # --------
    while len(queue) > 0:
        default_distance = 500
        if input_time < current_time:
            return
        for loc in queue:
            graph_distance = distance_data[current_location][loc]
            if graph_distance < default_distance:
                default_distance = graph_distance
                lowest_location = loc
        current_distance = default_distance
        total_distance.append(current_distance)
        current_location = lowest_location
        for x in truck_one_packages:
            address_string = ' '.join(addressData[current_location])
            package_object = packageHash.search(x)
            package_object_address = package_object.__getattribute__('address')
            if address_string == package_object_address:
                package_object.status = 'Delivered'
                time_traveled = (current_distance / 18) * 60
                travel_delta = timedelta(minutes=time_traveled)
                time_delivered = current_time + travel_delta
                current_time = time_delivered
                running_clock.current_time = current_time
                package_object.delivery_time = time_delivered
                sum_total_distance = sum(total_distance)
                truck_one.total_miles = sum_total_distance
        queue.remove(lowest_location)
        # Find the distance between the current location and the first default location
        if len(queue) == 0:
            to_hub = distance_data[current_location][0]
            total_distance.append(to_hub)
            truck_one.location = 'Finished'


# Truck Two route. Same as Truck One.
def run_truck_two_route(input_time):
    start_time = datetime(2021, 12, 15, 9, 6)
    current_time = datetime(2021, 12, 15, 9, 6)
    queue = route_index(truck_two.packages)
    priority_queue = route_index(truck_two.priority_packages)
    truck_two_packages = truck_two.packages
    truck_two_packages_high = truck_two.priority_packages
    truck_two.location = "On Route"
    total_distance = []
    current_location = 0
    lowest_location = 500
    for i in truck_two_packages + truck_two_packages_high:
        package_status_object = packageHash.search(i)
        package_status_object.status = "On Truck, Waiting For Delivery"
    while len(priority_queue) > 0:
        if input_time < current_time:
            return
        default_distance = 500
        for loc in priority_queue:
            graph_distance = distance_data[current_location][loc]
            if graph_distance < default_distance:
                default_distance = graph_distance
                lowest_location = loc
        current_distance = default_distance
        total_distance.append(current_distance)
        current_location = lowest_location
        for x in truck_two_packages_high:
            address_string = ' '.join(addressData[current_location])
            package_object = packageHash.search(x)
            package_object_address = package_object.__getattribute__('address')
            if address_string == package_object_address:
                package_object.status = 'Delivered'
                time_traveled = (current_distance / 18) * 60
                travel_delta = timedelta(minutes=time_traveled)
                time_delivered = current_time + travel_delta
                current_time = time_delivered
                running_clock.current_time = current_time
                package_object.delivery_time = time_delivered
                sum_total_distance = sum(total_distance)
                truck_two.total_miles = sum_total_distance
        priority_queue.remove(lowest_location)
    # --------
    while len(queue) > 0:
        if input_time < current_time:
            return
        default_distance = 500
        for loc in queue:
            graph_distance = distance_data[current_location][loc]
            if graph_distance < default_distance:
                default_distance = graph_distance
                lowest_location = loc
        current_distance = default_distance
        total_distance.append(current_distance)
        current_location = lowest_location
        # -NEW START-
        for x in truck_two_packages:
            address_string = ' '.join(addressData[current_location])
            package_object = packageHash.search(x)
            package_object_address = package_object.__getattribute__('address')
            if address_string == package_object_address:
                package_object.status = 'Delivered'
                time_traveled = (current_distance / 18) * 60
                travel_delta = timedelta(minutes=time_traveled)
                time_delivered = current_time + travel_delta
                current_time = time_delivered
                running_clock.current_time = current_time
                package_object.delivery_time = time_delivered
                sum_total_distance = sum(total_distance)
                truck_two.total_miles = sum_total_distance
        queue.remove(lowest_location)
        if len(queue) == 0:
            to_hub = distance_data[current_location][0]
            total_distance.append(to_hub)
            truck_two.location = 'Finished'


# Truck Three route. Same as Truck One.
def run_truck_three_route(input_time):
    start_time = datetime(2021, 12, 15, 10, 13)
    current_time = datetime(2021, 12, 15, 10, 13)
    queue = route_index(truck_three.packages)
    priority_queue = route_index(truck_three.priority_packages)
    truck_three_packages = truck_three.packages
    truck_three_packages_high = truck_three.priority_packages
    truck_three.location = "On Route"
    total_distance = []
    current_location = 0
    lowest_location = 500
    for i in truck_three_packages + truck_three_packages_high:
        package_status_object = packageHash.search(i)
        package_status_object.status = "On Truck, Waiting For Delivery"
    # --------
    while len(priority_queue) > 0:
        if input_time < current_time:
            return
        default_distance = 500
        for loc in priority_queue:
            graph_distance = distance_data[current_location][loc]
            if graph_distance < default_distance:
                default_distance = graph_distance
                lowest_location = loc
        current_distance = default_distance
        total_distance.append(current_distance)
        current_location = lowest_location
        for x in truck_three_packages_high:
            address_string = ' '.join(addressData[current_location])
            package_object = packageHash.search(x)
            package_object_address = package_object.__getattribute__('address')
            if address_string == package_object_address:
                package_object.status = 'Delivered'
                # package_object.delivery_time = 'TIME'
                time_traveled = (current_distance / 18) * 60
                travel_delta = timedelta(minutes=time_traveled)
                time_delivered = current_time + travel_delta
                current_time = time_delivered
                package_object.delivery_time = time_delivered
                running_clock.current_time = current_time
                sum_total_distance = sum(total_distance)
                truck_three.total_miles = sum_total_distance
        priority_queue.remove(lowest_location)
    # --------
    while len(queue) > 0:
        if input_time < current_time:
            return
        default_distance = 500
        for loc in queue:
            graph_distance = distance_data[current_location][loc]
            if graph_distance < default_distance:
                default_distance = graph_distance
                lowest_location = loc
        current_distance = default_distance
        total_distance.append(current_distance)
        current_location = lowest_location
        for x in truck_three_packages:
            address_string = ' '.join(addressData[current_location])
            package_object = packageHash.search(x)
            package_object_address = package_object.__getattribute__('address')
            if address_string == package_object_address:
                package_object.status = 'Delivered'
                time_traveled = (current_distance / 18) * 60
                travel_delta = timedelta(minutes=time_traveled)
                time_delivered = current_time + travel_delta
                current_time = time_delivered
                running_clock.current_time = current_time
                package_object.delivery_time = time_delivered
                sum_total_distance = sum(total_distance)
                truck_three.total_miles = sum_total_distance
        queue.remove(lowest_location)
        if len(queue) == 0:
            to_hub = distance_data[current_location][0]
            total_distance.append(to_hub)
            truck_three.location = 'Finished'
