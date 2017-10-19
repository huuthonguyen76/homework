import numpy as np
import math


def get_np_ranks(np_arr):
	temp = np.argsort(np_arr)
	ranks = np.zeros(len(np_arr))
	ranks[temp] = np.arange(len(np_arr))
	return ranks

def spearman_correlation(np_X_ranks, np_Y_ranks):
	np_XY_ranks = np_X_ranks * np_Y_ranks
	total_X = np.sum(np_X_ranks)
	total_Y = np.sum(np_Y_ranks)
	n = len(np_X_ranks)
	total_X_exp = np.sum(np.power(np_X_ranks, 2))
	total_Y_exp = np.sum(np.power(np_Y_ranks, 2))

	numerator = sum(np_XY_ranks) - ((total_X * total_Y) / n)
	denominator = math.sqrt(total_X_exp - (math.pow(total_X, 2) / n)) * math.sqrt(total_Y_exp - (math.pow(total_Y, 2) / n))

	return numerator / denominator


X = np.array([73, 76, 78, 65, 86, 82, 91], np.float)
Y = np.array([77, 78, 79, 80, 86, 89, 95], np.float)

np_X_ranks = get_np_ranks(X) + 1
np_Y_ranks = get_np_ranks(Y) + 1

print(spearman_correlation(np_X_ranks, np_Y_ranks))