#!/usr/bin/python
#Last updated 12/4/2012 4:30 pm
import os
def f(string):
	return string.strip()
os.system('rm across_locations.txt')
#os.system('rm cumulativeLocations.txt')
os.system('find . -name "randseed-*" -printf "%h\n" |sort -u  >> "across_locations.txt"')

print("making 'hamminc_across_script'")

outfile=open("hamming_across_script", "w")
print("#!/bin/sh", file= outfile)

startDir = "~/Documents/Excel/test_data/"
across_locations = open("across_locations.txt", "r")
for line in across_locations:
   #jump into directory to make across comparison of all seeds.
   cmd = "cd " + line
   print(cmd, file= outfile, end="")
   cmd = 'find . -name "cumulative_output.txt" -printf "%h\\n" |sort -u  > "cumulativeLocations.txt"'
   print(cmd, file= outfile)
   #each across file
   cmd = "cd " + startDir
   print(cmd, file= outfile)
   print("#------------------------------------------------------", file= outfile)
outfile.close()
across_locations.close()

#Makes acrossData.txt files in each experiment directory.
print("running 'hamming_across_script'")
os.system('./hamming_across_script')

across_locations2 = open("across_locations.txt", "r")
outfile2=open("hamming_across_script2", "w")
print("#!/bin/sh", file= outfile2)
for lines in across_locations2:
	cmd = "cd " + startDir
	print(cmd, file=outfile2, end="\n")
	cmd = "cd  " + lines
	print(cmd, file= outfile2, end="\n")
	cmd3= 'if [ -e "acrossData.txt" ] \nthen\n rm "acrossData.txt" \n fi'
	print(cmd3, file= outfile2, end="\n")

	cmd2 = f(line) + "/cumulativeLocations.txt"
	cumulativeGroup=open(f(cmd2), "r")
	for loc in cumulativeGroup:
		cmd= "cd " + f(loc)
		print(cmd, file=outfile2, end="\n")
#Below is where you can change which line of the cumulative_output.txt file
#the script uses from each seed. Just change the number before p to get that
#Line value. for example, '15000p' will take the 15000th line from each seed's
#cumulative_output.txt file and append it to the acrossData.txt file.
		cmd= "sed -n '15000p'"+" cumulative_output.txt >> ../acrossData.txt"
		print(cmd, file=outfile2, end="\n")
		cmd= "cd .."
		print(cmd, file=outfile2, end="\n")
outfile2.close()		
across_locations2.close()		

print("running 'hamming_across_script2'")
os.system('./hamming_across_script2')


#Jumps into each directory and run hamming_graph.py on each acrossData.txt file

across_locations3 = open("across_locations.txt", "r")
outfile3=open("hamming_across_script3", "w")
print("#!/bin/sh", file= outfile3)
for graph in across_locations3:
	cmd = "cd " + startDir
	print(cmd, file=outfile3, end="\n")
	cmd = "cd " + graph
	print(cmd, file=outfile3, end="")

	print('python3',startDir,end="",file= outfile3)
	print('hamming_code03.py acrossData.txt across_hamming_Cumulative.txt', file=outfile3)

outfile3.close()		
across_locations3.close()		

os.system('./hamming_across_script3')

