import sys
import random
import numpy as np
from argparse import ArgumentParser
from datetime import datetime



#FUNCTION DEFINITIONS
#---------------------------------------------------------------------#

def get_parser():
    parser = ArgumentParser(description='Simulate Schellings Model of Segregation', prog='schellings_test')
    parser.add_argument('-dg',  '--data_grid', default="data/schelling.txt", help="path to the file containing the data grid")
    parser.add_argument('-dsr', '--data_subregion', help='path to the file containing the data grid')
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
def compute_index_of_dissimilarity(grid, subregion_grid):
    population_count_x = np.count_nonzero(grid == 'X')
    population_count_o = np.count_nonzero(grid == 'O')
    sample_count_x = np.count_nonzero(subregion_grid == 'X')
    sample_count_o = np.count_nonzero(subregion_grid == 'O')

    index_of_dissimilarity = 0.5*abs((sample_count_x/population_count_x) - (sample_count_o/population_count_o))
    return round(index_of_dissimilarity, 6)

#---------------------------------------------------------------------#

def process_start():
    parser = get_parser()
    args   = parser.parse_args()

    #commandline parameters
    data_grid      = args.data_grid
    data_subregion = args.data_subregion

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
    print("\n\nSTART: Computing Index of Dissimilarity")
    subregion_grid = load_grid(data_subregion)
    print(f"Subregion size: " + str(subregion_grid.shape[0]) + " x " + str(subregion_grid.shape[1]))
    print("\nSubregion:")
    print_model(subregion_grid)

    index_of_dissimilarity = compute_index_of_dissimilarity(grid, subregion_grid)
    print(f"\nIndex of Dissimilarity = " + str(index_of_dissimilarity) + " or " + str(round(index_of_dissimilarity, 2)))
    print("DONE: Computing Index of Dissimilarity.\n")

    #simulation
    print("\nSTART: Simulation of Schelling Segregation.\n")
    print("\nDONE: Simulation of Schelling Segregation.\n")

    print("\n\nEnd Time: " + str(datetime.now()))

#---------------------------------------------------------------------#

if __name__ == "__main__":
    process_start()

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