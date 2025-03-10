import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data\\data.csv")

nodes = df["Nodes"]
evaluation = df["Evaluation (centipawns)"]
best_move = df["PV First Move"]

size = 10**6
plt.hist(nodes, bins=range(min(nodes), max(nodes)+size, size))

plt.xlabel("Nodes")
plt.ylabel("Counts")
plt.title("Node Distribution")

plt.tight_layout()
plt.show()

size = 1
plt.hist(evaluation, bins=range(min(evaluation), max(evaluation)+size, size))

plt.xlabel("Evaluation (centipawns)")
plt.ylabel("Counts")
plt.title("Evaluation Distribution")

plt.tight_layout()
plt.show()

plt.scatter(nodes, evaluation)

plt.xlabel("Nodes")
plt.ylabel("Evaluation (centipawns)")
plt.title("Evaluation versus Nodes")

plt.tight_layout()
plt.show()

labels, counts = np.unique(best_move, return_counts=True)
plt.bar(labels, counts)
plt.yscale("log")
plt.xticks(rotation="vertical")

plt.xlabel("Move")
plt.ylabel("Counts")
plt.title("PV First Moves")

plt.tight_layout()
plt.show()

print(np.mean(evaluation))
print(np.std(evaluation))
