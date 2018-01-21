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
        inputStrings = f.readlines()
        kmers = [x.strip() for x in inputStrings]
        k = len(kmers[0])
    for res in range(1,k):
        edgeSet= set()
        # creates a set if edges by icluding both kmer and its complement
        for kmer in kmers:
                edgeSet.add(kmer)            
                edgeSet.add(ReverseComplement(kmer))
                
        #function to create left and right k-1-mers
        edge = lambda x: (x[0:k-1], x[1:k])

        #creates edges from left and right k-1-mers
        edges=[]       
        for i in sorted(edgeSet):
            
            edges.append(edge(i))
        #print(edges)

       
        cyclicSCS = []
        for m in range(2):
                first_edge = edges[0]   
                cyclic = first_edge[0][-1]
                edges.remove(first_edge)
                #print(edges)
                # iterates till node still exists in the edges
                edgeCheck = [j[0] for j in edges]
                while first_edge[1] in edgeCheck:
                        cyclic += first_edge[1][-1]
                        for i, m in enumerate(edges):
                            if m[0] == first_edge[1]:
                                index=i
                       
                        first_edge = edges[index]
                        edges.remove(first_edge)
                        edgeCheck=[j[0] for j in edges]
                cyclicSCS.append(cyclic)

       
        if len(edges) == 0:
            break
    print(cyclicSCS[1])