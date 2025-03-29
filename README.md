# PenneyProject

The code's primary goal is to run a monte carlo style simulation of Penney's Game with a deck of cards. Penney's game is a coin game where each player picks a sequence of three values, either heads or tails. The players then flip the coin until the last three flips makeup one of the player's sequences, with that player getting a point. The simulation runs a version of this game with cards, and used black and red instead of heads and tails. The game involves a trick that drastically increases the chances of the second player winning, if the player knows the trick.

An objective of this code is an ability to store the series of random decks created for reproducibility. In this code, this is done by storing the system state as a tuple that is stored to a json for each running of the code. 

## DataGeneration.py

The first code file is used to create the decks and saves the state that made these decks as a tuple, saving it as a json file. To do this, the code first clears the system state, and then sets a given state before storing the data. This code is to be run if you desire to run the simulation with a completely new and random set of decks. This code does not do any processing itself. 

## Processing.py

Takes a generated series of decks to repeatedly play through the game and saves the results. Each possible combination of sequences is tested and the results, most notable the win percentages are stored. 

## Visualization.py

Provides a heatmap of the results collected from processing file. Two Heatmaps are created, one where the game is scored by the amount of tricks won, and another where the game is score by your total amount of cards won. 

## main.py

Runs the code. Produces results for both versions of scoring. 
