#Hamming code for two files.
#July 16th 2012
import sys

#Reads the data and creates the mainData list.
def readinfo(infile):
    dataList= []
    infileDataList = []
    for line in infile:
        line = line.strip('\n')
        dataList.append(line)
    for line in dataList:
        line = line.strip().split('\t')
        infileDataList.append(line)
    return(infileDataList)

#compares the two files and assigns a 0 if they are the same and a * if the values are different.
def compare(infileDataList1, infileDataList2):
    resultList = []
    infileDataListIndex = -1
    for cellSet in infileDataList1:
        infileDataListIndex = infileDataListIndex + 1
        cellSetIndex = -1
        for cellValue in cellSet:
            cellSetIndex = cellSetIndex + 1
            if(infileDataList1[infileDataListIndex][cellSetIndex] == infileDataList2[infileDataListIndex][cellSetIndex]):
                infileDataList1[infileDataListIndex][cellSetIndex] = 0
            else:
                infileDataList1[infileDataListIndex][cellSetIndex] = "*"
    return(infileDataList1)

#Prints the data to the outfile
def printToFile(resultList, infile1, infile2, outfile):
    for cellSet in resultList:
        for cellValue in cellSet:
            print(cellValue, end='\t', file=outfile)
        print(file=outfile)
    infile1.close()
    infile2.close()
    outfile.close()
    return(outfile)


#####################################################
############     Execution Code      ################
#####################################################
#####################################################

#Rename to change input and export files.
infilename1 = sys.argv[1]
infilename2 = sys.argv[2]
outfilename = sys.argv[3]

#opens the input and output files.
infile1 = open(infilename1, "r")
infile2 = open(infilename2, "r")
outfile = open(outfilename, "w")
print("Files", infilename1, "and", infilename2, "Opened")

#Execution Code
infileDataList1 = readinfo(infile1)
infileDataList2 = readinfo(infile2)
resultList = compare(infileDataList1, infileDataList2)
outfile = printToFile(resultList, infile1, infile2, outfile)
print("Finished. Output saved to", outfilename, end='\n')
