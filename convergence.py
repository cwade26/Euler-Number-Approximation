import numpy as np
from statistics import NormalDist as ND
import matplotlib.pyplot as plt

mean, sd = 1, 1
p = 0.01
target = round(1/p)
threshold = ND(mean, sd).inv_cdf(1 - p)

def draws_until_hit():
    a = 0
    i = 0
    while a < threshold:
        a = np.random.normal(mean, sd)
        i += 1
    return i
    
N = 10000

results = np.array([draws_until_hit() for k in range (N)])

above = results > target

running_prop = np.cumsum(above) / np.arange(1, N + 1)
    
mean_i = np.mean(above)

theory = (1 - p)**target

plt.plot(running_prop)
plt.axhline(theory, color = "red", linestyle = "--", label = f"theory: {theory:.3f}")
plt.axhline(mean_i, color = "green", linestyle = ":", label = f"practice: {mean_i:.3f}")
plt.xlabel("number of trials")
plt.ylabel(f"proportion of trials needing >{target} draws")
plt.legend()
plt.show()

percentage_error_from_theory = (np.abs(np.mean(results) - (1/p))/(1/p))*100
percentage_error_from_e = (np.abs((1/mean_i) - (np.e))/(np.e))*100

print(f"percentage error from theory = {percentage_error_from_theory}")

#(1-(1/n))**n -> 1/e as n -> infinity so, 1/mean_i approximates e as N -> infinity and p -> 0

print(f"e ~ {1/mean_i}    true value = {np.e}")
print(f"percentage error from e = {percentage_error_from_e}")
