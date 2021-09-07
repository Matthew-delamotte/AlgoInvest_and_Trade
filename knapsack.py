# # A naive recursive implementation of 0-1 Knapsack Problem

# # Returns the maximum value that can be put in a knapsack of
# # capacity W
# def knapSack(W, wt, val, n):

#     # Base Case
#     if n == 0 or W == 0:
#         return 0

#     # If weight of the nth item is more than Knapsack of capacity
#     # W, then this item cannot be included in the optimal solution
#     if (wt[n-1] > W):
#         return knapSack(W, wt, val, n-1)

#     # return the maximum of two cases:
#     # (1) nth item included
#     # (2) not included
#     else:
#         return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
#                    knapSack(W, wt, val, n-1))

# # end of function knapSack

# # To test above function

# wt = [20, 30, 50, 70, 60, 80, 22, 26, 48, 34,
#        42, 110, 38, 14, 18, 8, 4, 10, 24, 114]
# val = [5, 10, 12, 20, 17, 25, 7, 11, 13, 27, 17, 9, 23, 1, 3, 8, 12, 14, 21, 18]
# W = 500
# n = len(val)
# print(knapSack(W, wt, val, n))

# This code is contributed by Nikhil Kumar Singh

from ortools.algorithms import pywrapknapsack_solver


def main():
    # Create the solver.
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')

    values = [5, 10, 12, 20, 17, 25, 7, 11, 13, 27, 17, 9, 23, 1, 3, 8, 12, 14, 21, 18]
    weights = [20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 110, 38, 14, 18, 8, 4, 10, 24, 114]
    capacities = [500]

    solver.Init(values, weights, capacities)
    computed_value = solver.Solve()

    packed_items = []
    packed_weights = []
    total_weight = 0
    print('Total value =', computed_value)
    for i in range(len(values)):
        if solver.BestSolutionContains(i):
            packed_items.append(i)
            packed_weights.append(weights[0][i])
            total_weight += weights[0][i]
    print('Total weight:', total_weight)
    print('Packed items:', packed_items)
    print('Packed_weights:', packed_weights)


if __name__ == '__main__':
    main()