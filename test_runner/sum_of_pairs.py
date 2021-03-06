"""
Problem 1: Sum of pairs

Given an array of size n, find the unique pairs of elements whose sum will be equal to given value K.
An element can occur in only one pair. Print “None” if there is no pair whose sum is equal to K.
"""
from typing import List, Tuple


# Write your code inside this function.
# DO NOT modify the method signature
# DO NOT modify/remove any system generated code/comments

def DoWork(n, K, input):
    # n is the number of elements, an integer
    # K is the target sum, again an integer
    # input is the list of integers.
    # Expected return value is a list of two-tuples.

    # sum pairs for the given example [1, 2, 3, 4, 5, 6, 7] and sum 10:
    return [(3, 7), (4, 6)]


# DO NOT remove/modify the below line
# PLCHLDR_TSTCASES#
def remove_duplicate_pairs(pairs):
    # sort each of the 2-tuples to remove reversed pairs, which are duplicates
    return set(tuple(sorted(pair)) for pair in pairs)


def run_single_test_case(method, kwargs, actual_result, failure_message, success_message):
    # In cases of a 'None' result, empty lists are used instead for simplicity.
    # remove duplicates including reversed pairs from actual_result also
    actual_result = remove_duplicate_pairs(actual_result or [])
    try:
        result: 'List[Tuple[int, int]]' = method(**kwargs) or []
    except Exception as e:
        print(f"\t\t <fail>Exception raised during execution {type(e).__name__}: {e.__str__()}</fail>")
    else:
        # remove duplicates including reversed pairs
        result_set = remove_duplicate_pairs(result)
        if result_set != actual_result:
            print(f"\t\t <fail>{failure_message}</fail>")
        else:
            print(f"\t\t  <success>{success_message}</success>")


def run_test_case():
    for case in TEST_CASES:
        success_message = case.pop('success_message')
        failure_message = case.pop('failure_message')
        actual_result = case.pop('actual_result')
        run_single_test_case(DoWork, case, actual_result, failure_message, success_message)


TEST_CASES = ({
                  'n': 5,
                  'K': 10,
                  'input': [3, 1, 7, 9, 8],
                  'actual_result': {(1, 9), (3, 7)},
                  'success_message': 'Test succeeded.',
                  'failure_message': 'Failed to find all the pairs.'
              }, {
                  'n': 5,
                  'K': 10,
                  'input': [3, 4, 7, 3, 7],
                  'actual_result': {(3, 7)},
                  'success_message': 'Test succeeded.',
                  'failure_message': 'Failed to find all the pairs.'
              }, {
                  'n': 6,
                  'K': 10,
                  'input': [3, 4, 7, 5, 7, 23],
                  'actual_result': {(3, 7)},
                  'success_message': 'Test succeeded.',
                  'failure_message': 'Failed to find all the pairs.'
              })
# n_ = 7
# input_ = [1, 2, 3, 4, 5, 6, 7]
# K_ = 10
# result_ = DoWork(n_, K_, input_)
# print(f"Result: {result_}")

run_test_case()

# DO NOT remove/modify the below line
# PLCHLDR_TSTCASE_EXE#
