import csv

# Efficient of this search function is O(n^2) since it has nested arrays
# This block of code is to search through the distances csv file and return a distance based on the starting and ending location that is chosen.
# It is a recursive function since it calls itself and switches the start and end variables in order to search through the csv with the columns and rows switched.
def searchDistance(start, end):
    with open('distances.csv') as csvfile:
        filtered = (line.replace('\n', '') for line in csvfile)
        reader = csv.reader(filtered)
        counter = 0
        columnIndex = 0
        rowIndex = 0
        start = start[:10]
        end = end[:10]

        for i, row in enumerate(reader):
            
            if i==0:
                for j, column in enumerate(row):
                    if end in column:
                        columnIndex = j   
            else:
                for j, rowElement in enumerate(row):   
                    if start in rowElement:                      
                        rowIndex = j
                        if row[columnIndex] == '':
                            return searchDistance(end, start)
                        else:
                            return row[columnIndex]
            
   
 
 

