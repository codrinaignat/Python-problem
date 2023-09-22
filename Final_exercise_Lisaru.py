# 1. Open and read the information from Database.txt

input = open('Database.txt', 'r')
myString = input.read()



# 2. Create 5 lists for each basic function (the prefix of the Parameter_name value indicates the basic function
# PpDae – DAE (DriverActivityEstimation),
# Ada – ADA (ActionDecisionAsil),
# PpRpa – RPA (ReferencePointAdjustment),
# PpLv – LV (LaneVerification),
# Asq – ASQ (ActionSuppressionQM)),
# where the list elements are the lines from the text file (e.g [„string line1“, „string lineX“])

myBigList = myString.split("<")

#len(myBigList) returns 71

x = range(71)
PpDaeList = []
AdaList = []
PpRpaList = []
PpLvList = []
AsqList = []


for n in x:
    if 'PpDae' in myBigList[n]:
        PpDaeList.append(myBigList[n])
    elif 'Ada' in myBigList[n]:
        AdaList.append(myBigList[n])
    elif 'PpRpa' in myBigList[n]:
        PpRpaList.append(myBigList[n])
    elif 'PpLv' in myBigList[n]:
        PpLvList.append(myBigList[n])
    elif 'Asq' in myBigList[n]:
        AsqList.append(myBigList[n])
    else:
        print(' ')


# 3. Define a function to create a list of dictionaries where
# the key and value pairs are obtain from the equality (there should be 6 pairs)
# e.g. [{key1:value1, key2:value3}, {key1:value2, key2:value4}])

#def CreateDictionariesList ()

# 4. With the defined function create a single dictionary having the keys the names of the
# basic functions and the value the list of dictionaries (previously obtained) (e.g. {RPA:[{}, {}], DAE:[{}, {}]})

# 5. Using the obtained dictionary, print the Parameter_name value where the key „value“ has array (the type is defined as: type=„type[]“)

# 6. Using the obtained dictionary, print the Parameter_name where the key „lib:fusi “ is 1

# 7. Using the obtained dictionary, for the parameters of type Uint16, replace the „dd:MaxRange“ value which is
# different than the maximum value allowed by the data type (65 535)

# 8. Write the dictionary in a Output.exe file
