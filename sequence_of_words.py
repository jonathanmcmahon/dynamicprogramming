"""Dynamic programming solution to the Sequence of Words problem.

This is a solution to Problem 6.4 in Algorithms by Dasgupta, Papadimitriou, and Vazirani (DPV).
Given a string S, we want to know if it is composed of a valid sequence of words. We have a helper function
is_word that will tell us if a string is a valid single word.
"""
import numpy as np

dictionary = ["a", "an", "apple", "ate", "big", "eat", "olifaunt", "oversized", "rapacious"]


def is_word(s):
    """Indicate if a word is valid."""
    return s in dictionary


def sequence_of_words(s):
    """Determine if a string consists of a valid sequence of words.

    :param s: string
    :return: True if the string is a valid sequence of words; False otherwise
    """
    table = np.zeros((len(s), len(s)))
    for start_idx, starting_letter_set in enumerate(table):
        for end_idx, end_letter in enumerate(starting_letter_set):
            if end_idx >= start_idx:
                table[start_idx][end_idx] = is_word(s[start_idx:end_idx + 1])
                # This allows us to easily collapse the table down and ensure we have a valid sequence
                if table[start_idx][end_idx] == 1:
                    table[start_idx][start_idx:end_idx] = 1
    print(np.sum(table, axis=0))
    return np.all(np.sum(table, axis=0) == 1)


def run_test_suite(cases):
    """Test suite for sequence_of_words function.

    :param cases: a list of tuples of the form (string, boolean) indicating if the string is valid
    :return: None
    """
    for case in cases:
        string, validity = case
        assert sequence_of_words(string) == validity, "Test of %s failed." % string
    print("All %d test cases passed." % len(cases))


test_cases = [("anapple", True),
              ("arapaciousappleateanoversizedolifaunt", True),
              ("anappleelephantoversizedate", False),
              ("a", True),
              ("b", False),
              ("appleat", False)]

run_test_suite(test_cases)
