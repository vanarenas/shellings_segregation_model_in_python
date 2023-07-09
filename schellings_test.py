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
    parser.add_argument('-dsr', '--data_subregion', help='path to the file containing the subregion data grid')
    parser.add_argument('-st',  '--sim_threshold', type=float, help='desired similarity level with nearby neighbors')
    parser.add_argument('-mi',  '--max_iterations', type=int, help='maximum number of iterations to simulate the segregation')
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

def get_agents(grid):
    height, width = grid.shape
    agents = {}

    for h in range(height):
        for w in range(width):
            if grid[h][w] != ' ':
                agent_position = f"({h},{w})"
                agent_type = grid[h][w]
                agents[agent_position] = agent_type

    return agents

#---------------------------------------------------------------------#

def get_neighbors(grid, agents):
    height, width = grid.shape
    neighbors = {}

    for agent_position, agent_type in agents.items():
        row, column = map(int, agent_position.strip('()').split(','))

        for n_row in [-1, 0, 1]:
            for n_coloumn in [-1, 0, 1]:
                new_row    = row + n_row
                new_column = column + n_coloumn

                if (new_row, new_column) != (row, column) and (0 <= new_row < height and 0 <= new_column < width):
                    neighbor_position = f"({new_row},{new_column})"
                    neighbor_type     = grid[new_row][new_column]

                    if agent_position not in neighbors:
                        neighbors[agent_position] = []
                    neighbors[agent_position].append((neighbor_position, neighbor_type))

    return neighbors

#---------------------------------------------------------------------#

def compute_similarity(agents, neighbors):
    similarity   = {}

    for agent_position, agent_type in agents.items():
        num_similar = 0

        if agent_position in neighbors:
            for neighbor_position, neighbor_type in neighbors[agent_position]:
                if neighbor_type == agent_type:
                    num_similar += 1

        match = num_similar / len(neighbors[agent_position])
        similarity[agent_position] = round(match, 2)

    return similarity

#---------------------------------------------------------------------#

def compute_satisfaction(similarity, sim_threshold):
    satisfaction = {}

    for agent_position, match in similarity.items():
        is_satisfied = 1

        if match < sim_threshold:
            is_satisfied = 0

        satisfaction[agent_position] = is_satisfied

    return satisfaction

#---------------------------------------------------------------------#

def process_start():
    parser = get_parser()
    args   = parser.parse_args()

    #commandline parameters
    data_grid      = args.data_grid
    data_subregion = args.data_subregion
    sim_threshold  = round(args.sim_threshold, 2)
    max_iterations = args.max_iterations

    print("PYTHON IMPLEMENTATION OF SCHELLING'S MODEL OF SEGREGATION")
    print("Start Time: " + str(datetime.now()))

    #data grid (population) loading
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
    agents = get_agents(grid)
    neighbors = get_neighbors(grid, agents)
    similarity = compute_similarity(agents, neighbors)
    satisfaction = compute_satisfaction(similarity, sim_threshold)
    print(satisfaction)
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