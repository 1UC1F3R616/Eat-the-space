import random

for t in range(5): # Change iterating range to increase number of files maded
    name=random.randrange(10000000000000000)
    file=open(str(name)+'.txt','w')

    file.write('I am Kushal \n COOL')
    file.close()

    fileRead=open(str(name)+'.txt','r')
    text_extract=fileRead.read()
    print(text_extract)

    fileRead.close()
