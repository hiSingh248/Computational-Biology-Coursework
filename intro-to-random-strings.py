import sys
import math
path="C:/Users/Himani/Desktop/Comp Bio/TestProb6.txt"

def calc_log(testInputString, x):
    commonLog = 0
    for char in testInputString:
        if char in "GC":
            commonLog += (math.log10(x/2))
        else:
            commonLog += (math.log10((1-x)/2))
    
    commonLog=round(commonLog,3)
    print(commonLog)
 
 
lines = open(path).readlines()
testInputString=lines[0].strip()
GCContent=list(lines[1].strip().split())
new_list = [float(i) for i in GCContent]

for item in new_list:
    calc_log(testInputString,item)