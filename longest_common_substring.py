"""Dynamic programming solution to Longest Common Substring problem.

This is a solution to Problem 6.8 in Algorithms by Dasgupta, Papadimitriou, and Vazirani (DPV).
Given two strings, we wish to find the length of their longest common substring.
"""
import numpy as np


def longest_common_substring(string1, string2):
    """Return the length of the longest common substring of two strings.

    :param string1: first string to compare
    :param string2: second string to compare
    :return: length of longest common substring
    """
    n = len(string1)
    m = len(string2)

    # We need an n x m table. (Also, our algorithm will run in O(nm) time.)
    table = np.zeros((n, m))

    # Each table entry (for example, table[i,j]) represents the length of the longest common suffix
    # (LCSuf) for string1[0,i] and string2[0,j]. So, for example, "MMA" and "MMAM" have a LCSuf of 0,
    # but "MMA" and "GAMMA" have an LCSuf of 3.

    for i in range(n):
        for j in range(m):
            if X[i] == Y[j]:
                # Substrings of length 1
                if i == 0 or j == 0:
                    table[i][j] = 1
                # Bigger substrings
                else:
                    table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = 0

    print("Table: \n" + str(table))
    return np.max(table)


# Our two strings to compare
X = "GAMMAMUOMICRON"
Y = "BETAGAMMAPHI"

print("First string:\t%s" % X)
print("Second string:\t%s" % Y)
print("Length of longest common substring: %d" % longest_common_substring(X, Y))
