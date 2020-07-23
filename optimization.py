dict1 = {'a': [5.5, 10], 'b': [7.5, 20], 'c': [2.1, 15]}

dict2 = {}

route_array = []

node_array = []

# class Graph:
#     def __init__()


class Node:

    def __init__(self, name, distance, weight):
        self.name = name
        self.distance = distance
        self.weight = weight

for x in dict1:
    
    node_array.append(Node(x, dict1[x][0], dict1[x][1]))


def getDistance(node):
    return node.distance

node_array.sort(key=getDistance)

for node in node_array:
    print(node.name)
    
# for i, node in enumerate(node_array):
#     if not route_array:
#         route_array.append(node)
#     else:
#         if node.distance < route_array[i.distance]:
#             route_array.insert(node)