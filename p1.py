'''
Dunya Oguz, 40181540
Part 1 of the programming assignment for COMP 5361 - Discrete Structures and Formal Languages,
taught by Prof. Gosta Grahne, Winter 2021.
'''

from typing import List

# directives for user inputs
d0 = '''Enter a list of truth assignments for any number of propositional variables.
The truth assignments must be entered as T for true and F for false.
Each truth value must be separated with a space.

Example input: T F F T F F T T'''

d1 = '''\nEnter a propositional sentence involving these propositional variables.

Refer to propositional variables using their index in the list you entered.
As an example, to refer to the first truth assignment in the list, simply enter 0.
Do not include more variables than you input, and make sure to use the right indices.

The negation symbol must directly precede the propositional variable, as shown in the example below.
Every other logical operator must be separated with a space.

Use paranthesis to dictate conditional precedence.

Represent logical operators using the following symbols:

\t1. Negation: ~
\t2. Conjuction: ^
\t3. Disjunction: v
\t4. Conditional: ->
\t5. Biconditional: <->

Example input: ((0 ^ 1) v (~3 -> 1)) <-> ~2'''

def get_user_input() -> (List[str], str):
    '''
    bla bla bla

    Parameters:
        None

    Returns:
        ksksks
    '''
    # Get list of truth assignments
    print(d0)
    while True:
        try:
            t = input('\n---> ')
            parsed_t = t.strip().split(' ')
            if set(parsed_t) not in [{'T', 'F'}, {'T'}, {'F'}]:
                raise ValueError
            break
        except ValueError:
            print('Invalid input entered. Valid inputs may only contain the strings T and F. Please try again.')
            continue

    # Get propositonal sentence
    print(d1)
    while True:
        try:
            s = input('\n---> ')
            list_s = s.replace('(', '').replace(')', '').split()
            variables = [int(_.lstrip('-')) for _ in list_s if _.lstrip('-').isdigit()]
            if len(variables) > len(parsed_t) or max(variables) >= len(parsed_t):
                raise ValueError
            break
        except ValueError:
            print('More propositional variables were specified than entered, or the indices specified were wrong. Please try again.')
            continue

    return parsed_t, '('+s+')'

def evaluate_logical_expression(t0, symbol, t1) -> bool:
    '''
    bla bla bla

    Parameters:
        kdkdkd
    Returns:
        ksksks
    '''
    if symbol == '^':
        return t0 and t1
    elif symbol == 'v':
        return t0 or t1
    elif symbol == '->':
        return not t0 or t1
    elif symbol == '<->':
        return t0 == t1

def solve_atomic_proposition(s) -> str:
    '''
    bla bla bla

    Parameters:
        kdkdkd
    Returns:
        ksksks
    '''

    stack = []
    trues, falses = ['T', '~F', 'True'], ['F', '~T', 'False']

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            j = stack.pop()
            atomic_p = [True if _ in trues else False if _ in falses else _ for _ in s[j+1:i].split(' ')]
            result = evaluate_logical_expression(atomic_p[0], atomic_p[1], atomic_p[2])
            return s[0:j] + str(result) + s[i+1:]

def solve_propositional_sentence(t, s) -> bool:
    '''
    bla bla bla

    Parameters:
        kdkdkd
    Returns:
        ksksks
    '''

    # replace T/F's with True/False
    t = {str(i): _ for i, _ in enumerate(t)}
    for k, v in t.items():
        s = s.replace(k, v)

    if len(s.split(' ')) == 1:
        return 'True' if s == '(T)' else 'False'

    i = 1
    while len(s.split(' ')) > 1:
        s = solve_atomic_proposition(s)
        print(f'Step {i}: {s}')
        i += 1

    return s.strip('()')

if __name__ == '__main__':

    print('\n========== GETTING USER INPUT ==========\n')
    t, s = get_user_input()
    print(t, s)

    print('\n========== SOLVING PROPOSITION ==========\n')
    r = solve_propositional_sentence(t, s)

    print(f'Final result: {r}')
