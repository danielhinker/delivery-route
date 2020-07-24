from search import searchDistance
from hashmap import packagesHash

class Truck:

    def __init__(self, h):
        self.currentLocation = "4001 South 700 East"
        self.packagesLoaded = []
        self.packagesRemaining = []
        self.packagesHash = packagesHash
        self.distance = 0.0

    def getJob(self, packagesList):
        self.packagesRemaining = packagesList

    def goToLocation(self):
        package = self.packagesHash.get(str(self.packagesRemaining[0]))
        packageLocation = package[1]
        distanceToLocation = searchDistance(self.currentLocation, packageLocation)
        self.distance += float(distanceToLocation)
        print("Going to: " + packageLocation)
        print("Total distance: " + str(self.distance))
        self.loadPackage()
        # print(self.h.get('1')[1])
        # print(self.currentLocation)
        # print(str(self.packagesRemaining[0]))
        # print(self.h.get(str(self.packagesRemaining[0]))[1])
    
    def loadPackage(self):
        print("Loading package: #" + self.packagesRemaining[0])
        # print("Packages Loaded: " + self.packagesRemaining[0])
        self.packagesLoaded.append(self.packagesRemaining.pop(0))
        
        
        # print(self.packagesLoaded)
        # print("Packages Remaining: " + self.packagesRemaining)


        
    
        