Stabilization Regions Analysis Scripts
July 2012

To run the scripts:
-Make sure run_scripts.py, decimal_discrete_convert01.py, and hamming_code04.py
are all in the top of the directory structure you want to run the scripts on. 
-Edit the startDir variable (in run_scripts.py) is edited to be this directory.
-Check to make sure you do not need the previous file_locations.txt file
(If there is one).
-Run the command "python3 run_scripts.py".

================================================================================
-------------------------- decimal_discrete_convert.py -------------------------
================================================================================

This is the first and possibly the most basic of the scripts. It imports the
data file and converts all the numbers to a discrete log value. 

Functions
----------
-readinfo(infile) reads the data file and strips it,putting all the information
into a usable list. Its only parameter is the in file (variable for the data
file being read).

-converttoDiscrete() - takes the new list of all the data and converts each of 
the data points to a discrete logarithmic value.It does this using the equation:

			logvalue = log10((value)+.1))+1
	
This value is calculated as an int, so any extraneous decimal places are
truncated,ensuring the log value is discrete. If the calculated value is greater
than 4, it just converts it to 4(this particular data can ignore changes above
that threshold, as they are not what we are looking for). The only parameter is 
the mainData list (although not actually needed).

-printToFile reads the list with the newly converted values and systematically
prints them to an outfile. Unlike the incoming data, the output data will not
have tabs between each value. This is so changes can be more easily seen by the
eye when scrolling through the output file. Additionally, since all the values 
are restricted to be between 0 and 4, all the values remain aligned. 

-execution code
The execution code first defines the in/out filenames by reading the
command line arguments (sys.argv[1]= infilename, sys.argv[2] = outfilename).It
then opens both the in and out files based on their names. 
-Lastly, the three functions are run.

Using the script as a standalone
--------------------------------
*decimal_discrete_convert.py as a standalone script is best done from
the command line, since the script requires command-line arguments. Please note,
the script also requires python3 and will not work correctly with python2.

Arguments-
-using python3, call the script file, then add the arguments in order
-the input data file name/path
-the name/path for the output file.
 
 *Remember to include ".txt" to the end of file names.

example: 
python3 decimal_discrete_convert.py INDATAFILE OUTPUTFILE


================================================================================
------------------------------- hamming_code04.py ------------------------------
================================================================================

This is the 4th hamming code script and does the job of both hamming_code02.py
and hamming_code03.py. This script takes the discrete log output from
decimal_discrete_convert.py and runs through the discrete log values line by
line and compares where the changes are between lines (from the bottom up).
When the discrete log value changes for a cell from one line to another, a* is
placed. If there is no change between the two lines for that cell, a 0 is
recorded. It outputs this file to show where all the changes are taking place
throughout the run. The script uses that list in order to calculate the
cumulative change throughout the data (backwards). This produces an output file
that start with an * for every cell that changed its discrete log value anytime
during the run. As the file scrolls down, cells start to display a 0 when they 
stopped changing during the run. This allows a trickle-down effect where there 
are a few strands of cells that still display "*", marking them as cells that 
are still undecided.

Functions
----------
readinfo(infile)- reads the data file and strips it,putting all the information
into a usable list. Its only parameter is the in file (variable for the data
file being read).

hamming(infile, infileDataList)- goes through the new data list backwards and 
compares cells of each line. If the cell's current discrete log value is the 
same as in the previous line, a 0 is placed for that comparison. If the two
values are different, an "*" is placed. This is run through all the lines. At 
the end, the first line of the list is removed (because all of the new lines are
comparisons of two lines, the resulting file will have one less line. The first
line does not change, and therefore is removed).

cumulate(dataList)- This function uses the datalist exported by the previous 
function. Creates an output that is the cumulative changes occurring for each
cell. This is what creates the data list for the trickle-down file. It looks
to see if the previous line has changed yet, and if it does to have it always
place a * from now on (as it ascends the data).

printToFile(data, outfile)- The parameters are the datafile to be printed and
the outfile the data will be printed to. This function systematically prints
the new datalists to files.

Execution Code
--------------
The execution code first gets the infile name (sys.argv[1]), the
hammingOutfilename (sys.argv[2]), and the cumulativeOutfilename (sys.argv[3]),
and then opens all the files based on their names. The functions are then called
to create the data lists, and lastly the datalists are printed to files using
the printToFile() function.

Using the script as a standalone
--------------------------------
*running hamming_code04.py as a standalone script is best done from
the command line, since the script requires command-line arguments. Please note,
the script also requires python3 and will not work correctly with python2.

Arguments-
-using python3, call the script file, then add the arguments in order
-the input data file name/path
-the name/path for the hamming difference output file (what is generated during
hamming() )
-the name/path for the cumulative output file (what is generated during
 cumulate() )
 
 *Remember to include ".txt" to the end of file names.

example: 
python3 hamming_output4.py INDATAFILE HAMMINGOUTFILE CUMULATIVEOUTFILE

================================================================================
-------------------------------- hamming_across.py -----------------------------
================================================================================

This script searches all the sub directories looking for the produced 
cumulative_output.txt files (generated from the hamming_code04.py script
mentioned above). The script then generates shell scripts to search through all
the seed directories for each parameter setup to produce a cumulative hamming 
code across all the seeds. This allows the user to see what cells are still
unstable across all the seeds at the specified time stamp.

Produced Shell Scripts
----------------------
This script produces 3 shell scripts, which then do the work.

hamming_across_script - goes into each parameter setting directory (where the
seed folders are all located) and creates a "cumulativeLocations.txt" that 
contains the location directories of where all the "cumulative_output.txt" files
are. These files are used to direct further scripts.

hamming_across_script2 - goes into each parameter directory, and then in each
locations in the "cumulativeLocations.txt" file, takes the specified line from
the "cumulative_output.txt" of each seed file, and appends it to the
acrossData.txt that is contained in the parameter directory.

hamming_across_script3 - goes to each acrossData.txt file produced in the 
hamming_across_script2 and runs hamming_code03.py to run a cumulative hamming
code on the lines of the acrossData.txt. It saves this as across_hamming_Cumulative.txt

Execution
---------
It is set up to just run at the end of all the other scripts when the
run_scripts.py file is run. The user does not have to do anything to get this to
run in run_scripts.py. 

However, there are specific ways to customize how the script runs. 
If you want to change what line is read from the cumulative_output.txt file of
each seed (ex: line 15,000 or 20,000), you have to change a number in the code.

Line 54 (as of 12/13/2012) of hamming_across.py has to be changed as follows.

#Below is where you can change which line of the cumulative_output.txt file
#the script uses from each seed. Just change the number before p to get that
#Line value. for example, '15000p' will take the 15000th line from each seed's
#cumulative_output.txt file and append it to the acrossData.txt file.

cmd= "sed -n '15000p'"+" cumulative_output.txt >> ../acrossData.txt"

Other than than, the only real thing that might need to be changed is the file
names, which should be easy enough to see in the script. I might change them so
this is easier to do at some point if it is needed.

Using the script as a standalone
--------------------------------
This script works well as a stand alone. In fact, all run_scripts.py does with
this script is execute it at the end. To run it as a stand alone, the user just
has to place it in the top of the directory they want to use it on and execute
it. If the file/folder names that are being searched are different than the
defaults, they might need to be changed, but the user only has to change them
in the hamming_across.py script, since that script makes all the shell scripts.

If the file names are correct and the specified line is set to the users
preference, just run it in the top of the directory using python.

ex: "python3 hamming_across.py"

================================================================================
--------------------------------- run_scripts.py -------------------------------
================================================================================

This script finds all of the data files to be analyzed, then makes and runs a
script that starts the other scripts for all the files found.

Execution Code
--------------
This script doesn't have defined functions, but rather a list of execution code.

First, the script removes the file_locations.txt file from the current
directory. This is so that it will only read the data files it finds during
this execution of the script, otherwise it would append the new list to an old
one (if it exists). *Make sure it is okay to delete file_locations.txt before
running this script*.

Next, the script finds all the data files with a certain name, (by default,
"notchNucCounts.txt") and adds their directories to a new file_locations.txt
file.

The file_locations.txt and an output script are then opened. For each file
location, commands to enter the directory, run decimal_discrete_convert01.py and
hamming_code04.py on the datafile, then jump back out are added to the output
script file. After commands for all of the locations are written, the file is
closed, given executable permission, and then executed.

At the end, hamming_across.py is run on the data.

To use run_scripts.py
---------------------
-Make sure run_scripts.py, decimal_discrete_convert01.py, and hamming_code04.py
are all in the top of the directory structure you want to run the scripts on. 
-The startDir variable is edited to be this directory.
-Check to make sure you do not need th previous file_locations.txt file.
-Run the command "python3 run_scripts.py".



||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\  Other Scripts  ///////////////////////////////
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

These files aren't really part of the current analysis scripts, but were initial
steps in making the current ones. They might be still be useful for something.
The individual functions won't be explained for these since they are very
similar to the current scripts. What they do and how to run them will be
explained in case they can be used for something.

================================================================================
-------------------------------- hamming_code.py -------------------------------
================================================================================

This script takes in two discrete log data files (from
decimal_discrete_convert01.py) and find the line by line hamming distance
between the two. It give an output file that shows the differences in the
changes of the discrete log data files.

To run the script, it is better use the command line since the script requires
command line arguments. Two discrete log data file have to be input, and the
name for the output file must also be given.
Example:
	python3 hamming_code.py DATAFILENAME1 DATAFILENAME2 OUTPUTFILENAME
*remember to include ".txt" to the file names.

================================================================================
------------------------------- hamming_code02.py ------------------------------
================================================================================

This takes in a discrete log data file (from decimal_discrete_convert01.py) and
runs a hamming code on it line by line from bottom to top. For example, the
first step is it compares the last line to the second last line. For a different
value, it writes a "*" and for the same value of the cell from line to line, it
writes a 0 to the output file. It does this all the way up the script and then
prints out the result. This is the first part that is run during
hamming_code04.py (The hamming_output.txt).
To run the script, it is better use the command line since the script requires
command line arguments. Two discrete log data file have to be input, and the
name for the output file must also be given.
Example:
	python3 hamming_code02.py DATAFILENAME OUTPUTFILENAME
*remember to include ".txt" to the file names.

================================================================================
------------------------------- hamming_code03.py ------------------------------
================================================================================

This takes in a discrete log data file (from decimal_discrete_convert01.py) and
runs a cumulative hamming code on it line by line from bottom to top.This is
just like the last code, except once a difference has been spotted for a cell,
it continues to print a "*" as the script ascends the file. This is the second
part of the hamming_code04.py script (what produces the cumulative_output.txt).

To run the script, it is better use the command line since the script requires
command line arguments. One discrete log data file has to be input, and the
name for the output file must also be given.
Example:
	python3 hamming_code03.py DATAFILENAME OUTPUTFILENAME
*remember to include ".txt" to the file names.

