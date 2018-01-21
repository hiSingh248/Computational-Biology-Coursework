import math


path = 'C:/Users/Himani/Desktop/CompBio/TestFasta.fasta'
strings=[]
IDs=[]
checkEnd = ''
readFile = open(path,'r')
for fasta_item in readFile:
    
        if fasta_item[0] == ">":
            IDs.append(fasta_item[1:].strip())
            if checkEnd != '':
                strings.append(checkEnd)
            checkEnd = ''
        else:
          checkEnd += fasta_item.strip()

strings.append(checkEnd)

outputString=strings[0]

def merge(strings,outputString):
    
    for item in strings:
        
       for i in range(1,len(strings)):
            item = strings[i]            
            checkLength = len(item)
            

            for prefixCheck in range(math.floor((checkLength / 2))):
                suffixCheck = checkLength - prefixCheck

                if outputString.startswith(item[prefixCheck:]):
                    strings.remove(strings[i])
                    return merge(strings, item[:prefixCheck] + outputString)

                if outputString.endswith(item[:suffixCheck]):
                    strings.remove(strings[i])
                    return merge(strings, outputString + item[suffixCheck:])
    return outputString

    
checkVal=merge(strings,outputString)
print(checkVal)
print(len(checkVal))