## Uniform cost search

1. Name and CSM Campus ID of the student.

	Name: Deepak Rajasekhar Karishetti
	CSM Campus ID: 


2. What programming language is used.

	Python 3.


3. What OS is used to compile and run the codes.
	
	Ubuntu 16.04 LTS.


4. How the code is structured.
	
	-Initially with the start of the program, all the necessary modules are imported.
	-A graph dictionary is created using the data from the input text file.
	-Nodes are defined and are connected to each other in the graph.
	-Uninformed cost search algorithm is defined which uses PriorityQueue as a data structure for expanding and testing the nodes along the specified path.
	-Function to find the neighbouring nodes in the graph is defined.
	-Function to calculate the cost of each path is defined.
	-The function to display the route and the path cost from the start city to the destination city is defined.
	-Main function is defined to read all the input arguments, create graph from input text file, finding path and cost ucs and displaying the path is defined, as per the project description.
	-Finally, the main function is called to run the whole program to implement the search algorithm to find the route beteween two input cities.


5. How to run the code, including very specific compilation instructions, if compilation is needed. Instructions such as "compile using g++" are NOT considered specific.

	-Open the file location on Linux terminal (having both the find_route.py and the input text file).

	-The following command is run:

		>> python3 find_route.py <input_filename> <source_city_name> <destination_city_name>

