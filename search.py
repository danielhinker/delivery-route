import csv

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
                # print(row[4])
                for j, column in enumerate(row):
                    if end in column:
                        columnIndex = j
                        
            else:
                for j, rowElement in enumerate(row):
                # print(row[0])
                # if i==3:
                    # print(row)
                    if start in rowElement:
                        # print('yes')
                        rowIndex = j
                        if row[columnIndex] == '':
                            return searchDistance(end, start)

                        else:
                            return row[columnIndex]
            
                    # else:
                    #     return row
 
 

# print(searchDistance('1060 Dalton Ave S(84104)', '4001 South 700 East'))
# print(searchDistance('1330 2100 S', '4001 South 700 East'))
# print(searchDistance('1330 2100 S', '1060 Dalton Ave S'))
# print(searchDistance('4001 South 700 East', '3575 W'))

