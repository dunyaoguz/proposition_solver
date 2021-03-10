from typing import List

q1 = '''
Enter a list of truth assignments for any number of variables.
The truth assignments must be entered as T for true and F for false.
Each truth value must be separated with a space.

Example input: T F F T F F T T
'''

q2 = '''
Enter a propositional sentence involving these variables.
Refer to propositional variables using their index in the list you entered.
As an example, to refer to the first truth assignment in the list, enter 0.
Don't include more variables than you provided in the previous section.
Make sure to use the right indices when referring to variables.

Represent logical operators using the following symbols:

\t1. Negation: ~
\t2. Conjuction: ^
\t3. Disjunction: v
\t4. Conditional: ->
\t5. Biconditional: <->

Use paranthesis to dictate conditional precedence.
The negation symbol must directly precede variables or parantheses.
Every other logical operator must be separated with a space.

Acceptable input example: ((0 ^ 1) v (~3 -> 1)) <-> ~2
Unacceptable input example: 0 ^ 1 v 2 [Must be `(0 ^ 1) v 2` or `0 ^ (1 v 2)`]
'''


def get_user_input() -> (List[str], str):
    '''Prints instructions on how users must format their input, checks for
    the validity of the inputs entered and parses them.

    Returns:
    --------
        List[str]
            Truth assignments entered by the user, parsed into a list
        str
            The propositional sentence entered by the user
    '''
    # Get list of truth assignments
    print(q1)
    while True:
        try:
            t = input('---> ')
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
            s = input('---> ')
            parsed_s = '(' + s.strip() + ')'
            # Check for input errors
            sl = s.replace('(', '').replace(')', '').split()
            vars = [int(_.lstrip('~')) for _ in sl if _.lstrip('~').isdigit()]
            if len(set(vars)) > len(parsed_t) or max(vars) >= len(parsed_t):
                raise ValueError
            break
        except ValueError:
            print('Incompatible number of variables or indices. Try again.')
            continue
    return parsed_t, parsed_s
