from search import searchDistance
from hashmap import packagesHash
from utils import currentTime
import datetime

class Truck:

    def __init__(self, h, name):
        self.currentLocation = "4001 South 700 East"
        self.packagesLoaded = []
        self.packagesRemaining = []
        self.packagesFinished = []
        self.packagesHash = packagesHash
        self.distance = 0.0
        self.speed = 18.0
        self.currentTime = currentTime
        self.huhLocation = "4001 South 700 East"
        self.timesToHub = 0
        self.name = name
        

    def getJob(self, packagesList):
        self.packagesRemaining = packagesList

    def getDistance(self, node):
        return node.distance

    def recalculate(self):
        for x in self.packagesRemaining:
            
            # b = packagesHash.get(x.id)
            x.distance = float(searchDistance(self.currentLocation, x.location))
        self.packagesRemaining.sort(key=self.getDistance)

    def goToHub(self):
        
        print(self.name)
        print("Current Location: " + self.currentLocation)
        print("Going back to hub at 4001 South 700 East")
        
        distanceToLocation = searchDistance(self.currentLocation, self.huhLocation)
        print("Total distance: " + str(self.distance))
        timeTaken = float(distanceToLocation) / self.speed
        print("Took: " + str(timeTaken) + " hours")
        self.currentTime += datetime.timedelta(hours=timeTaken)
        print("Current Time: " + str(self.currentTime))
        
        for x in self.packagesLoaded:
            self.packagesFinished.append(x)
        
        self.packagesLoaded = []
        print("Finished dropping at hub")
        
        

    def goToLocation(self):
        print(self.name)
        if len(self.packagesRemaining) < 11:
            self.recalculate()
        
        if self.currentTime > datetime.timedelta(hours=10, minutes=20, seconds=00):
            print("pass time")
            for x in self.packagesRemaining:
                if x.id == '9':
                    x.location = '410 S State St'
                    print('found')
                    print(x.location)
            print("pass time")
        if len(self.packagesLoaded) == 16:
            self.goToHub()
        else:
            # package = self.packagesHash.get(self.packagesRemaining[0].id)
            # print(package)
            package = self.packagesRemaining[0]
            packageLocation = package.location
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
            
            loadedPackage = package = self.packagesHash.get(self.packagesRemaining[0].id)
            loadedPackage[8] = "in-route"
            packagesHash.delete(loadedPackage[0])
            packagesHash.add(loadedPackage[0], loadedPackage)
            print(loadedPackage)
            self.loadPackage()
            print("finished loading packages")
          
    
    def loadPackage(self):
        print("Loading package: #" + self.packagesRemaining[0].id)
        self.packagesLoaded.append(self.packagesRemaining.pop(0))
      
    