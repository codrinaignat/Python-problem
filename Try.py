import re
input = open('Database.txt', 'r')
myString = input.read()
myBigList = re.split(r'\n', myString)

x = range(len(myBigList)) 

#x = range(71)
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


        
        

    
