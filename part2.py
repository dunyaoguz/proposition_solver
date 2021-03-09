from typing import List
from user_instructions import get_user_input
from part1 import solve_propositional_sentence


def find_all_truth_permutations(t) -> List[List[bool]]:
    '''Finds all permutations of truth values for any number of propositonal
    variables.

    Parameters:
    -----------
        t: list
            List of truth assignments provided by the user.

    Returns:
    --------
        list
            List of different combination of values the propositional variables
            can take.
    '''

    truth_values = [['T', 'F']]*len(t)

    def recur(truth_values, truth_set=[], result=[]):
        # Base case is reached when a single permutation is found
        if not truth_values:
            result.append(truth_set)
            return

        # FOR DEBUG
        # print(truth_set, result)
        for truth_value in truth_values[0]:
            recur(truth_values[1:], truth_set + [truth_value], result)

    result = []
    recur(truth_values, result=result)
    return result


def print_truth_table(vals, s) -> None:
    '''Solves propositional sentence s for each combination of truth values
    given in vals and prints the results in a table.

    Parameters:
    -----------
        vals: list
            List of all the possible truth values that the propositional
            variables given by the user can assume.
        s: string
            The propositional sentence provided by the user.
    '''

    results = []
    delim = '   |   '

    for i, v in enumerate(vals):
        r = solve_propositional_sentence(v, s)
        results.append(r)
        row = str(i).rjust(4) + delim + delim.join(v) + delim + r.ljust(7)

        if i == 0:
            print((len(row)+4)*('-'))

        print('||' + row + '||')

        if i == len(vals)-1:
            print((len(row)+4)*('-'))

    if set(results) == 'False':
        assessment = 'CONTRADICTION'
    elif set(results) == 'True':
        assessment = 'TAUTOLOGY'
    else:
        assessment = 'CONTINGENCY'

    print(f'\nThe statement is a {assessment}.\n')


if __name__ == '__main__':

    print('\n============ GETTING USER INPUT ============\n')
    t, s = get_user_input()

    print('\n========== GENERATING TRUTH TABLE ==========\n')
    vals = find_all_truth_permutations(t)
    print_truth_table(vals, s)
