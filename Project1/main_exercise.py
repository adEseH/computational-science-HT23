import numpy as np
import random as rd


def Lennard_Jones(r, epsilon, sigma):
    return 4*epsilon*((sigma/r)**12-(sigma/r)**6)

def get_U(r, epsilon=10, sigma=1, T=1, k_B=1):
    r_length = r.shape[0]
    U = 0
    for n in range(r_length):
        r_diff = Lennard_Jones(np.linalg.norm(r-np.repeat([r[n,:]],r_length,axis=0),axis=1), epsilon, sigma)
        U += np.sum(r_diff[~np.isnan(r_diff)])
    return U/2

# r is a np vector of particle positions

def MC_step(r, epsilon=10, sigma=1, T=1, k_B=1):
    beta = 1/(k_B*T)
    # pick random entry of r
    r_length = r.shape[0]
    n = rd.randrange(r_length)
    r_new = np.random.rand(3)
    r_diff = Lennard_Jones(np.linalg.norm(r-np.repeat([r[n,:]],r_length,axis=0),axis=1), epsilon, sigma)
    r_diff_new = Lennard_Jones(np.linalg.norm(r-np.repeat([r_new],r_length,axis=0),axis=1), epsilon, sigma)
    r[n,:] = r_new
    delta_U = np.sum(r_diff_new[~np.isnan(r_diff_new)])-np.sum(r_diff[~np.isnan(r_diff)])
    xi = rd.random()
    if xi < np.exp(-beta*delta_U):
        # accept the move
        r[n,:] = r_new
    return r, delta_U


N = 2 # number of particles

# initialise system
r = np.random.rand(N,3)

for i in range(100):
    U = get_U(r)
    r, delta_U = MC_step(r)
    print(U)
