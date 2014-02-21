#hamming_graph v. 1.0
#September 2012
#Reads the hamming_output file and plot the changes

import sys
import copy

#Reads the data and puts it into list form
def readinfo(infile):
    mainList = []
    for line in infile:
        line = line.strip('\n')
        mainList.append(line)
        
    infile.close()
    return(mainList)

#Processes the input information to make the dataoutput file.
def processing(mainList):
	dataList = []
	lineChanges = 0
	index = 0
	for line in mainList:
		for cell in line:
			if(cell == "*"):
				lineChanges = lineChanges + 1
		dataList.append(lineChanges)
		lineChanges = 0
	return(dataList)
				
#Prints the results to a file            
def printToFile(dataList, outfile, outfilename):
	index = 0
	print("time,count", file=outfile)
	for dataValue in dataList:
		print(index, end="", file=outfile)
		print(",",end="", file=outfile)
		print(dataValue,end="\n", file=outfile)
		index = index + 1
	outfile.close()
	print("Data printed to",outfilename,"and the file was closed.")
	return(outfile)				
		



#####################################################
############     Execution Code      ################
#####################################################
#####################################################

#Rename to change input and export files.
infilename = sys.argv[1]
outfilename = sys.argv[2]

#Opens the input and output files.
infile = open(infilename, "r")
outfile = open(outfilename, "w")
print("File", infilename, "opened.")

#Execution Code
mainList = readinfo(infile)
dataList = processing(mainList)
printData = printToFile(dataList, outfile, outfilename)


