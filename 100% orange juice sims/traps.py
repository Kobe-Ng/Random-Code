"""
This code tests the probability that you will
land on a placed trap given a certain starting
distance from the trap.

The probability increases from 16% to 36% from
distances 1-6, and then average out to about 28%
from far away.
"""

import numpy as np
from matplotlib import pyplot as plt
from functools import reduce

distances = 16
trap_proced = np.array([0] * distances)
trials = 50000

for initial_distance in range(1, distances):
    for _ in range(0, trials):
        distance_from_trap = initial_distance
        while distance_from_trap > 0:
            distance_from_trap -= np.random.randint(1, 7)
            if distance_from_trap == 0:
                trap_proced[initial_distance] += 1

probability_trap_procced = list(map(lambda x: x * 100.0 / trials, trap_proced))

print(probability_trap_procced)
print("the average is:", reduce(lambda a, b: a + b,
             probability_trap_procced) / len(probability_trap_procced))

plt.ylim(0, 100)
plt.scatter(list(range(0, distances)), probability_trap_procced)
plt.xlabel('initial distance from trap')
plt.ylabel('probability trap was procced while passing over')
plt.show()
