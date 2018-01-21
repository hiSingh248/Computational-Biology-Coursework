import sys
path = 'C:/Users/Himani/Desktop/Comp Bio/TestFasta.fasta'
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

codonTable={
    'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAU':'N', 'AAC':'N', 'GAU':'D', 'GAC':'D', 'UGU':'C', 'UGC':'C',
    'CAA':'Q', 'CAG':'Q', 'GAA':'E', 'GAG':'E', 'GGU':'G', 'GGC':'G',
    'GGA':'G', 'GGG':'G', 'CAU':'H', 'CAC':'H', 'AUU':'I',
    'AUC':'I', 'AUA':'I', 'AUG':'START', 'UUA':'L', 'UUG':'L','CUU':'L',
    'CUC':'L', 'CUA':'L', 'CUG':'L', 'AAA':'K', 'AAG':'K', 'AUG':'M',
    'UUU':'F', 'UUC':'F', 'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S', 'AGU':'S', 'AGC':'S',
    'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T', 'UGG':'W', 'UAU':'Y',
    'UAC':'Y', 'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V', 'UAA':'STOP',
    'UGA':'STOP', 'UAG':'STOP'
    }
testProteinString=''
testDataset=""


item = strings[0]
print(item)
lengthBefore=len(item)
print(lengthBefore)
counter=0
for j in range(1, len(strings)):
    itemToCompare = strings[j]
   
    lengths=len(itemToCompare)
    counter=counter+lengths
   
    
    item = item.replace(itemToCompare,'')
print(counter)

    

item=item.replace('T','U');
print(item)
lengthAfter=len(item)
print(lengthAfter)
for i in range(0, len(item), 3):
    valToMatch=item[i:i+3]
    if valToMatch in codonTable:
        val_CodonTable= codonTable[valToMatch]
        if val_CodonTable != 'STOP' and val_CodonTable != 'START':   
            testProteinString += val_CodonTable
           
print(testProteinString)