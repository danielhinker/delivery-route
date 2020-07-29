# Daniel Hinker 001284172
import csv
import datetime

from utils import currentTime, Node
from hashmap import packagesHash
from search import searchDistance
from truck import Truck

# Reading and parsing of the CSV file containing the locations to add it into the hash table
# Efficiency is O(n) since it iterates through the rows of the csv file once
with open('locations.csv') as csvfile:
    reader = csv.reader(csvfile)
    counter = 0
    for i, row in enumerate(reader):
        if i != 0:
            packageId = row[0]
            address = row[1]
            city = row[2]
            state = row[3]
            zip = row[4]
            delivery = row[5]
            mass = row[6]
            notes = row[7]
            status = "pending"
            timeDelivered = 0
            timePickedUp = 0
            packagesHash.add(packageId, [packageId, address, city, state, zip, delivery, mass, notes, status, timePickedUp, timeDelivered])
       
# Initializing empty arrays to use for later storing packages
# O(1), initializing an empty array
all_nodes = []
node_array = []
node_array_2 = []

# This function will be used to help sort an array of objects representing the packages by how far they are.
# O(1), retrieving and displaying the distance of a node that is provided
def getDistance(node):
    return node.distance

# Add all 40 packages to an array by pulling it from the hash table
# O(n), iterating through the array
for x in range(1, 41):
    a = packagesHash.get(str(x))    
    all_nodes.append(Node(a[0], a[1], float(searchDistance('4001 South 700 East', a[1])), a[4]))

# Function to help manually add packages to the arrays.
# O(n + m) where n is the number of data in the slice array and m is the number of packages in nodeArray
def addPackages(slice, nodeArray):
    # Efficiency of this is O(n^2) since it has nested arrays
    for x in slice:
        for y in all_nodes[:]:
            if str(y.id) == str(x):
                nodeArray.append(y)
                all_nodes.remove(y)

# Adding packages specifically for truck 1
# O(n + m) where n is the number of data in the first variable and m is the number of packages in the second
addPackages([13,14,15,16,19,20,39,27], node_array)

# Adding packages specifically for truck 2
# O(n + m) where n is the number of data in the first variable and m is the number of packages in the second
addPackages([29, 30, 31, 34, 37, 40], node_array_2)

# Efficiency of this sort function is O(n log n)
# This sorts the array based on the distances of each object
all_nodes.sort(key=getDistance)

# Efficiency of this is O(n) since I have to iterate through an array and append each element to another array
# This is used to divide the rest of the packages automatically
for i, node in enumerate(all_nodes[:]):
    if int(node.id) in [6,25,28,32,36]:
        pass
    elif i < 10:
        addPackages([int(node.id)], node_array)
    else:
        addPackages([int(node.id)], node_array_2)

# These two variables store the amount of packages that each truck will deliver in total to help determine when the trucks have finished delivering
# Each one is O(1) since it just returns the length of the array which takes O(1) time
originalAmount = len(node_array)
originalAmount2 = len(node_array_2)

# This function checks the time periodically to make sure it is time to add delayed packages
# O(n + m) since it calls the addPackages function
def checkTime(truckObject):
    if truckObject.currentTime > datetime.timedelta(hours=9, minutes=5, seconds=00) and truckObject.counter == 0:
        addPackages([6,25,28,32,36], truckObject.allPackages)
        truckObject.counter += 1
        truckObject.originalAmount += 5
        truckObject.goToHub()

# Creates an instance of the Truck class, creating Truck 1, and the function that starts the truck on their delivery until it finishes all packages
# O(n + m) since it calls the addPackages function
truck_1 = Truck(packagesHash, "Truck 1", node_array, originalAmount)
def startTruck_1():
    truck_1.getJob()
    while len(truck_1.packagesFinished) != truck_1.originalAmount:
        
        if len(truck_1.packagesRemaining) != 0:
            truck_1.goToLocation()
        else:
            truck_1.goToHub()

# Creates an instance of the Truck class, creating Truck 2, and the function that starts the truck on their delivery until it finishes all packages
truck_2 = Truck(packagesHash, "Truck 2", node_array_2, originalAmount2)
def startTruck_2():
    truck_2.getJob()
    while len(truck_2.packagesFinished) != truck_2.originalAmount:
        checkTime(truck_2)
        if len(truck_2.packagesRemaining) != 0:
            truck_2.goToLocation()
        else:
            truck_2.goToHub()

# Calling the function to start the truck objects for the delivery
startTruck_1()
startTruck_2()

# Helps calculate the total distances by adding the distances that each truck has covered
# O(1) time
totalDistance = truck_1.distance + truck_2.distance

# This initializes the finishTime and returns the final time based on which truck took the longest
# O(1) time
finishTime = 0
if truck_1.currentTime > truck_2.currentTime:
    finishTime = truck_1.currentTime
else:
    finishTime = truck_2.currentTime

# Prints the total distance driven and the time finished
print("-------------------------")
print("All packages have been delivered")
print("Total Distance driven: " + str(totalDistance) + " miles")
print("Time Finished: " + str(finishTime))

# Input
# This block of code allows users to see an interface where they can input commands for the program
# such as displaying the status of packages between certain times and searching for packages
# O(n) time on average and O(n^2) at worst because it has to iterate through the packages and get from the hash table the information
for x in range (1,41):
    package = packagesHash.get(str(x))
    package[9] = "Picked up: " + str(package[9])
    package[10] = "Delivered: " + str(package[10])

input1 = ''
while input1 != 'end':
    print("----------------------------------")
    input1 = input("Enter 1,2,3 to see packages between 8:35-9:25am, 9:35-10:25am, 12:03-1:12pm\n" +
    "Type 'find' to check status of a package by id\nType 'all' to see all package with all information\n" +
    "Type 'time' to see all packages by time delivered\nType 'end' to stop program\n> ")
    # input1 = input1.strip()
    filtered = filter(str.isalnum, input1)
    filtered2 = "".join(filtered)
    input1 = filtered2
    if input1 == 'find':
        packageInput = input("PackageId: ")
        # addressInput = input("Address: ")
        # cityInput = input("City: ")
        # stateInput = input("State: ")
        # zipInput = input("Zip: ")
        # deliveryInput = input("Delivery Deadline: ")
        # weightInput = input("Weight: ")
        # statusInput = input("Status (Type pending, in-route, delivered): ")
        print(packagesHash.search(packageInput)[0][1])
    elif input1 == "all":
        packagesHash.all()
    elif input1 == "time":
        packagesHash.timeOnly()
    elif input1 == "1":
        print("Packages between 8:35am and 9:25am")
        packagesHash.timeDelivered(datetime.timedelta(hours=8, minutes=35, seconds=00), datetime.timedelta(hours=9, minutes=25, seconds=00))
        print("----------------------------------")
    elif input1 == "2":
        print("Packages between 9:35am and 10:25am")
        packagesHash.timeDelivered(datetime.timedelta(hours=9, minutes=35, seconds=00), datetime.timedelta(hours=10, minutes=25, seconds=00))
        print("----------------------------------")
    elif input1 == "3":
        print("Packages between 12:03pm and 1:12pm")
        packagesHash.timeDelivered(datetime.timedelta(hours=12, minutes=3, seconds=00), datetime.timedelta(hours=13, minutes=12, seconds=00))
        print("----------------------------------")


# Packages only on truck 2
# 3, 18, 36, 38

# Delayed till 9:05am
# 6, 25, 28, 32

# Has to be delivered before 9:00am
# 15

# Delivered together
# 13, 14, 15, 16, 19, 20

# Has to be delivered before 10:30am
# 1, 6, 13, 14, 16, 20, 25,   29, 30, 31, 34, 37, 40
# sort then divide in half

# Wrong address till 10:20am
# 9
# The wrong delivery address for package #9, Third District Juvenile Court, will be corrected at 10:20 a.m. The correct address is 410 S State St., Salt Lake City, UT 84111.
