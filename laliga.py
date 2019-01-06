import numpy as np
import matplotlib.pyplot as plt

TOTAL_GAMES=42
POINTS_THRESHOLD=75
NUM_SIMULATIONS=1000

# run simlations
results = np.random.multinomial(
	TOTAL_GAMES, 
	[11/19,3/19,5/19],
	NUM_SIMULATIONS)

# calculate points
points = np.array([x[0]*3+x[1] for x in results])

# PMF
_ = plt.hist(points, normed=True, bins=25)
_ = plt.xlabel('Total points in season')
_ = plt.ylabel('Probability')
_ = plt.title('PMF')

plt.show()

# ECDF
_ = plt.hist(points, normed=True, cumulative=True, histtype='step', bins=100)
_ = plt.axvline(x=POINTS_THRESHOLD)
_ = plt.xlabel('Total points in season')
_ = plt.ylabel('Probability')
_ = plt.title('ECDF')

plt.show()

# Print out probability of more than threshold points
print('Probability of more than {} points is {}'.format(
        POINTS_THRESHOLD,
        sum(points>=POINTS_THRESHOLD)/NUM_SIMULATIONS)
)
