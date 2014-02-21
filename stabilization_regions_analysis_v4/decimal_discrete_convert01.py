#decimal to discrete converter for notchNucCounts.txt
#July 16th 2012
import sys
import math

#Reads the data and creates the mainData list.    
def readinfo(infile):
    dataList= []
    mainData = []
    for line in infile:
        line = line.strip('\n')
        dataList.append(line)
    for line in dataList:
        line = line.strip().split('\t')
        mainData.append(line)
    return(mainData)

#Reads through the data and re-assigns each value as a discrete one.
def convertToDiscrete(mainData):
    mainDataIndex = -1
    for cellSet in mainData:
        mainDataIndex = mainDataIndex+1
        cellSetIndex = -1
        for cellValue in cellSet:
            cellSetIndex = cellSetIndex +1
            cellValue = int(cellValue)
            logvalue = int(math.log10((cellValue)+.1))+1
            
            if(logvalue > 4):
                mainData[mainDataIndex][cellSetIndex] = 4
            else:
                mainData[mainDataIndex][cellSetIndex] = logvalue
          

    return(mainData)

#prints the new data to the outfile and Closes the files.
def printToFile(mainData, infile, outfile):
    for cellSet in mainData:
        for cellValue in cellSet:
            print(cellValue, end="", file=outfile)
        print(file=outfile)
    infile.close()
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
mainData = readinfo(infile)
mainData = convertToDiscrete(mainData)
outfile = printToFile(mainData, infile, outfile)
print("Finished. Output saved to", outfilename, end='\n')
