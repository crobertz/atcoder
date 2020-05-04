string = input()

test = ['dream','dreamer','erase','eraser']

def constructible(string,testlist):
  if string == '':
    return 'YES'
  else:
    for word in testlist:
      if len(word) <= len(string):
        if string[-len(word):] == word:
          return constructible(string[:-len(word)],testlist)
    return 'NO'

print(constructible(string,test))
