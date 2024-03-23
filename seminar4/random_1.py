import matplotlib.pyplot as plt
import numpy as np

rg = np.random.default_rng(42)

a = rg.random((1, 10))

print(a)


# rng = np.random.default_rng(42) 

# N_points = 1000
# n_bins = 20


# dist1 = rng.standard_normal(N_points)
# dist2 = rng.uniform(-5,5, N_points)

# fig, axs = plt.subplots(1, 2, sharey=True)


# axs[0].hist(dist1, bins=n_bins)
# axs[1].hist(dist2, bins=n_bins)
# axs[0].grid()
# axs[1].grid()
# plt.show()