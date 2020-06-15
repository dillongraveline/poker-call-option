import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

"""
By: Dillon Graveline
"""

premium = 0.25
entries = 90
rake = 0.02
places_paid = 13
your_ranking = 0.8

prize_pool = (premium - rake) * entries

payoff = []
z = 0.3 * prize_pool

for i in range(entries):
    payoff.append(z)
    z = z * 0.75

payoff[places_paid:] = [0 for i in range(len(payoff[places_paid:]))]

iterations = 10000

distribution = np.random.normal(0.1 * entries, entries * 0.3, iterations)

distribution[distribution > entries] = entries
distribution[distribution < 0] = 0

profit = np.array([payoff[int(i-1)] - premium for i in distribution])
cum_profit = []
temp_storage = 0
for i in range(len(profit)):
    temp_storage += profit[i]
    cum_profit.append(temp_storage)

mean = profit.mean()
standard_deviation = profit.std()

print("====parameters====")
print(f"premium: {premium}")
print(f"entries: {entries}")
print(f"rake: {rake}")
print(f"places paid: {places_paid}")
print(f"your ranking: {your_ranking * 100}%")
print(f"iterations: {iterations}")
print("")
print("====statistics====")
print(f"mean: {mean}")
print(f"standard deviation: {standard_deviation}")

tournaments = np.linspace(1, iterations, iterations)
plt.style.use('dark_background')
plt.plot(tournaments, cum_profit, color='red')
plt.xlabel('Tournaments')
plt.ylabel('Profit')
plt.show()
