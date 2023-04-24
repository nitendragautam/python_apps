#Open a file

#Open the file in write mode
fo = open('test.txt', 'w')

#Info of File
print('Name: ',fo.name)

print('Is Closed: ', fo.closed)
print('File Opening mode: ',fo.mode)

fo.write('This is a test')
fo.write('\n I repeat')
fo.close()

#Open and Append File
fo = open('test.txt', 'a') #Open file in Append Mode

fo.write('\n Still Testing')
fo.close()

#Read from File
fo = open('test.txt', 'rt')
text = fo.read(10)
print(text)

#Create a file
fo = open('test2.txt', 'w+')
fo.write('This is a new File')
fo.close()
