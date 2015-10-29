#YouTube tutorial "Python 3 Programming Tutorial"

import csv

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    print(readCSV)
    
    dates = []
    colors = []
    
    for column in readCSV:
        color = column[2]
        date = column[1]
        
        dates.append(date)
        colors.append(color)
    
    print(dates)
    print(colors)
    
    
        
        
        
        