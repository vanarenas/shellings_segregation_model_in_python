import sys
import random
import numpy as np



#FUNCTION DEFINITIONS
#---------------------------------------------------------------------#

def load_grid(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            grid_data = [list(line.strip()) for line in lines]
        return np.array(grid_data)
    except FileNotFoundError:
        print(f"ERROR: File '{filename}' not found.")
        sys.exit(1)

#---------------------------------------------------------------------#

def print_model(grid):
    for row in grid:
        print(" ".join(row))

#---------------------------------------------------------------------#

def cpt_idx_dissimilarity(min, max):
    idx_rand   = random.uniform(min, max)
    return round(idx_rand, 6)

#---------------------------------------------------------------------#



#PROCESS START
data_grid = sys.argv[1]
data_subregion = sys.argv[2]

print("START: Loading data grid. ...")
grid = load_grid(data_grid)
print(" DONE: Loading data grid.\n")
print("Grid Dimensions:")
print(f"> Row count: {grid.shape[0]}")
print(f"> Column count: {grid.shape[1]}\n")


print("\nSTART: Printing data contents.\n")
print_model(grid)
print("\nDONE: Printing data contents.\n")

print("\nSTART: Computing Index of Dissimilarity.\n")
print("Subregion:")
subregion = load_grid(data_subregion)
print_model(subregion)

index_of_dissimilarity = cpt_idx_dissimilarity(0,1)
print("\nIndex of Dissimilarity = " + str(index_of_dissimilarity) + " or " + str(round(index_of_dissimilarity, 2)))
print("DONE: Computing Index of Dissimilarity.\n")

print("\nSTART: Simulation of Schelling Segregation.\n")
print("\nDONE: Simulation of Schelling Segregation.\n")

# START: Computing Index of Dissimilarity.

# (1) check if the subregion is within the data grid
# (2) if within the data grid then, print the subregion
# (3) if not within the data grid, then throw an error
# Subregion:
# X O X O
# O X O X
# O X O X
# X   X O


# (4) if subregion is not null, then compute for index of similarity
# Index of Dissimilarity = 0.020909 or 0.021
# DONE: Computing Index of Dissimilarity.

# (5) define other variables here check again the course from coursera

# (1) there are
# START: Simulation of Schelling Segregation.

# X   O O
# X           O
#   X X     O
#   X X X   O     X
#       X
# X       X X
# X X O         O   O
# X         O O   O O
# O       O O   O   O
# O O   O O O O

# DONE: Simulation of Schelling Segregation.