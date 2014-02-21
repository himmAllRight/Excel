#Third step

import sys
import copy

def readinfo(infile, outfile):
    dataList = []
    for line in infile:
        line = line.strip('\n')
        
        chIndex = -1
        lineList = []
        for ch in line:
            chIndex = chIndex + 1
            lineList.append(line[chIndex])
        dataList.append(lineList)
    infile.close()
    return(dataList)

def cumulate(dataList):
    index1 = -1
    index2 = -2
    for line in range(len(dataList)-1):
        cellIndex = 0
        for cell in range(0,len(dataList[index1])):
            if(dataList[index1][cellIndex] == "*" or dataList[index2][cellIndex] == "*"):
                dataList[index2][cellIndex] = "*"
            else:
                dataList[index2][cellIndex] = 0
            cellIndex = cellIndex + 1
        index1 = index1 - 1
        index2 = index2 - 1
    return(dataList)



def printToFile(outputData, outfile):
    for line in outputData:
        for cell in line:
            print(cell, end='', file=outfile)
        print(file=outfile)
    outfile.close()
    







#####################################################
############     Execution Code      ################
#####################################################
#####################################################

#Rename to change input and export files.
infilename = sys.argv[1]
outfilename = sys.argv[2]

#Opens input and output files
infile = open(infilename, "r")
outfile = open(outfilename, "w")

#Execution Code
dataList = readinfo(infile, outfile)
outputData = cumulate(dataList)
print = printToFile(outputData, outfile)

