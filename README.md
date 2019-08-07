# Scripts

There are three scripts you can run: 

*'noopt.py', which runs only the Z3 solver without objective functions; 
*'optpairwise.py', which runs the Z3 solver with objective functions to minimize the pairwise distance between any 2 nodes
*'optrectangle.py', which runs the Z3 solver with objective functions to minimize the overall size of the entire graph

# Command Line

Each script can be run in the following manner:

'''<script> <source> <destination>'''

The source should be a '.png' file, and the destination will have a '.tex' extension; a '.pdf' file will also be generated.

# Editing Parameters

There are some ways to edit the specific parameters of how these scripts will run:

*In 'circle.py', uncomment the print line (42) to output the circle detection results for debug purposes.
*In 'circle.py', changing the threshold variable will change how lax the script is on what a circle is. A higher threshold is more strict.
