from search import searchDistance
from hashmap import packagesHash
from utils import currentTime
import datetime

class Truck:

    def __init__(self, h):
        self.currentLocation = "4001 South 700 East"
        self.packagesLoaded = []
        self.packagesRemaining = []
        self.packagesHash = packagesHash
        self.distance = 0.0
        self.speed = 18.0
        self.currentTime = currentTime
        self.huhLocation = "4001 South 700 East"

    def getJob(self, packagesList):
        self.packagesRemaining = packagesList

    
    def recalculate(self):
        pass

    def goToHub(self):
        
        print("Current Location: " + self.currentLocation)
        print("Going back to hub at 4001 South 700 East")
        
        distanceToLocation = searchDistance(self.currentLocation, self.huhLocation)
        print("Total distance: " + str(self.distance))
        timeTaken = float(distanceToLocation) / self.speed
        print("Took: " + str(timeTaken) + " hours")
        self.currentTime += datetime.timedelta(hours=timeTaken)
        print("Current Time: " + str(self.currentTime))
        self.packagesLoaded = []

    def goToLocation(self):
        if len(self.packagesLoaded) == 16:
            self.goToHub()
        else:
            package = self.packagesHash.get(self.packagesRemaining[0].id)
            packageLocation = package[1]
            distanceToLocation = searchDistance(self.currentLocation, packageLocation)
            self.distance += float(distanceToLocation)
            timeTaken = float(distanceToLocation) / self.speed
            
            print("Took: " + str(timeTaken) + " hours")
            print("Current Location: " + self.currentLocation)
            print("Going to: " + packageLocation)
            print("Total distance: " + str(self.distance))
            # print(currentTime)
            self.currentTime += datetime.timedelta(hours=timeTaken)
            print("Current Time: " + str(self.currentTime))
            self.currentLocation = packageLocation
            self.loadPackage()
            # print(self.h.get('1')[1])
            # print(self.currentLocation)
            # print(str(self.packagesRemaining[0]))
            # print(self.h.get(str(self.packagesRemaining[0]))[1])
    
    def loadPackage(self):
        print("Loading package: #" + self.packagesRemaining[0].id)
        # print("Packages Loaded: " + self.packagesRemaining[0])
        self.packagesLoaded.append(self.packagesRemaining.pop(0))
        # print("")
        
        
        # print(self.packagesLoaded)
        # print(self.packagesRemaining)


        
    
        