"""Dynamic programming solution to Minimum Cost String Breaking problem.

This is a solution to Problem 6.9 in Algorithms by Dasgupta, Papadimitriou, and Vazirani (DPV).
Given a string of length n and the position of m cuts, we want to find the minimum cost of breaking
the string in to m+1 pieces at the m cut positions.

The idea behind this problem is that the order in which we perform the cuts matters because a cut
involves copying the entire string of length y being cut and so will take time y.

Example:
string = "STRING"
breakpoints = 1, 3
substrings resulting from the cut: "S", "TR", "ING"
"""
import numpy as np


def min_cutting_cost(string, breakpoints):
    pass
