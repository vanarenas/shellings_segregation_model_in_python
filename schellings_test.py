import sys
import random
import numpy as np
from argparse import ArgumentParser
from datetime import datetime



#GLOBAL VARIABLES



#FUNCTION DEFINITIONS
#---------------------------------------------------------------------#

def get_parser():
    parser = ArgumentParser(description='Simulate Schellings Model of Segregation', prog='schellings_test')
    parser.add_argument('-dg',  '--data_grid', default="data/schelling.txt", help="path to the file containing the data grid")
    parser.add_argument('-dsr', '--data_subregion', help='size of the subregion used to compute the index of dissimilarity')
    parser.add_argument('-ssz', '--subregion_size', help='size of the subregion used to compute the index of dissimilarity')
    parser.add_argument('-st',  '--similarity_threshold', help='Who is giving the signoff?')
    parser.add_argument('-mi',  '--max_iterations', help='Team which is giving the signoff (TS or TC)')
    return parser

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
def compute_index_of_dissimilarity(grid, subregion_size):
    height, width = grid.shape
    dissimilar_count = 0

    for i in range(0, height, subregion_size):
        for j in range(0, width, subregion_size):
            subregion = grid[i:i + subregion_size, j:j + subregion_size]

            unique_elements = np.unique(subregion)
            if len(unique_elements) > 1:
                dissimilar_count += 1

    index_of_dissimilarity = dissimilar_count / (height * width)
    return round(index_of_dissimilarity, 6)

#---------------------------------------------------------------------#

def process_start():
    parser = get_parser()
    args   = parser.parse_args()

    #commandline parameters
    data_grid      = args.data_grid
    data_subregion = args.data_subregion
    subregion_size = int(args.subregion_size)

    print("PYTHON IMPLEMENTATION OF SCHELLING'S MODEL OF SEGREGATION")
    print("Start Time: " + str(datetime.now()))

    #data grip (population) loading
    print("\n\nSTART: Loading data grid. ...")
    grid = load_grid(data_grid)
    print(" DONE: Loading data grid.\n")
    print("Grid Dimensions:")
    print(f"> Row count: {grid.shape[0]}")
    print(f"> Column count: {grid.shape[1]}\n")
    print("Data Grid:")
    print_model(grid)

    #data subregion (sample) loading and index of dissimilarity calculation
    print("\n\nSTART: Computing Index of Dissimilarity v1")
    print("Subregion size: " + str(subregion_size) + " x " + str(subregion_size))
    idx_of_dissimilarity = compute_index_of_dissimilarity(grid, subregion_size)
    print("\nSubregion:")
    print_model(grid[:subregion_size, :subregion_size])
    print(f"\nIndex of Dissimilarity = " + str(idx_of_dissimilarity) + " or " + str(round(idx_of_dissimilarity, 2)))
    print("DONE: Computing Index of Dissimilarity.\n")

    #simulation
    print("\nSTART: Simulation of Schelling Segregation.\n")
    print("\nDONE: Simulation of Schelling Segregation.\n")

    print("\n\nEnd Time: " + str(datetime.now()))

#---------------------------------------------------------------------#

if __name__ == "__main__":
    process_start()

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
#   X X    O     X
#       X
# X       X X
# X X O         O   O
# X         O O   O O
# O       O O   O   O
# O O   O O O O

# DONE: Simulation of Schelling Segregation.