# Daniel Hinker 001284172
import csv
import math
import datetime

from utils import currentTime, Node
from hashmap import packagesHash
from search import searchDistance
from truck import Truck


# Reading and parsing of the CSV file containing the locations to add it into the hash table
with open('locations.csv') as csvfile:
    reader = csv.reader(csvfile)
    counter = 0
    for i, row in enumerate(reader):
        # if line_count == 0:
        # print(i)
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
            packagesHash.add(packageId, [packageId, address, city, state, zip, delivery, mass, notes, status, timeDelivered, timePickedUp])
       
all_nodes = []
node_array = []
node_array_2 = []



def getDistance(node):
    return node.distance


# All packages
for x in range(1, 41):
    a = packagesHash.get(str(x))
    # print(x)
    
    all_nodes.append(Node(a[0], a[1], float(searchDistance('4001 South 700 East', a[1]))))

# NOTES
# I manually sorted the packages that had special delivery notes
# I had three different sets of packages where each set was individually sorted based on its distance from the hub and then appended together
# I had a hash table to hold the package information
# I made a Node class to help with sorting packages
# An adjacency matrix could have also been used instead of the hash map of packages
# A weighted graph could also have been made based on the distances between each packages but this would take a lot of calculations since there are 40 packages
# If there are no delivery requirements, a more efficient algorithm would be to recalculate distances every time a package is picked up
# I tried to do that but only after the packages with the delivery requirements have been delivered


def addPackages(slice, nodeArray):
    # Efficiency of this is O(n^2) since it has nested arrays
    # newNodeArray = all_nodes[:]
    for x in slice:
        for y in all_nodes[:]:
            # print(y.id)
            if str(y.id) == str(x):
                nodeArray.append(y)
                all_nodes.remove(y)
                

    # Efficiency of this sort function is O(n log n)
    # nodeArray.sort(key=getDistance)

# Truck 1 first set

# Truck 1 second set
addPackages([13,14,15,16,19,20], node_array)



# Truck 1 second set

# addPackages([6,25,28,32], node_array_3)


addPackages([29, 30, 31, 34, 37, 40], node_array_2)


# Third set
# Efficiency of this is O(n) since I have to iterate through an array and append each element to another array


# Efficiency of this sort function is O(n log n)
all_nodes.sort(key=getDistance)

# Efficiency of this is O(n) since I have to iterate through an array and append each element to another array
for i, node in enumerate(all_nodes[:]):
    # print(node.id)
    if int(node.id) in [6,25,28,32]:
        pass
    elif i < 10:
        addPackages([int(node.id)], node_array)
    else:
        addPackages([int(node.id)], node_array_2)
# print(all_nodes)
# addPackages([], node_array)



originalAmount = len(node_array)
originalAmount2 = len(node_array_2)

def checkTime(truckObject):
    if truckObject.currentTime > datetime.timedelta(hours=9, minutes=5, seconds=00) and truckObject.counter == 0:
        addPackages([6,25,28,32], truckObject.allPackages)
        truckObject.counter += 1
        truckObject.originalAmount += 4
        truckObject.goToHub()
        # object.

# Main function
truck_1 = Truck(packagesHash, "Truck 1", node_array, originalAmount)
def startTruck_1():
    # truck_1.getJob(node_array)
    truck_1.getJob()
    while len(truck_1.packagesFinished) != truck_1.originalAmount:
        
        if len(truck_1.packagesRemaining) != 0:
            truck_1.goToLocation()
        else:
            truck_1.goToHub()

# for x in node_array_2:
#     print(x.id)

truck_2 = Truck(packagesHash, "Truck 2", node_array_2, originalAmount2)
def startTruck_2():
    
    # truck_2.getJob(node_array_2)
    truck_2.getJob()
    while len(truck_2.packagesFinished) != truck_2.originalAmount:
        checkTime(truck_2)
        if len(truck_2.packagesRemaining) != 0:
            truck_2.goToLocation()
        else:
            truck_2.goToHub()

startTruck_1()
startTruck_2()
totalDistance = truck_1.distance + truck_2.distance
print(len(all_nodes))
print(len(truck_1.packagesFinished))
print(len(truck_2.packagesFinished))

finishTime = 0
if truck_1.currentTime > truck_2.currentTime:
    finishTime = truck_1.currentTime
else:
    finishTime = truck_2.currentTime

print("-------------------------")
print("All packages have been delivered")
print("Total Distance driven: " + str(totalDistance) + " miles")
print("Time Finished: " + str(finishTime))


# Input
input1 = ''
while input1 != 'end':
    input1 = input("Enter 1,2,3 to see packages between 8:35-9:25am, 9:35-10:25am, 12:03-1:12pm\nType x to check status of a package or type end to stop program ")
    if input1 == 'x':
        packageInput = input("PackageId: ")
        addressInput = input("address: ")
        cityInput = input("city: ")
        stateInput = input("state: ")
        zipInput = input("zip: ")
        deliveryInput = input("Delivery Deadline: ")
        weightInput = input("Weight: ")
        statusInput = input("Status (Type pending or in-route): ")
        print(packagesHash.search(packageInput, addressInput, cityInput, stateInput, zipInput, deliveryInput, weightInput, statusInput)[0][1])
        # print(packagesHash.search('2', '2530 S 500 E', 'Salt Lake City', 'UT', '84106', 'EOD', '44', 'pending'))
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


# Fulfilled
# Packages only on truck 2
# 3, 18, 36, 38

# Delayed till 9:05am
# 6, 25, 28, 32

# Has to be delivered before 9:00am
# 15

# Delivered together
# 13, 14, 15, 16, 19, 20

# Has to be delivered before 10:30am
# 6, 13, 14, 16, 20, 25,   29, 30, 31, 34, 37, 40
# sort then divide in half

# Wrong address till 10:20am
# 9
# The wrong delivery address for package #9, Third District Juvenile Court, will be corrected at 10:20 a.m. The correct address is 410 S State St., Salt Lake City, UT 84111.

# truck 1 first set
# [6,13,14,15, 16, 19, 20]

# truck 2 first set
# [29,30,31,34,37,40,25]

# truck 1 second set
# [6,25,28,32]

# truck 2 second set
#  [3,18,36,38]

# third set is the rest of the packages sorted and split





