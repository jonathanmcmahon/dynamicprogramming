"""Dynamic programming solution to the Maximum Contiguous Subsequence problem.

This is a solution to Problem 6.1 in Algorithms by Dasgupta, Papadimitriou, and Vazirani (DPV).
Given a list S, we want to find the contiguous subsequence of S with maximum sum.

Example:
S = 9, -10, 31, 5, -20, 19
Maximum contiguous subsequence = 31, 5
"""
import numpy as np


def max_contiguous_subsequence(sequence):
    """Return the maximum sum contiguous subsequence.

    :param sequence: sequence to consider
    :return: list containing maximum sum contiguous subsequence of sequence
    """
    table = np.zeros((len(sequence)), dtype=int)
    max_contig_subseq = []
    for idx, value in enumerate(sequence):
        if idx == 0:
            table[idx] = value
        else:
            table[idx] = max([table[idx-1] + value, value])

    # Get the index of input sequence where the maximum sum subsequence ends
    max_seq_end_idx = np.argmax(table)

    # Build list of the maximum sum subsequence
    s = 0
    idx = max_seq_end_idx
    max_sum = table[max_seq_end_idx]
    while s != max_sum:
        max_contig_subseq.append(sequence[idx])
        s += sequence[idx]
        idx -= 1
    return max_contig_subseq[::-1]


def test_max_contiguous_subsequence(tests):
    """Test a series of sequences.

    :param tests: a list of dicts, each dict its own test and each containing a "sequence" and "answer"
    :return: None
    """
    for test in tests:
        seq = test["sequence"]
        ans = test["answer"]
        m = max_contiguous_subsequence(seq)
        assert m == ans, "Subsequence %s fails to match expected subsequence." % m
        print(m)


test_suite = [
    {"sequence": [5, 15, -30, 10, -5, 40, 10, -500, 50, -10, 10], "answer": [10, -5, 40, 10]},
    {"sequence": [5, 15, -30], "answer": [5, 15]},
    {"sequence": [-30, 5, 15, -30], "answer": [5, 15]},
    {"sequence": [-30, 5, 15, -30, 500], "answer": [500]},
    {"sequence": [-30, 20, 15, -30, 500], "answer": [20, 15, -30, 500]}
]

test_max_contiguous_subsequence(test_suite)
