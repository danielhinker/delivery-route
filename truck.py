from search import searchDistance
from hashmap import packagesHash
from utils import currentTime
import datetime

class Truck:

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
        

    def getJob(self):
        for i, x in enumerate(self.allPackages[:]):
            
            if len(self.packagesRemaining) != 16:
                
                self.packagesRemaining.append(x)
                self.allPackages.remove(x)


    def drive(self, startLocation, endLocation):
        print(self.name)
        print("Current Location: " + startLocation)
        if endLocation == self.hubLocation:
            print("Going back to hub at 4001 South 700 East") 
        else:
            print("Going to: " + endLocation)
        distanceToLocation = searchDistance(startLocation, endLocation)
        self.distance += float(distanceToLocation)
        timeTaken = float(distanceToLocation) / self.speed
        self.currentTime += datetime.timedelta(hours=timeTaken)
        print("Time After Drive: " + str(self.currentTime))
        self.currentLocation = endLocation
        


    def goToHub(self):
        
        self.drive(self.currentLocation, self.hubLocation)
        self.getJob()
        self.recalculate()
        
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
        

    def goToLocation(self):
        self.checkNewPackages()
        self.recalculate()
        package = self.packagesRemaining[0]
        packageLocation = package.location

        # Fixes hashmap
        loadedPackage = self.packagesHash.get(self.packagesRemaining[0].id)
        loadedPackage[8] = "in-route"
        loadedPackage[10] = self.currentTime
        packagesHash.remove(loadedPackage[0])
        packagesHash.add(loadedPackage[0], loadedPackage)
        print("Current Time: " + str(self.currentTime))
        self.drive(self.currentLocation, packageLocation)
        self.deliverPackage()
        
    
    def deliverPackage(self):
        if len(self.packagesRemaining[0].id) == 1:
            print("Delivering package: ##0" + self.packagesRemaining[0].id)
        else:
            print("Delivering package: ##" + self.packagesRemaining[0].id)
        
        # Fixes hashmap
        loadedPackage = self.packagesHash.get(self.packagesRemaining[0].id)
        loadedPackage[8] = "delivered"
        loadedPackage[9] = self.currentTime
        packagesHash.remove(loadedPackage[0])
        packagesHash.add(loadedPackage[0], loadedPackage)

        self.packagesFinished.append(self.packagesRemaining.pop(0))
        
        print(self.currentTime)
      
    
    def getDistance(self, node):
        return node.distance

    def recalculate(self):
        # The efficiency of this for block is O(n) since I'm iterating through an array and changing values
        for x in self.packagesRemaining:
            x.distance = float(searchDistance(self.currentLocation, x.location))
        # This sort function is O(n log n)
        self.packagesRemaining.sort(key=self.getDistance)