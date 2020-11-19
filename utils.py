import datetime

# Node class to represent packages and help with sorting them by distances.
class Node:
    
    def __init__(self, id, location, distance, *argv):
        for x in argv:
            self.zipCode = x
        self.id = id
        self.location = location
        self.distance = distance
        
# This initializes the starting time
# O(1) time
currentTime = datetime.timedelta(hours=8, minutes=00, seconds=00)
