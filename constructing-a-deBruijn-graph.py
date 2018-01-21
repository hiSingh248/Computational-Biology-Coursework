def ReverseComplement(kmer):
    
    kmer = kmer[::-1]
    revKmer=''
    for i in range(len(kmer)):
        if kmer[i]=='A':
            revKmer+='T'
        elif kmer[i]=='T':
            revKmer+='A'
        elif kmer[i]=='G':
            revKmer+='C'
        elif kmer[i]=='C':
            revKmer+='G'
               
    return revKmer



if __name__=="__main__":
    with open('sample.txt') as f:
        content = f.readlines()
        kmers = [x.strip() for x in content] 
    
    edgeSet= set()
    for kmer in kmers:
            edgeSet.add(kmer)            
            edgeSet.add(ReverseComplement(kmer))
    k = len(kmers[0])
    edge = lambda elmt: '('+elmt[0:k-1]+', '+elmt[1:k]+')'
    edges=[]
    for i in sorted(edgeSet):
        edges.append(edge(i))
    
  
    print( "\n".join(edges))