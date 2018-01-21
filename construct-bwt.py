import numpy

def rotations(t):
    tt = t * 2
    return[tt[i:i+len(t)]for i in range(0,len(t))]


def bwm(t):
    return sorted(rotations(t))
def bwtViaBwm(t):
    return ''.join(map(lambda x:x[-1],bwm(t)))
    

if __name__ == '__main__':
    
    inputData='CTCAACACGAATTTACCAATTGCATTTTATACACCCATTTAGCCAGGTACCCACAAGGCCCAACGCATCGGTCGCTGGCATCGTTTAACTACTCTAACTGCCCCTGTCCCGAGGCTCTTATGACTTTGCCGTTTTTCTGATCTGCTTGCGGGTTGAAGTCTGTAGCCTCTAATCGCGAGTGCGGAACTATTCACAGTGGTCGAATATTGGTGTGCTAATGTCGTCGATGCGTGTTCGGGACCCGCGCGCGTTCGTGCAACGGAAACTCTGCTTGATTTCGCCCCCGAAATTCCGTTAAGGCGAGCTTAACCTGACGTGGAGGGATGTGAAAGCAAATTAATGTTCCTGCTACGCGGCGAAGGCTAAACGGCCGGGGGGATTTTACTCCCTTCTTGAACATTATTCACTAAACGTTCGATCAACGCGCCCATTGAGTACAATCCCCAACATGCCTCCTCGGTCTCGATACCAAGTGCTATTCCATACTGGTCTCCTCCATCTTGGACAACTTACTTCCATCTGCATTCCAATAGATAATTTTCTCCTTTCACTCTTATCAACCCTTTCAGGTCGACTTTGCCCCCTTTGCATCATGTCTTTGCACAAGTGCATCGTGGCCTTAATGTAGTAAGTTGGAAAAGTCGCAGCGGCAACAAATTGTTTGTCAAAGTGGGGGCCCTCAGAGTCTTACCTTGGCCAGCCCGTTTCCTGAAACCAGAATGGAGGCCTCAAAGTAATTATGTATTGACGATACCGGTATGGGGTCGCCGGGATCAATCTCGCATACCTGATGCTTCGCGAGAGCTACACTTGCTGTGGGTGTGCAACTTGGAGGATTCTATGTACACTTGACGCAACCATAAGCATCGGGTTAATGGCTACGCTGGGTGACACCTTCGGGCTTACTGGAGGAGGGGCGACTGGTTAAACGCCCAT$'
    
    bwtData=bwtViaBwm(inputData)
    print(bwtData)