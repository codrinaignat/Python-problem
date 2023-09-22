import re

input = open('Database2.txt', 'r')
#myString = input.read()
myString = '<Parameter_name="PpDae_d_DriverUncertain" value="0" type="tUInt16" dd:MinRange="0" dd:MaxRange="65535" lib:fusi="0"/> <Parameter_name="Ada_t_ReactionTimes" value="300 300 300 300" type="tUInt16[]" dd:MinRange="0" dd:MaxRange="65535" lib:fusi="0"/>'
myNewString = myString.replace('/>', '')
myMoreNewString = myNewString.replace('<','')


myBiggerList = myMoreNewString.split('\n')

myBiggerList2 = re.split(r'" |="', myMoreNewString)

y = range(0, len(myBiggerList2)-1)
SingleDictionary = {}
ListOfDictionaries = []


for m in y:
    if ((m%2 == 0)&(m<=11)):
        SingleDictionary[myBiggerList2[m]] = myBiggerList2[m+1]
        if (len(SingleDictionary))==6:
            ListOfDictionaries.append(SingleDictionary)
            
    elif ((m%2 == 1)&(m>=12)&(m<=23)):
        SingleDictionary[myBiggerList2[m]] = myBiggerList2[m+1]
        if (len(SingleDictionary))==6:
            ListOfDictionaries.append(SingleDictionary)
            
print(ListOfDictionaries)



