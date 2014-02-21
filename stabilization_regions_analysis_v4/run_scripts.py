#Last edit 12/3/2012 5:00 pm
import os

os.system('rm file_locations.txt')
os.system('find . -name "notchNucCounts.txt" -printf "%h\n"|sort -u  >> "file_locations.txt"')

startDir = "~/Documents/Excel/test_data/"


file_locations = open("file_locations.txt", "r")
outfile=open("run_script", "w")

print("#!/bin/sh", file= outfile)

for line in file_locations:
    print("cd",line, end="", file= outfile)
    print('echo ///////////////////////////////////////////', file=outfile)
    print('echo',line, file= outfile)
    print('echo ///////////////////////////////////////////', file=outfile)
    print('python3',startDir,end="", file= outfile)
    print('decimal_discrete_convert01.py notchNucCounts.txt discrete_log.txt', file=outfile)
    print('python3',startDir,end="", file= outfile)
    print('hamming_code04.py discrete_log.txt hamming_output.txt cumulative_output.txt', file=outfile)
    
    print('python3',startDir,end="", file= outfile)
    print('hamming_graph.py hamming_output.txt graph_data.csv', file=outfile)
    print('Rscript',startDir,end="", file=outfile)
    print('StabilizationOverTime.r',file=outfile)
    
    
    print("cd",startDir,file= outfile)
    

print('python3 hamming_across.py',end="",file=outfile)
outfile.close()


os.system('chmod +x run_script')
os.system('./run_script')
