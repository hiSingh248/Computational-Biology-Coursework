import sys
import numpy as np


def readFasta(path):
    
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
    return strings



def optimalAlignmentScore(s1,s2):
    

    #appending a random character at matrix[0,0] position
    s1='$'+s1
    s2='$'+s2
    
    len_s1= len(s1)
    len_s2= len(s2)
    
    #initialize an empty matrix of len_s1 * len_s2
    scoreMatrix = np.zeros((len_s1,len_s2))
    alignmentCounts = np.zeros((len_s1,len_s2))
   
    #updates 1st column with 1 to length of string s1
    for i in range(0,len_s1): 
        scoreMatrix[i][0] = i
        alignmentCounts[i][0] = 1
    
    
    #updates 1st row with 1 to length of string s2
    for j in range(1,len_s2): 
        scoreMatrix[0][j] = j
        alignmentCounts[0][j] = 1      

  

    #starts iteration from 1st column keeping 0th column intact
    for j in range(1,len_s2):
        # iterates through all the rows
        for i in range(1,len_s1):

            scores = [scoreMatrix[i-1][j-1] + (s1[i-1] != s2[j-1]),
                     scoreMatrix[i-1][j] + 1,
                      scoreMatrix[i][j-1] + 1]
            scoreMatrix[i][j] = min(scores)
    

            if scoreMatrix[i][j] == scores[0]:
                alignmentCounts[i][j] += alignmentCounts[i-1][j-1]
            if scoreMatrix[i][j] == scores[1]:
                alignmentCounts[i][j] += alignmentCounts[i-1][j]
            if scoreMatrix[i][j] == scores[2]:
                alignmentCounts[i][j] += alignmentCounts[i][j-1]

           
            alignmentCounts[i][j] = alignmentCounts[i][j] % 134217727
    
    return alignmentCounts[-1][-1]
 




    



if __name__ == '__main__':
    
    path = 'C:\\Users\\Himani\\Desktop\\CompBio\\RosProject2\\Data\\DataFile.fasta' 
    inputStrings=readFasta(path)
  
      
    output=optimalAlignmentScore(inputStrings[0],inputStrings[1])
    print(output)