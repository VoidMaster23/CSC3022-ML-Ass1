# CSC 3022F: Machine Learning Assignment 1: Clustering
## Edson Shivuri (SHVNKA005)

This repository contains the code for an implementation of K-means clustering using python. 

# Files Submitted
- requirements.txt: contains a list of packages that need to be included in the virtual environment 
- Makefile: automates the generation of a venv for the program to run
- kMeans_shvnka005.py: contains all the logic for the algorithm implementation, including the generation of an output file ("output.txt")

# Additional Libraries Used And How
- Numpy: used mainly for the distance calculation , but also used 
- Pandas: used to store and represent data in dataframes. The built-in grouping capabilites from pandas was used to generate clusers and determine the mean values for subsequent iterations

# Output Format

\<input data in dataframe form\>

____________INITIAL STEP ____________________

ITERATION 0

\<data pertaining to that iteration , including previos nearest clusters, the current nearest, the centroid values and the cluster groupings as dataframes\>

____________Further Iterations ____________________

\<iteration number \>

\<data pertaining to that iteration , including previos nearest clusters, the current nearest, the centroid values and the cluster groupings as dataframes\>



Total Iteration Count: \<iteration count\>


***Please Note that the iteration count is inclusive of the first step***

# How to Run The Code
enter the command :  `make run` 

It should clear previous outputs, generate a venv for the program to run and then execute (please note that this may take some time)

Alternatively, you can use any combinations of the following commands to depending on what you need to do:

`make env` : create the venv

`make requirements`: activate the venv and install neccessary packages


`make clean`:
	removes venv file and the output.txt

`make test`: run the python script

