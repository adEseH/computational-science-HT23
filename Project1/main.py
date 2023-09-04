import numpy as np
import random as rd

# good programming practice in python
# - avoid loops (vectorise, use numpy, stencils)
# - avoid function calls


# Extensions:
# - magnetisation


class Irsing():
    # Carmen: class structure
    def __init__(self):
        # parameters
        self.N
        self.L
        self.T
        self.q
        self.J_p = 1
        self.s # initialise this somehow
        # s = [[1,2,1],[1,3,1],...] 2D-matrix os spin states, reading order
        self.E # list of energies


    def MC_step(self, s):
        # Anna
        T = self.T
        # steps 1-3 p.12

    def nearest_neighbours():
        # returns a stencil given a coordinate

    def run_simulation(self):
        # Anna
        # initialise
        
        for i in range():

    def get_E(self):
        # Carmen
        # calculate the energy

    def write_E():
        # Theo

    def plot_state(self):
        # Theo



def plot_energies(self):
    # Carmen
    # taking averages, etc.
    


if __name__ == '__main__':
    # main starts here
    # designing experiments: Anna, Theo, Carmen


