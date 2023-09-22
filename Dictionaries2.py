import re

input = open('Database2.txt', 'r')
fileContent = input.read()
withoutBrackets = fileContent.replace('<', '').replace('/>', '')
# withoutNewlines = withoutBrackets.replace('\n', '')

lines = withoutBrackets.split('\n')

keys = []
values = []
listOfDictionaries = []

for line in lines:
    words = re.split(r'" |="|"', line)
    words.pop()

    for index, word in enumerate(words):
        if (index % 2 == 0):
            keys.append(word)
        else:
            values.append(word)

    singleDictionary = dict(zip(keys, values))
    listOfDictionaries.append(singleDictionary)

print(*listOfDictionaries, sep='\n')
