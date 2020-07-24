# Hash Map

class PackagesHashMap:
        def __init__(self):
                self.size = 250
                self.map = [None] * self.size
		
        def _get_hash(self, key):
                hash = 0
                for char in str(key):
                        hash += ord(char)
                return hash % self.size
		
        def add(self, key, value):
                key_hash = self._get_hash(key)
                key_value = [key, value]
		
                if self.map[key_hash] is None:
                        self.map[key_hash] = list([key_value])
                        return True
                else:
                        for pair in self.map[key_hash]:
                                if pair[0] == key:
                                        pair[1] = value
                                        return True
                        self.map[key_hash].append(key_value)
                        return True
			
        def get(self, key):
                key_hash = self._get_hash(key)
                if self.map[key_hash] is not None:
                        for pair in self.map[key_hash]:
                                if pair[0] == key:
                                        return pair[1]
                return None
			
        def delete(self, key):
                key_hash = self._get_hash(key)
		
                if self.map[key_hash] is None:
                        return False
                for i in range (0, len(self.map[key_hash])):
                        if self.map[key_hash][i][0] == key:
                                self.map[key_hash].pop(i)
                                return True
                return False
	
        def keys(self):
                arr = []
                for i in range(0, len(self.map)):
                        if self.map[i]:
                                arr.append(self.map[i][0])
                return arr
			
        def print1(self):
                print('---PHONEBOOK----')
                for item in self.map:
                        if item is not None:
                                print(str(item))
        
        def search(self, packageId, address, city, state, zip, delivery, mass, status):
                for item in self.map:
                        if item is not None:
                                # if ['2', '2530 S 500 E', 'Salt Lake City', 'UT', '84106', 'EOD', '44', 'pending'] in item:
                                # return item[0][1][0]
                                if item[0][1][0] == packageId and item[0][1][1] == address and item[0][1][2] == city and item[0][1][3] == state and item[0][1][4] == zip and item[0][1][5] == delivery and item[0][1][6] == mass and item[0][1][8] == status:
                                        return item

			

packagesHash = PackagesHashMap()
# h.add('Ming', '293-6753')
# h.add('Ming', '333-8233')
# h.add('Ankit', '293-8625')
# h.add('Aditya', '852-6551')
# h.add('Alicia', '632-4123')
# h.add('Mike', '567-2188')
# h.add('Aditya', '777-8888')
# h.print1()		
# h.delete('Bob')
# h.print1()
# print('Ming: ' + h.get('Ming'))
# print(h.keys())




# # ZyBooks Im
# class HashTable:
#     # Constructor with optional initial capacity parameter.
#     # Assigns all buckets with an empty list.
#     def __init__(self, initial_capacity=10):
#         # initialize the hash table with empty bucket list entries.
#         self.table = []
#         for i in range(initial_capacity):
#             self.table.append([])
      
#     # Inserts a new item into the hash table.
#     def insert(self, item):
#         # get the bucket list where this item will go.
#         bucket = hash(item) % len(self.table)
#         bucket_list = self.table[bucket]

#         # insert the item to the end of the bucket list.
#         bucket_list.append(item)
         
#     # Searches for an item with matching key in the hash table.
#     # Returns the item if found, or None if not found.
#     def search(self, key):
#         # get the bucket list where this key would be.
#         bucket = hash(key) % len(self.table)
#         bucket_list = self.table[bucket]

#         # search for the key in the bucket list
#         if key in bucket_list:
#             # find the item's index and return the item that is in the bucket list.
#             item_index = bucket_list.index(key)
#             return bucket_list[item_index]
#         else:
#             # the key is not found.
#             return None

#     # Removes an item with matching key from the hash table.
#     def remove(self, key):
#         # get the bucket list where this item will be removed from.
#         bucket = hash(key) % len(self.table)
#         bucket_list = self.table[bucket]

#         # remove the item from the bucket list if it is present.
#         if key in bucket_list:
#             bucket_list.remove(key)

