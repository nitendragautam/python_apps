import re


OFile = open('../in/tagged_data.dat')


OData = OFile.read()

x= re.findall(r'<ts>(.*?)<ts>',OData,re.DOTALL)

for item in x:
    splittedItem = re.findall(r'<tv>(.*?)<tv>',item)

    print(len(splittedItem))
