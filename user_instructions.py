from typing import List

q1 = '''Enter a list of truth assignments for any number of propositional variables.
The truth assignments must be entered as T for true and F for false.
Each truth value must be separated with a space.

Example input: T F F T F F T T'''

q2 = '''\nEnter a propositional sentence involving these propositional variables.
Refer to propositional variables using their index in the list you entered.
As an example, to refer to the first truth assignment in the list, simply enter 0.
Do not include more variables than you input, and make sure to use the right indices.

The negation symbol must directly precede the propositional variable, without space.
Every other logical operator must be separated with a space.

Use paranthesis to dictate conditional precedence.

Represent logical operators using the following symbols:

\t1. Negation: ~
\t2. Conjuction: ^
\t3. Disjunction: v
\t4. Conditional: ->
\t5. Biconditional: <->

Acceptable input example: ((0 ^ 1) v (~3 -> 1)) <-> ~2
Unacceptable input example: 0 ^ 1 v 2 [Must be `(0 ^ 1) v 2` or `0 ^ (1 v 2)`]'''


def get_user_input() -> (List[str], str):
    '''bla bla bla

    Returns:
    --------
        ksksks
    '''
    # Get list of truth assignments
    print(q1)
    while True:
        try:
            t = input('\n---> ')
            parsed_t = t.strip().split(' ')
            # Check for input errors
            if set(parsed_t) not in [{'T', 'F'}, {'T'}, {'F'}]:
                raise ValueError
            break
        except ValueError:
            print('Valid inputs may only contain T and F. Please try again.')
            continue

    # Get propositonal sentence
    print(q2)
    while True:
        try:
            s = input('\n---> ')
            parsed_s = '(' + s.strip() + ')'
            # Check for input errors
            l = s.replace('(', '').replace(')', '').split()
            variables = [int(_.lstrip('~')) for _ in l if _.lstrip('~').isdigit()]
            if len(variables) > len(parsed_t) or max(variables) >= len(parsed_t):
                raise ValueError
            break
        except ValueError:
            print('Incompatible number of variables or indices. Please try again.')
            continue

    return parsed_t, parsed_s
