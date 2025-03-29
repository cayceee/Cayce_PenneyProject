# PenneyProject

The code's primary goal is to run a monte carlo style simulation of Penney's Game with a deck of cards. Penney's game is a card game that involves a trick that drastically increases the chances of the second player winning, if the player knows the trick. This code simulates the ratio in which each player wins, given player 2 knows the trick. 

An objective of this code is an ability to store the series of random decks created for reproducibility. In this code, this is done by storing the system state as a tuple, as produced by the function random.getstate(). The code is therefore split into two different files, "Data Generation and Storage" creates a random series of decks as a tuple, and produces the system state that made these decks as a tuple. The system state is stored on the local directory as a txt file, to be copied and pasted into the "Running the Simulation File," which then runs the simulation given a tuple of decks and produces the results and a visualization. 

**Data Generation and Storage:**
The first code file is used to create a random tuple of shuffled decks and saves the state that made these decks as a tuple, saving it as a txt file. To do this, the code first clears the system state, and then sets a "random one." This code is to be run if you desire to run the simulation with a completely new and random set of decks. This code does not do any simulation itself. 

**Running the Simulation:**
Once you have a tuple of the system state, either through running "Data Generation and Storage" or through trying to reproduce the results of a previous simulation run, the system state tuple from the txt file is to be copied and pasted into the "Running the Simulation Code" at the "newState" variable. This sets the system state to the state you want it to run in, then runs the simulation and produces the results and visualization. 

