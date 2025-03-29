import random
import numpy as np
from collections import defaultdict
from src.DataGeneration import MAKE_DECKS, SAVE_RANDOM_STATE, LOAD_RANDOM_STATE
from src.Processing import simulate, simulateByCards, calculate_win_percentage
from src.Visualization import make_heatmap, make_heatmap_by_cards



random.seed(None)
seed = 42
random.seed(seed)
SAVE_RANDOM_STATE()

#LOAD_RANDOM_STATE() #Uncomment and insert an index from random_seeds to reproduce data

SEQUENCE_LIST = ['BBB', 'BBR', 'BRB', 'BRR', 'RBB', 'RBR', 'RRB', 'RRR']

decks = MAKE_DECKS()
print(decks[0])
print(decks[999])




### SIMULATE BY SCORING BY TRICKS ###


results = defaultdict(lambda: defaultdict(lambda: {'wins': 0, 'losses': 0, 'ties': 0}))
win_percentage_matrix = np.zeros((len(SEQUENCE_LIST), len(SEQUENCE_LIST)))

results = defaultdict(lambda: defaultdict(lambda: {'wins': 0, 'losses': 0, 'ties': 0}))
win_percentage_matrix = np.zeros((len(SEQUENCE_LIST), len(SEQUENCE_LIST)))

simulate(decks)

for i, seq_1 in enumerate(SEQUENCE_LIST):
    for j, seq_2 in enumerate(SEQUENCE_LIST):
        win_percentage_matrix[i][j] = calculate_win_percentage(seq_1, seq_2)


make_heatmap(win_percentage_matrix, SEQUENCE_LIST)




### SIMULATE BY SCORING BY CARDS ###


results = defaultdict(lambda: defaultdict(lambda: {'wins': 0, 'losses': 0, 'ties': 0}))
win_percentage_matrix = np.zeros((len(SEQUENCE_LIST), len(SEQUENCE_LIST)))

simulateByCards(decks)

for i, seq_1 in enumerate(SEQUENCE_LIST):
    for j, seq_2 in enumerate(SEQUENCE_LIST):
        win_percentage_matrix[i][j] = calculate_win_percentage(seq_1, seq_2)


make_heatmap_by_cards(win_percentage_matrix, SEQUENCE_LIST)