import csv
from datetime import datetime


"""
Manipulating CSV using csv Utility
"""

#Print Classes and Utility in module
print(dir(csv))

path = '../in/google_stock_data.csv'

#Open the file
file = open(path,newline ='')

reader = csv.reader(file)

header = next(reader) #First Line is the header

data = [row for row in reader] #Read the remaining data

print(header)
print(data[0]) #Data is still being read as String


data = []
for row in reader:
    # row = [Date, Open, High, Low, Close, Volume, Adj. Close] #This CSV has different data types
    date = datetime.strftime(row[0],'%m/%d/%Y')
    open_price = float(row[1]) #'open' is a builtin python function

