# Scripts

There are three scripts you can run: 

1. `noopt.py`, which runs only the Z3 solver without objective functions; 
2. `optpairwise.py`, which runs the Z3 solver with objective functions to minimize the pairwise distance between any 2 nodes;
3. `optrectangle.py`, which runs the Z3 solver with objective functions to minimize the overall size of the entire graph

# Command Line

Each script can be run in the following manner:

```<script> <source> <destination>```

The source should be a `.png` file, and the destination will have a `.tex` extension; a `.pdf` file will also be generated.

# Editing Parameters

There are some ways to edit the specific parameters of how these scripts will run:

1. In `circle.py`, uncomment the print line (42) to output the circle detection results for debug purposes.
2. In `circle.py`, changing the threshold variable will change how lax the script is on what a circle is. A higher threshold is more strict.
