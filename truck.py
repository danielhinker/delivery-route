from search import searchDistance
from hashmap import packagesHash
from utils import currentTime
import datetime

class Truck:

# Initializes the attributes of each truck
# O(1) time
    def __init__(self, hashmap, name, nodeArray, originalAmount):
        self.currentLocation = "4001 South 700 East"
        self.packagesRemaining = []
        self.packagesFinished = []
        self.allPackages = nodeArray
        self.packagesHash = hashmap
        self.distance = 0.0
        self.speed = 18.0
        self.currentTime = currentTime
        self.hubLocation = "4001 South 700 East"
        self.name = name
        self.counter = 0
        self.originalAmount = originalAmount
        
# Adds more packages from the hub
# O(n) time since it has to iterate through all packages in the allPackages array
    def getJob(self):
        for i, x in enumerate(self.allPackages[:]):
            if len(self.packagesRemaining) != 16:
                self.packagesRemaining.append(x)
                self.allPackages.remove(x)

# This function changes the state of the truck's location and adds to the time and distance
# O(n^2) since it has to call the searchDistance function
    def drive(self, startLocation, endLocation):
        print(self.name)
        print("Current Time: " + str(self.currentTime))
        print("Current Location: " + startLocation)
        if endLocation == self.hubLocation:
            print("Going back to hub at 4001 South 700 East") 
        else:
            print("Going to: " + endLocation)
        distanceToLocation = searchDistance(startLocation, endLocation)
        self.distance += float(distanceToLocation)
        timeTaken = float(distanceToLocation) / self.speed
        self.currentTime += datetime.timedelta(hours=timeTaken)
        # print("Time After Drive: " + str(self.currentTime))
        self.currentLocation = endLocation

# Sets the location to drive to as the hub location
# O(n^3) since it has to call the recalculate function which is the most time consuming task
    def goToHub(self):   
        self.drive(self.currentLocation, self.hubLocation)
        self.getJob()
        self.recalculate()

# Periodically checks if the wrong address is ready to be fixed
# O(n) on average and O(n^2) at worst since it has to iterate through the packagesRemaining array and look through the hash table for the package information
    def checkNewPackages(self):
        if self.currentTime > datetime.timedelta(hours=10, minutes=20, seconds=00):
            for x in self.packagesRemaining:
                if x.id == '9':
                    x.location = '410 S State St'
                    print('Corrected address')
                    loadedPackage = self.packagesHash.get(self.packagesRemaining[0].id)
                    loadedPackage[1] = x.location
                    packagesHash.remove(loadedPackage[0])
                    packagesHash.add(loadedPackage[0], loadedPackage)
        
# Checks the next package to be delivered and sets the location
# O(n^3) because it has to call the recalculate function
    def goToLocation(self):
        self.checkNewPackages()
        self.recalculate()
        package = self.packagesRemaining[0]
        packageLocation = package.location

        # Fixes hashmap
        loadedPackage = self.packagesHash.get(self.packagesRemaining[0].id)
        loadedPackage[8] = "in-route"
        loadedPackage[9] = self.currentTime
        packagesHash.remove(loadedPackage[0])
        packagesHash.add(loadedPackage[0], loadedPackage)
        
        self.drive(self.currentLocation, packageLocation)
        self.deliverPackage()

# Updates the arrays and the packages to be appended or removed
# O(1) on average and O(n) at worst since it uses an add, remove, and get on the hash table
    def deliverPackage(self):
        if len(self.packagesRemaining[0].id) == 1:
            print("Delivering package: #0" + self.packagesRemaining[0].id)
        else:
            print("Delivering package: #" + self.packagesRemaining[0].id)
        
        # Fixes hashmap
        loadedPackage = self.packagesHash.get(self.packagesRemaining[0].id)
        loadedPackage[8] = "Delivered"
        loadedPackage[10] = self.currentTime
        packagesHash.remove(loadedPackage[0])
        packagesHash.add(loadedPackage[0], loadedPackage)

        self.packagesFinished.append(self.packagesRemaining.pop(0))
    
# Used in sorting the distances of the packages
# O(1) time
    def getDistance(self, node):
        return node.distance

# Used before traveling to each package and sorts to see which package is the closest
# O(n^3) + O(nlogn) = O(n^3) since they are not nested and n^3 is more significant than O(nlogn)
    def recalculate(self):
        # The efficiency of this for block is O(n^3) since I'm iterating through an array which is O(n) and then calling the searchDistance function which is O(n^2) and they are nested
        for x in self.packagesRemaining:
            x.distance = float(searchDistance(self.currentLocation, x.location))
        # This sort function is O(n log n)
        self.packagesRemaining.sort(key=self.getDistance)