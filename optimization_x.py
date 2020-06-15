import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

"""
By: Dillon Graveline
"""

premium = 0.02
entries = 990
rake = 0.00
places_paid = 50
your_ranking = 0.6
learning_rate = 0.001

prize_pool = (premium - rake) * entries

payoff = []
z = 0.3 * prize_pool

for i in range(entries):
    payoff.append(z)
    z = z * 0.75

payoff[places_paid:] = [0 for i in range(len(payoff[places_paid:]))]

iterations = 10000

def simulation(your_ranking):
    distribution = np.random.normal(your_ranking * entries, entries * 0.3, iterations)
    distribution[distribution > entries] = entries
    distribution[distribution < 0] = 0
    profit = np.array([payoff[int(i-1)] - premium for i in distribution])
    mean = profit.mean()
    standard_deviation = profit.std()
    return mean, standard_deviation

print("====parameters====")
print(f"premium: {premium}")
print(f"entries: {entries}")
print(f"rake: {rake}")
print(f"places paid: {places_paid}")
print(f"your ranking: {your_ranking * 100}%")
print(f"learning rate: {learning_rate}")
print(f"iterations: {iterations}")
print("")
print("====statistics====")

mean, standard_deviation = simulation(your_ranking)
while mean < -0.00001 or mean > 0.00001:
    mean, standard_deviation = simulation(your_ranking)
    if mean > 0:
       your_ranking += learning_rate 
    elif mean < 0:
        your_ranking -= learning_rate
    print(f"mean: {mean}")
    print(f"X: {your_ranking}")
