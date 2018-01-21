from random import sample
def datasetPreprocess(edges):
    #creates a dictionary of edges 
    edgeSet = dict()
    for edge in edges:
        startState, transition, endState = edge.split(' ')        
        endStates = endState.split(',')
        edgeSet[startState] = set(endStates)
    return edgeSet

    


def eulerianPath(edgeSet):
    # finds number of incoming and outgoing edges for every node and creates a dict of indgrees and outdegrees
    
    inDegree = dict()
    outDegree = dict()
    
    
    for sNode in edgeSet:
        
        if sNode not in inDegree:
            inDegree[sNode] = 0
        outDegree[sNode] = len(edgeSet[sNode])
        
        for dNode in edgeSet[sNode]:
            if dNode not in outDegree:
                outDegree[dNode] = 0
                
            if dNode in inDegree:
                inDegree[dNode] += 1
            else:
                inDegree[dNode] = 1
                
            
                
    #print('inDegree',inDegree)
    #print('outDegree',outDegree)

    #finds start node and destination Node of the path
    
    for node in inDegree:
        
        incomingEdges=inDegree[node]
        outgoingEdges=outDegree[node]

        #sets the start node if outgoingEdges is 1 more than incoming edges
        
        if outgoingEdges == incomingEdges + 1:
           startState = node
           
        #sets the end node if incomingEdges is 1 more than the outgoing edges
        elif incomingEdges == outgoingEdges + 1:
           endState = node

    #print(startState,endState)
    
    if endState in sorted(edgeSet):
        edgeSet[endState].add(startState)
    else:
        edgeSet[endState] = set([startState])

    cycle, subset = processSubsets(edgeSet, startState)
    
    while subset:
        for i, s in enumerate(cycle):
            if s in subset:
                k, subset = processSubsets(subset, s)
                
                cycle = cycle[:i] + k + cycle[i+1:]
                break
    cycle=cycle[:-1]
    
    return cycle


def processSubsets(edgeSet, sNode):
    
    cycle = [sNode]
    node = sNode
    isTraversed = False
    while not isTraversed:
       
        # gets all the destination nodes corresponding to the startnode
        dests = edgeSet.get(node)
        if dests != None:
            #takes the first element as destination node
            dest = dests.pop()
            dests.add(dest)
            #dest=sample(dests, 1)[0]
            if len(dests) > 1:
                graph[node] = dests - set([dest])
               
            else:
                del(graph[node])
                
            cycle.append(dest)
            
            if dest==sNode:
                isTraversed = True
            else:
                node=dest
        else:
            isTraversed = True
            
    return cycle, graph
   

if __name__=="__main__":
    with open('sample.txt') as f:
        inputStrings = f.readlines()
        edges = [x.strip() for x in inputStrings] 
    graph = datasetPreprocess(edges)
    path = eulerianPath(graph)

    print('->'.join(path))