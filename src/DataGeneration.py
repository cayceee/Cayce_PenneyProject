import random
import json
import os
from typing import List
from src.Helpers import debugger_factory


def INITIAL_DECKS(n = 26) -> List[bool]:
  """
  Creates the initial, unshuffled deck, with 0's and 1's representing black and red cards.
  The values of the cards are arbitrary with respect to the game.
  The deck is returned as 'initial_deck', a list.
  """

  initial_deck = [0]*n + [1]*n
  output_deck = ['B' if item == 0 else 'R' for item in initial_deck] # Switch 0s and 1s to Bs and Rs
  return output_deck


def SAVE_RANDOM_STATE() -> None:
  """
  Saves the system state to a json file of system states. 
  The json file is a list of system states.
  When function is called, the list of systems states is appended with the new state,
  the json file is then cleared and appened with the new state. 
  """
  
  state = random.getstate() 

  #if os.path.exists("data/random_seeds.json"): #checks if file exists before reading it. 
    #with open("data/random_seeds.json", "r") as f:
      #seeds = json.load(f)      
  #else:
  seeds = []  #if file does not exist, stores the seed as a list

  seeds.append(state)

  with open("data/random_seeds.json", "w") as f: #clears and rewrites the json file with the appended list of seeds.
      json.dump(seeds, f)



def LOAD_RANDOM_STATE(index) -> None:
  """
  Function is used to load a random state as the current system random state.
  Used for the reproducability of data already generated, if needed.
  """

  with open("data/random_seeds.json", "r") as file:
      seeds = json.load(file)

  state_serializable = seeds[index]
  state = (state_serializable[0], tuple(state_serializable[1]), state_serializable[2])
  random.setstate(state)



@debugger_factory()
def MAKE_DECKS(v = 1000000) -> List[List[bool]]:
    """
    Makes a v amount of decks, set to 100,000 by default.
    Presents 'decks' as a tuple of the deck lists.
    """

    decks = []
    for i in range(v):
      newDeck = INITIAL_DECKS()
      random.shuffle(newDeck)
      decks.append(newDeck)

    return decks

