from search import searchDistance
from hashmap import packagesHash
from utils import currentTime
import datetime

class Truck:

    def __init__(self, hashmap, name):
        self.currentLocation = "4001 South 700 East"
        
        self.packagesRemaining = []
        self.packagesFinished = []
        self.allPackages = []
        self.packagesHash = hashmap
        self.distance = 0.0
        self.speed = 18.0
        self.currentTime = currentTime
        self.hubLocation = "4001 South 700 East"
        self.name = name
        

    def getJob(self, packagesList):
        self.allPackages = packagesList
        # print(len(packagesList))
        
        for i, x in enumerate(self.allPackages):
            
            if len(self.packagesRemaining) != 10:
                
                self.packagesRemaining.append(x)
        
        for i, x in enumerate(self.packagesRemaining):
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
        print("Current Time: " + str(self.currentTime))
        print("Total distance: " + str(self.distance))
        # print("Took: " + str(timeTaken) + " hours")
        
        self.currentLocation = endLocation
        


    def goToHub(self):
        
        self.drive(self.currentLocation, self.hubLocation)
        print("Finished going to hub")
        self.getJob(self.allPackages)

        # for x in self.packagesLoaded:
            # self.packagesFinished.append(x)

            # print("Delivering package: #" + x.id)
            
            # Fixes hashmap
            # deliveredPackage = self.packagesHash.get(x.id)
            # deliveredPackage[8] = "delivered"
            # deliveredPackage[9] = self.currentTime
            # packagesHash.delete(deliveredPackage[0])
            # packagesHash.add(deliveredPackage[0], deliveredPackage)
        self.recalculate()
        
        

    def goToLocation(self):
    
        self.recalculate()
        
        # if self.currentTime > datetime.timedelta(hours=10, minutes=20, seconds=00):
        #     for x in self.packagesRemaining:
        #         if x.id == '9':
        #             x.location = '410 S State St'
        #             print('Corrected address')
        #             loadedPackage = self.packagesHash.get(self.packagesRemaining[0].id)
        #             loadedPackage[1] = x.location
        #             packagesHash.delete(loadedPackage[0])
        #             packagesHash.add(loadedPackage[0], loadedPackage)
        #             print(x.location)
            
        package = self.packagesRemaining[0]
        packageLocation = package.location
        
        self.drive(self.currentLocation, packageLocation)
        
        # Fixes hashmap
        # loadedPackage = self.packagesHash.get(self.packagesRemaining[0].id)
        # loadedPackage[8] = "in-route"
        # loadedPackage[10] = self.currentTime
        # packagesHash.delete(loadedPackage[0])
        # packagesHash.add(loadedPackage[0], loadedPackage)

        # print(loadedPackage)
        self.deliverPackage()
        
    
    def deliverPackage(self):
        print("Delivering package: #" + self.packagesRemaining[0].id)
        # self.packagesLoaded.append(self.packagesRemaining.pop(0))
        a = self.packagesRemaining.pop(0)
        self.packagesFinished.append(a)
        print(self.currentTime)
        print("Finished delivering package")
      
    
    def getDistance(self, node):
        return node.distance

    def recalculate(self):
        # The efficiency of this for block is O(n) since I'm iterating through an array and changing values
        for x in self.packagesRemaining:
            x.distance = float(searchDistance(self.currentLocation, x.location))
        # This sort function is O(n log n)
        self.packagesRemaining.sort(key=self.getDistance)