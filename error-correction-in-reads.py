from collections import Counter

def hammingDistance(read1, read2):
    mutations = 0
    for i in range(len(read1)):
        if read1[i] != read2[i]:
            mutations += 1
    return mutations


def ReverseComplement(read):
    
    read = read[::-1]
    revRead=''
    for i in range(len(read)):
        if read[i]=='A':
            revRead+='T'
        elif read[i]=='T':
            revRead+='A'
        elif read[i]=='G':
            revRead+='C'
        elif read[i]=='C':
            revRead+='G'
               
    return revRead

def divideReads(freq, inputStrings):
    correctReads = []
    incorrectReads = []
    for i in freq:
        #if read occurs more than or equal to twice, append to correct Reads
        if freq[i] >= 2:
            correctReads.append(i)
        #else to incorrect reads
        else:
            incorrectReads.append(i)
    
    return correctReads, incorrectReads

def findCorrections(correctReads, incorrectReads):
    listCorrections = []
    for oldRead in incorrectReads:
        for newRead in correctReads:
            #each incorrect read has hamming distance 1 w.r.t to exactly one correct read
            if hammingDistance(oldRead, newRead) == 1:
                listCorrections.append([oldRead, newRead])
    return listCorrections


def getFreqCount(inputStrings):
    
    freq = dict()

    for i in inputStrings:
        #if already in dict, increase count by 1
        if i in freq:
            freq[i] += 1
        # if reverse complement exists in dict, then increase count by 1
        elif ReverseComplement(i) in freq:
            freq[ReverseComplement(i)] += 1
        #else set to 1
        else:
            freq[i] = 1
            freq[ReverseComplement(i)] = 1

    return freq


def readFasta(path):
    
    strings=[]   
    checkEnd = ''
    readFile = open(path,'r')
    for fasta_item in readFile:
            
            if fasta_item[0] == ">":
                
                if checkEnd != '':
                    strings.append(checkEnd)
                checkEnd = ''
            else:
              checkEnd += fasta_item.strip()
    strings.append(checkEnd)
    return strings

if __name__ == '__main__':
    
    
    inputStrings=readFasta('DataFile.fasta')
    inputStrings += [ReverseComplement(i) for i in inputStrings]
    freq = getFreqCount(inputStrings)
    correctReads, incorrectReads = divideReads(freq, inputStrings)
    listCorrections = findCorrections(correctReads, incorrectReads)
    
    for i in listCorrections:
        print('->'.join(i) + '\n')