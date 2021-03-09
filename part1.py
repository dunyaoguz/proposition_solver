from user_instructions import get_user_input


def evaluate_logical_expression(t0, symbol, t1) -> bool:
    '''bla bla bla

    Parameters:
    -----------
        kdkdkd

    Returns:
    --------
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
    '''bla bla bla

    Parameters:
    -----------
        kdkdkd

    Returns:
    --------
        ksksks
    '''

    stack = []
    true, false = ['T', '~F', 'True'], ['F', '~T', 'False']

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            j = stack.pop()
            at = s[j+1:i].split(' ')
            p = [True if _ in true else False if _ in false else _ for _ in at]
            result = evaluate_logical_expression(p[0], p[1], p[2])
            return s[0:j] + str(result) + s[i+1:]


def solve_propositional_sentence(t, s, explain=False) -> bool:
    '''bla bla bla

    Parameters:
    -----------
        kdkdkd

    Returns:
    --------
        ksksks
    '''

    # Replace indices in the propositional sentence with their respective value
    t = {str(i): _ for i, _ in enumerate(t)}
    for k, v in t.items():
        s = s.replace(k, v)

    # If the user only provided one variable, return its value
    if len(s.split(' ')) == 1:
        return 'True' if s == '(T)' else 'False'

    # If the user provided more than one variable, solve the propositional
    # sentence by sequentially solving atomic propositions according to their
    # precedence as dictated by parantheses
    i = 1
    while len(s.split(' ')) > 1:
        s = solve_atomic_proposition(s)
        if explain:
            print(f'Step {i}: {s}')
        i += 1

    return s.strip('()')


if __name__ == '__main__':

    print('\n========== GETTING USER INPUT ==========\n')
    t, s = get_user_input()

    print('\n========== SOLVING PROPOSITION ==========\n')
    r = solve_propositional_sentence(t, s, True)

    print(f'Final result: {r}')
