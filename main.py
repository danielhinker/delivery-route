# Daniel Hinker 001284172
import csv
import math

from utils import currentTime
from hashmap import packagesHash
from search import searchDistance
from truck import Truck



# speed = 18
# maximum_weight = 16
# time = '8:00'


packagesList = []
distance_list = []
packagesRemaining = []



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
            packagesHash.add(packageId, [packageId, address, city, state, zip, delivery, mass, notes, status])
      
# def lookupPackage(packageId, address, city, state, zip, delivery, mass, status):
#     for x in packagesHash:
#         if [packageId, address, city, state, zip, delivery, mass, status] in x:
#             return x

# print(lookupPackage('2', '2530 S 500 E', 'Salt Lake City', 'UT', '84106', 'EOD', '44', 'pending'))


input1 = input("Type x to check status of a package: ")
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





all_nodes = []
node_array = []
node_array_2 = []
node_array_3 = []

class Node:
    
    def __init__(self, id, location, distance):
        self.id = id
        self.location = location
        self.distance = distance

def getDistance(node):
    return node.distance


# All packages
for x in range(1, 41):
    a = packagesHash.get(str(x))
    all_nodes.append(Node(a[0], a[1], float(searchDistance('4001 South 700 East', a[1]))))


# node_array.sort(key=getDistance)






# for x in range(1, 41):
#     a = packagesHash.get(str(x))
#     node_array.append(Node(a[0], a[1], float(searchDistance('4001 South 700 East', a[1]))))


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

for x in [13, 14, 15, 16, 19, 20]:
    a = packagesHash.get(str(x))
    for y in all_nodes:
        if y.id == str(x):

            all_nodes.remove(y)
    node_array.append(Node(a[0], a[1], float(searchDistance('4001 South 700 East', a[1]))))
    
node_array.sort(key=getDistance)

for x in [6,25,28,32]:
    b = packagesHash.get(str(x))

    for y in all_nodes:
        if y.id == str(x):

            all_nodes.remove(y)
    node_array_3.append(Node(b[0], b[1], float(searchDistance('4001 South 700 East', a[1]))))

node_array_3.sort(key=getDistance)

for x in node_array_3:
    node_array.append(x)



node_array_3 = []

for y in [29,30,31,34,37,40]:
    b = packagesHash.get(str(y))
    for x in all_nodes:
        if x.id == str(y):

            all_nodes.remove(x)
    node_array_2.append(Node(b[0], b[1], float(searchDistance('4001 South 700 East', b[1]))))

node_array_2.sort(key=getDistance)

for y in [3,18,36,38]:
    b = packagesHash.get(str(y))
    for x in all_nodes:
        if x.id == str(y):

            all_nodes.remove(x)
    node_array_3.append(Node(b[0], b[1], float(searchDistance('4001 South 700 East', b[1]))))

node_array_3.sort(key=getDistance)

for y in node_array_3:
    node_array_2.append(y)


node_array_3 = []
missing_node = 0
for x in all_nodes:
    if x.id == '9':
        missing_node = x
    else:
        b = packagesHash.get(x.id)
        node_array_3.append(Node(b[0], b[1], float(searchDistance('4001 South 700 East', b[1]))))

node_array_3.sort(key=getDistance)


for i, node in enumerate(node_array_3):
    if i < 11:
        node_array.append(node)
        # node_array_3.remove(node)
    else:
        node_array_2.append(node)
    
        # node_array_3.remove(node)
    # print(i)
node_array.append(missing_node)


# print(len(node_array_2))
# print(len(node_array))
# print(len(all_nodes))

# Main function
# truck_1 = Truck(packagesHash, "truck1")
# def startTruck_1():
    
#     truck_1.getJob(node_array)
#     while len(node_array) > 0:
#         truck_1.goToLocation()
#     if len(truck_1.packagesLoaded) > 0:
#         truck_1.goToHub()

# truck_2 = Truck(packagesHash, "truck2")
# def startTruck_2():
    
#     truck_2.getJob(node_array_2)
#     while len(node_array_2) > 0:
#         truck_2.goToLocation()
        
#     if len(truck_2.packagesLoaded) > 0:
#         truck_2.goToHub()

# startTruck_1()
# startTruck_2()
# totalDistance = truck_1.distance + truck_2.distance


# finishTime = 0
# if truck_1.currentTime > truck_2.currentTime:
#     finishTime = truck_1.currentTime
# else:
#     finishTime = truck_2.currentTime
# print(totalDistance)
# print(finishTime)



# truck 1 first set
# [6,13,14,15, 16, 19, 20]

# truck 2 first set
# [29,30,31,34,37,40,25]

# truck 1 second set
# [6,25,28,32]

# truck 2 second set
#  [3,18,36,38]

# third set is the rest of the packages sorted and split



# Wrong address till 10:20am
# 9
# The wrong delivery address for package #9, Third District Juvenile Court, will be corrected at 10:20 a.m. The correct address is 410 S State St., Salt Lake City, UT 84111.


