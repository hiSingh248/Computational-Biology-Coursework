def countSymbols(symbol,index,lastColumn):
    slicedBWT=lastColumn[:index]
    occurences=slicedBWT.count(symbol)
    return occurences
    


def BetterBwMatching(lastColumn, pattern):
    
    lastColumn=list(lastColumn)
    firstColumn=sorted(lastColumn)
    
    top = 0
    bottom = (len(lastColumn))-1
    while top <= bottom:
        if len(pattern)!=0:
            symbol =pattern[-1]            
            pattern=pattern[:-1]
           
            if symbol in lastColumn[top:bottom+1]:            
                index=firstColumn.index(symbol)
                top = index+countSymbols(symbol,top,lastColumn)              
                bottom = index+countSymbols(symbol,bottom+1,lastColumn)-1
               
            else:
                return 0
        else:
            
            return bottom - top + 1
  
   
        

    
if __name__ == '__main__':
    
    file = open('C:\\Users\\Himani\\Desktop\\CompBio\\RosProject2\\Data\\DF.txt','r')
    lines = file.readlines()
    inputData = lines[0].strip()    
    inputPatterns=lines[1].split()
    
    patternOccurences=[]
    for j in range(0,len(inputPatterns)):
        
        patternOccurences.append(BetterBwMatching(inputData, inputPatterns[j]))
        
    
    for x in patternOccurences:
        print(x, end=' ')