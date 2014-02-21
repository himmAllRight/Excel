#Hamming Code version 2.0
#July 18th 2012
#imports the discrete log and does a hamming comparison on two lines, through the entire document in reverse.

import sys

#Reads the data and puts it into list form
def readinfo(infile,outfile):
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
    
#Prints the results to a file            
def printToFile(infile1, outfile, resultList):
    for cellSet in resultList:
        for cellValue in cellSet:
            print(cellValue, end='', file=outfile)
        print(file=outfile)
    infile1.close()
    outfile.close()
    return(outfile)

#####################################################
############     Execution Code      ################
#####################################################
#####################################################

#Rename to change input and export files.
infilename = sys.argv[1]
outfilename = sys.argv[2]

#opens the input and output files.
infile = open(infilename, "r")
outfile = open(outfilename, "w")
print("File", infilename, "Opened")

#Execution Code
infileDataList = readinfo(infile, outfile)
result = hamming(infile, infileDataList)
outfile = printToFile(infile, outfile, infileDataList)
print("Finished. Output saved to", outfilename, end='\n')
