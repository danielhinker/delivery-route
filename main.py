# Daniel Hinker 001284172
import csv
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
            # status = row[8]
            # packagesList.append()
            packagesHash.add(packageId, [packageId, address, city, state, zip, delivery, mass, notes, status])
      

node_array = []

class Node:
    
    def __init__(self, id, location, distance):
        self.id = id
        self.location = location
        self.distance = distance

def getDistance(node):
    return node.distance
# for x in len(packagesHash.keys()):
    # print(x)
    # node_array.append(Node(x, packagesHash[x][0], packagesHash[x][1]))

for x in range(1, 41):
    a = packagesHash.get(str(x))
    node_array.append(Node(a[0], a[1], float(searchDistance('4001 South 700 East', a[1]))))

node_array.sort(key=getDistance)
for x in node_array:
    print(x.distance)
# print(packagesHash.map)

for x in range(1, 41):
    packagesRemaining.append(str(x))
    # print(packagesHash.get(str(x)))




def recalculate(self):
    print(node_array)

# recalculate()




# Main function
# truck_1 = Truck(packagesHash)
# truck_1.getJob(packagesRemaining)
# while len(packagesRemaining) > 0:
#     truck_1.goToLocation()
#     truck_1.packagesRemaining
# if len(truck_1.packagesLoaded) > 0:
#     truck_1.goToHub()

# Packages only on truck 2
# 3, 18, 36, 38


