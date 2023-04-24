"""

Read CSV without using csv module
"""

lines = [line for line in open("../in/google_stock_data.csv")]
""

#Display Headers
print(lines[0])

print(lines[1])

#Remove any leading and trailing white space
print(lines[0].strip())

#Partition the data by splitting
print(lines[0].strip().split(','))

dataset = [lines.strip().split(',') for line in open('google_stock_data.csv')]



