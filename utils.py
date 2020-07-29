import datetime

class Node:
    
    def __init__(self, id, location, distance, *argv):
        for x in argv:
            self.zipCode = x
        self.id = id
        self.location = location
        self.distance = distance
        
currentTime = datetime.timedelta(hours=8, minutes=00, seconds=00)
