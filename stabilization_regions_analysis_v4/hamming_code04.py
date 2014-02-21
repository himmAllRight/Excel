#Hamming Code version 4.0
#July 18th 2012
#imports the discrete log and does a hamming comparison on two lines, through the entire document in reverse.
#This model also then goes through shows the cumulative changes.

import sys
import copy

#Reads the data and puts it into list form
def readinfo(infile):
    mainList = []
    for line in infile:
        line = line.strip('\n')
        chIndex = -1
        lineList = []
        for ch in line:
            chIndex = chIndex + 1
            ch = int(ch)
            lineList.append(line[chIndex])
        mainList.append(lineList)
    infile.close()
    return(mainList)

#Running the hamming comparisons between two lines, in reverse through the document.
def hamming(infile, infileDataList):
    index1 = -1
    index2 = -2
    cellSet1 = infileDataList[index1]
    cellSet2 = infileDataList[index2]
    resultList = infileDataList
    for cellSet in range(0,len(infileDataList)-1):
        cellIndex = -1
        for callValue in infileDataList[index1]:
            if( infileDataList[index1][cellIndex] == infileDataList[index2][cellIndex]):
                resultList[index1][cellIndex] = 0
            else:
                resultList[index1][cellIndex] = "*"
            cellIndex = cellIndex + 1
        index1 = index1 - 1
        index2 = index2 - 1
    resultList.pop(0)
    return(infileDataList)
#shows the accumulation of changes through the hamming differences.
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
    
#Prints the results to a file            
def printToFile(data, outfile):
    for cellSet in data:
        for cellValue in cellSet:
            print(cellValue, end='', file=outfile)
        print(file=outfile)
    outfile.close()
    return(outfile)

#####################################################
############     Execution Code      ################
#####################################################
#####################################################

#Rename to change input and export files.
infilename = sys.argv[1]
hammingOutfilename = sys.argv[2]
cumulativeOutfilename = sys.argv[3]

#opens the input and output files.
infile = open(infilename, "r")
hammingOutfile = open(hammingOutfilename, "w")
cumulativeOutfile = open(cumulativeOutfilename, "w")
print("File", infilename, "Opened")

#Execution Code
mainList = readinfo(infile)
infileDataList = hamming(infile, mainList)
dataList = copy.deepcopy(infileDataList)
dataList = cumulate(dataList) 
printhamming = printToFile(infileDataList,hammingOutfile)
printcumulative = printToFile(dataList, cumulativeOutfile)
print("Finished. Hamming difference Output saved to", hammingOutfilename, end='\n')
print("Cumulative Hamming difference output saved to", cumulativeOutfilename, end='\n')
