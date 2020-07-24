# Daniel Hinker 001284172
import csv
from hashmap import packagesHash
from search import searchDistance
from truck import Truck

speed = 18
maximum_weight = 16
time = '8:00'


packagesList = []
distance_list = []
packagesRemaining = []



# Reading and parsing of the CSV file containing the locations to add it into the hash table
with open('locations.csv') as csvfile:
    reader = csv.reader(csvfile)
    counter = 0
    for i, row in enumerate(reader):
        # if line_count == 0:
        
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
        # counter += 1



# print(list[0][1])
# for x in range(1, 41):
#     packagesRemaining.append(str(x))


print(packagesRemaining)
# h.print1()
truck_1 = Truck(packagesHash)
truck_1.getJob(['1'])
truck_1.packagesRemaining
truck_1.goToLocation()
# truck_1.goToLocation()
# print(h.get('1'))


