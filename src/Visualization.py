import seaborn as sns
import matplotlib.pyplot as plt


def make_heatmap(matrix, seqs):
    """
    Makes a heatmap for all combinations of different sequences. 
    """
    plt.figure(figsize=(10, 8))  
    sns.heatmap(matrix, annot=True, cmap='viridis', fmt=".1f", 
                xticklabels = seqs, yticklabels = seqs)

    plt.title("Penney's Game Win Percentages")
    plt.xlabel("Player 2 Sequence")
    plt.ylabel("Player 1 Sequence")
    plt.yticks(rotation = 0)

    plt.show()