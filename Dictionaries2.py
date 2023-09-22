import re

input = open('Database2.txt', 'r')
myString = input.read()
myNewString = myString.replace('/>', '')
myMoreNewString = myNewString.replace('<','')
myMoreNewString = myMoreNewString.replace('\n','')


myBiggerList = myMoreNewString.split('\n')

myBiggerList2 = re.split(r'" |="|"', myMoreNewString)
myBiggerList2.pop()

y = range(0, len(myBiggerList2))
Keys = []
Values = []


for m in y:
    if (m%2 == 0):
        Keys.append(myBiggerList2[m])
    else:
        Values.append(myBiggerList2[m])
 


ListOfDictionaries = []
#SingleDictionary = {Keys[i]: Values[i] for i in range(len(Keys))}
for i in range(len(Keys)):
    SingleDictionary = dict(zip(Keys, Values))
    ListOfDictionaries.append(SingleDictionary)
        
print(SingleDictionary)

print(len(Keys))
print(len(Values))
#print(ListOfDictionaries)

Dict2 = SingleDictionary
