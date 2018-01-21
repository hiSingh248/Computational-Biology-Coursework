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



def editDistance(s1,s2):
    

    #appending a random character at matrix[0,0] position
    s1='$'+s1
    s2='$'+s2
    
    len_s1= len(s1)
    len_s2= len(s2)
    
    #initialize an empty matrix of len_s1 * len_s2
    distanceMatrix = np.zeros((len_s1,len_s2))

    #updates 1st column with 1 to length of string s1
    for i in range(1,len_s1): 
        distanceMatrix[i][0] = i
    #print(distanceMatrix)
    
    #updates 1st row with 1 to length of string s2
    for j in range(1,len_s2): 
        distanceMatrix[0][j] = j
    

  

    #starts iteration from 1st column keeping 0th column intact
    for j in range(1,len_s2):
        # iterates through all the rows
        for i in range(1,len_s1):

            #replaces the cell value by upper diagonal value if the character in ith row is equal to jth column indicating no change with 0 value          
            if s1[i] == s2[j]:
                
                distanceMatrix[i][j] =distanceMatrix[i - 1][j - 1]              
            #no match- replaces the cell value by the minimun of upper row value +1(deletion) ,left column value+1(insertion), upper diagonal value +1(substitution)  
            else:               
                distanceMatrix[i][j] = min(distanceMatrix[i - 1][j]+1,  #deletion
                                           distanceMatrix[i][j - 1] +1, #insertion
                                           distanceMatrix[i-1][j-1]+ 1) #substitution
    
    print(distanceMatrix)
    distance=distanceMatrix[len_s1-1][len_s2-1]



    
    rows=len_s1-1
    cols=len_s2-1
    
    s1=list(s1)
    s2=list(s2)
    updatedS1=[]
    updatedS2=[]
    
    while rows > 0 and cols > 0:
        #calculates min distance from the right most corner
        minDist=min(distanceMatrix[rows][cols],distanceMatrix[rows-1][cols],distanceMatrix[rows][cols-1])
        
       # appends character to s1 and s2 if matches
        if minDist==distanceMatrix[rows][cols]:
            updatedS1.append(s1[rows])
            updatedS2.append(s2[cols])            
            
            rows-=1
            cols-=1
        #appends character to s1 if distance = adjacent top
        #appends character to s2 if distance =adjacent left
        elif minDist!=distanceMatrix[rows][cols]:
            
            if minDist==distanceMatrix[rows-1][cols]:
                updatedS2.append('-')
                updatedS1.append(s1[rows])
                rows-=1
            elif minDist==distanceMatrix[rows][cols-1]:
                updatedS1.append('-')
                updatedS2.append(s2[cols])
                cols-=1
       

    output=''.join(reversed(updatedS1)),''.join(reversed(updatedS2))
    return distance, output



if __name__ == '__main__':
    
    path = 'C:\\Users\\Himani\\Desktop\\CompBio\\RosProject2\\Data\\DataFile.fasta' 
   
        
    inputStrings=readFasta(path)
    distance,output=editDistance(inputStrings[0],inputStrings[1])
    print(distance)
    print(output)