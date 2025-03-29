import random
from typing import Tuple
from collections import defaultdict



SEQUENCE_LIST = ['BBB', 'BBR', 'BRB', 'BRR', 'RBB', 'RBR', 'RRB', 'RRR']
results = defaultdict(lambda: defaultdict(lambda: {'wins': 0, 'losses': 0, 'ties': 0}))

def CHOOSE_SEQ(seqList) -> str:
    """
    Selects a random entry in the sequence list to be used as a player's choice. 
    """
    return random.choice(seqList)



def record_result(player1: str, player2: str, player1_SCORE: int, player2_SCORE: int):
    """
    records the result of a whole game, notably not an individual trick. 
    """
    if player1_SCORE > player2_SCORE:
        result = "win"
    elif player1_SCORE < player2_SCORE:
        result = "loss"
    elif player1_SCORE == player2_SCORE:
        result = "tie"

    if result == 'win':
        results[player1][player2]['wins'] += 1
        results[player2][player1]['losses'] += 1
    elif result == 'loss':
        results[player1][player2]['losses'] += 1
        results[player2][player1]['wins'] += 1
    elif result == 'tie':
        results[player1][player2]['ties'] += 1
        results[player2][player1]['ties'] += 1



def calculate_win_percentage(player1: str, player2: str) -> float:
    """
    calculates the win percentage of two players. Used to compare sequence scores. 
    """
    total_matches = results[player1][player2]['wins'] + results[player1][player2]['losses'] + results[player1][player2]['ties']
    if total_matches == 0:
        return 0 
    
    return (results[player1][player2]['wins'] / total_matches) * 100



def dealOne(deck) -> str:
  """
  Given a deck, this function removes the first card from the deck and returns it.
  """
  card = deck[0]
  deck.remove(deck[0])

  return card



def play(player1, player2, deck) -> Tuple[int, int]:
  """
  Plays through one deck of Penney's Game
  Score is kept from number of stacks of cards won, not number of cards won.
  """
  dealtCards = []
  player1_temp = list(player1)
  player2_temp = list(player2)
  player1_score = 0
  player2_score = 0


  while len(deck) > 0:
    dealtCards.append(dealOne(deck))
    if len(dealtCards) >= 3:
      checkCards = dealtCards[len(dealtCards) -3 : len(dealtCards)]
      if checkCards == player1_temp:
        player1_score = player1_score + 1
        dealtCards = []
      elif checkCards == player2_temp:
        player2_score = player2_score + 1
        dealtCards = []

  return player1_score, player2_score



def simulate(decks, seqs = SEQUENCE_LIST):
  """
  Plays the game, resetting with each deck.
  Wins refer to the amount of decks that player won.
  """

  for deck in decks:
    player1 = CHOOSE_SEQ(seqs)
    player2 = CHOOSE_SEQ(seqs)
    player1_score, player2_score = play(player1, player2, deck)
    record_result(player1, player2, player1_score, player2_score)



