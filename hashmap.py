
class PackagesHashMap:
        
        # Initializes the hashmap
        # O(n) since you would want the size to at the least match the number of packages and it has to create the many spaces in the hash table
        def __init__(self):
                self.size = 250
                self.map = [None] * self.size
		
        # Creates a hash which determines where it is stored in the hashmap and helps with retrieval of it
        # O(1) time complexity since all it does is return a value
        def _hasher(self, key):                
                return hash(key) % self.size
		
        # Add packages with the need of a key and a value to store it
        # Time complexity is O(1) on average when theres no hash collisions and O(n) at worst if hashcollision occurs
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
        # Time complexity is O(1) on average when theres no hash collisions and O(n) at worst if hashcollision occurs
        def get(self, key):
                hashedKey = self._hasher(key)
                if self.map[hashedKey] != None:
                        for x in self.map[hashedKey]:
                                if x[0] == key:
                                        return x[1]
                return None
			
        # Removes packages from the hashmap
        # Time complexity is O(1) on average when theres no hash collisions and O(n) at worst if hashcollision occurs
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
        # def search(self, packageId, address, city, state, zip, delivery, mass, status):
        def search(self, packageId):
                for x in self.map:
                        if x != None:
                                # if item[0][1][0] == packageId and item[0][1][1] == address and item[0][1][2] == city and item[0][1][3] == state and item[0][1][4] == zip and item[0][1][5] == delivery and item[0][1][6] == mass and item[0][1][8] == status:
                                if x[0][0] == packageId:
                                        return x
                error = "None Found"
                return error
        
        # This function prints all the packages in the hashmap
        # Time complexity is O(n) since it iterates through all the packages
        def all(self):
                for x in range(1, 41):
                        package = packagesHash.get(str(x))
                        a = package[9]
                        b = package[10]
                        package[9] = "Picked up: " + str(package[9])
                        package[10] = "Delivered: " + str(package[10])
                        print(self.get(str(x)))
                        package[9] = a
                        package[10] = b
        
        # This function is similar to the all function but only puts out the id and time
        # Time complexity is O(n) since it iterates through all the packages
        def timeOnly(self):
                for x in range(1,41):
                        package = self.get(str(x))
                        print("Package ID: " + package[0] + ", Delivered: " + str(package[10]))
        
        # This creates the screenshots of where the packages are at given times
        # Time complexity is O(n) since it iterates through all the packages
        def timeDelivered(self, timeStart, timeEnd):
                for x in range(1, 41):
                        package = self.get(str(x))
                        if package[9] > timeEnd and package[10] > timeEnd:
                                a = package[8]
                                package[8] = "pending"
                                print(package)
                                package[8] = a
                        elif package[10] < timeStart:
                                a = package[8]
                                package[8] = "delivered"
                                print(package)
                                package[8] = a
                        else:
                                a = package[8]
                                package[8] = "in-route"
                                print(package)
                                package[8] = a
                                
                        
packagesHash = PackagesHashMap()

