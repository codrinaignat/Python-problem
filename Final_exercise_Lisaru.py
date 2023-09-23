# 1. Ex1 starts from here

import re
input = open('Database.txt', 'r')
fileContent = input.read()

# 2. Ex2 starts from here

myBigList = fileContent.split("<")
#len(myBigList) returns 71

x = range(71)
DAEList = []
ADAList = []
RPAList = []
LVList = []
ASQList = []

for n in x:
    if 'PpDae' in myBigList[n]:
        DAEList.append(myBigList[n])
    elif 'Ada' in myBigList[n]:
        ADAList.append(myBigList[n])
    elif 'PpRpa' in myBigList[n]:
        RPAList.append(myBigList[n])
    elif 'PpLv' in myBigList[n]:
        LVList.append(myBigList[n])
    elif 'Asq' in myBigList[n]:
        ASQList.append(myBigList[n])
    else:
        print(' ')
print(*DAEList, sep='\n')
#print(*ADAList, sep='\n')
#print(*RPAList, sep='\n')
#print(*LVList, sep='\n')
#print(*ASQList, sep='\n')

#Ex3 starts from here

lines = fileContent.split('\n')
def parameterStringsToDictionaries (stringLines):
    
    keys = []
    values = []
    listOfDictionaries = []

    for line in stringLines:
        withoutBrackets = line.replace('<', '').replace('/>', '')
        words = re.split(r'" |="|"', withoutBrackets)
        words.pop()

        for index, word in enumerate(words):
            if (index % 2 == 0):
                keys.append(word)
            else:
                values.append(word)

        singleDictionary = dict(zip(keys, values))
        listOfDictionaries.append(singleDictionary)

    print(*listOfDictionaries, sep='\n')
    #print(listOfDictionaries)
    return

parameterStringsToDictionaries(lines)

# 4. With the defined function create a single dictionary having the keys the names of the
# basic functions and the value the list of dictionaries (previously obtained) (e.g. {RPA:[{}, {}], DAE:[{}, {}]})



# 5. Using the obtained dictionary, print the Parameter_name value where the key „value“ has array (the type is defined as: type=„type[]“)

# 6. Using the obtained dictionary, print the Parameter_name where the key „lib:fusi “ is 1

# 7. Using the obtained dictionary, for the parameters of type Uint16, replace the „dd:MaxRange“ value which is
# different than the maximum value allowed by the data type (65 535)

# 8. Write the dictionary in a Output.exe file
