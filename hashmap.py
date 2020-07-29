
class PackagesHashMap:
        
        # Initializes the hashmap
        def __init__(self):
                self.size = 50
                self.map = [None] * self.size
		
        # Creates a hash which determines where it is stored in the hashmap and helps with retrieval of it
        def _hasher(self, key):                
                return hash(key) % self.size
		
        # Add packages with the need of a key and a value to store it
        def add(self, key, value):
                hashedKey = self._hasher(key)
                key_value = [key, value]
		
                if self.map[hashedKey] == None:
                        self.map[hashedKey] = list([key_value])
                        return True
                else:
                        for x in self.map[hashedKey]:
                                if x[0] == key:
                                        x[1] = value
                                        return True
                        self.map[hashedKey].append(key_value)
                        return True
	
        # Gets packages using their package id
        def get(self, key):
                hashedKey = self._hasher(key)
                if self.map[hashedKey] != None:
                        for x in self.map[hashedKey]:
                                if x[0] == key:
                                        return x[1]
                return None
			
        # Removes packages from the hashmap
        def remove(self, key):
                hashedKey = self._hasher(key)
		
                if self.map[hashedKey] == None:
                        return False
                for i in range (0, len(self.map[hashedKey])):
                        if self.map[hashedKey][i][0] == key:
                                self.map[hashedKey].pop(i)
                                return True
                return False
        
        # Search function to find individual packages
        def search(self, packageId, address, city, state, zip, delivery, mass, status):
                for item in self.map:
                        if item != None:
                                if item[0][1][0] == packageId and item[0][1][1] == address and item[0][1][2] == city and item[0][1][3] == state and item[0][1][4] == zip and item[0][1][5] == delivery and item[0][1][6] == mass and item[0][1][8] == status:
                                        return item
                error = "None Found"
                return error
        
        # This function prints all the packages in the hashmap
        def all(self):
                for x in range(1, 41):
                        print(self.get(str(x)))
        
        # This creates the screenshots of where the packages are at given times
        def timeDelivered(self, timeStart, timeEnd):
                for x in range(1, 41):
                        package = self.get(str(x))
                        if package[10] > timeEnd and package[9] > timeEnd:
                                package[8] = "pending"
                                print(package)
                        elif package[9] < timeStart:
                                package[8] = "delivered"
                                print(package)
                        else:
                                package[8] = "in-route"
                                print(package)
                                
                        
packagesHash = PackagesHashMap()

