import csv

def searchDistance(start, end):
    with open('distances.csv') as csvfile:
        filtered = (line.replace('\n', '') for line in csvfile)
        reader = csv.reader(filtered)
        counter = 0
        columnIndex = 0
        
        for i, row in enumerate(reader):
            if i==0:
                # print(row[4])
                for j, column in enumerate(row):
                    if end in column:
                        # print(j)
                        # print(end)
                        # print(column)
                        
                        columnIndex = j
                        # print(type(j))
            else:
                for j, rowElement in enumerate(row):
                # print(row[0])
                # if i==3:
                    # print(row)
                    if start in rowElement:
                        # print('yes')
                        return row[columnIndex]
 
 

# print(searchDistance('1060 Dalton Ave S(84104)', '4001 South 700 East'))
# print(searchDistance('1330 2100 S', '4001 South 700 East'))

