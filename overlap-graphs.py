import sys
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
##print(IDs)
#print(strings)


for i in range(0, len(strings)):
    item = strings[i]    
    #print(i)
    for j in range(0, len(strings)):
             itemToCompare = strings[j]
             if item!=itemToCompare:
                     itemSuffix= item[-3:]
                     itemPrefix= itemToCompare[:3]
                     if itemSuffix == itemPrefix:
                             print(IDs[i],IDs[j])