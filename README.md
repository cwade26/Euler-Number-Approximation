# Euler-Number-Approximation

A Python project exploring numerical approximation of Euler's number e using a Monte Carlo simulation and normal distribution, with error analysis against the theoretical (expected) value and e.

Libraries: NumPy, Matplotlib

Results: as p -> 0 and N -> infinity, (1-p)**(1/p)-> 1/e

<img width="386" height="266" alt="e_convergence" src="https://github.com/user-attachments/assets/c09f6661-5750-4e78-ae0e-2fdb3a2b1833" />

# Method

Here, I used NumPy to produce random numbers from the normal distribution until the number was above the 1-p quantile.

I then calculate whether it took above or below the expected number of trials 1/p.

The probability that it took over the expected number of trials = (1-p)**(1/p) which is approximately 1/e, as p -> 0.

I then decided to repeat this trial N times, and counted each time it took over 1/p trials to produce a number in above the 1-p quantile.

As N -> infinity, the proportion of runs that took more than 1/p trials to find a number above the 1-p quantile approaches 1/e.

I then plotted this visually using matplotlib to compare the expected value with the real value over N number of times.

Finally, I calculated the percentage difference between the real value and the expected value as well as the 1/(real value) and e.
