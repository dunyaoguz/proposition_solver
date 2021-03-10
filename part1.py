from user_instructions import get_user_input


def logic_util(t0, symbol, t1) -> bool:
    '''Util function used in evaluate_logical_expression. Solves a logical
    expression composed of two truth values.

    Parameters:
    -----------
        t0: bool
            The first truth value.
        symbol: str
            The string representation of the logical operator according to
            program instructions.
        t1: bool
            The second truth value.

    Returns:
    --------
        bool
            The outcome of the logical operation performed.
    '''
    if symbol == '^':
        return t0 and t1
    elif symbol == 'v':
        return t0 or t1
    elif symbol == '->':
        return not t0 or t1
    elif symbol == '<->':
        return t0 == t1


def solve_logical_expression(exp):
    '''Solves a logical expression inside a paranthesis. Can be composed of
    two or more variables.

    Parameters:
    -----------
        exp: str
            An atomic proposition within the propositional sentence entered by
            the user.

    Returns:
    --------
        bool
            The outcome of the logical operation performed.
    '''
    true, false = ['T', '~F', 'True', '~False'], ['F', '~T', 'False', '~True']
    p = [True if _ in true else False if _ in false else _ for _ in exp]

    result = logic_util(*p[0:3])
    if len(p) > 3:
        while len(p) > 3:
            p = [result] + p[3:]
            result = logic_util(*p[0:3])
    return result


def identify_atomic_proposition(s) -> str:
    '''Identifies the atomic proposition within a given propositional sentence
    that needs to be solved first, passes it onto solve_logical_expression
    and returns a condensed propositional sentence using the result.

    Parameters:
    -----------
        exp: str
            The propositional sentence entered by the user.

    Returns:
    --------
        str
            A condensed version of th given propositional sentence.
    '''
    stack = []
    is_negation = {}

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
            # Check if the paranthesis is preceded by a negation
            is_negation[i] = True if s[i-1] == '~' else False
        elif char == ')':
            # Find the position of the opening paranthesis that corresponds to
            # the closing paranthesis, and evaluate the logical expression
            # inside the two paranthesis
            j = stack.pop()
            atomic_proposition = s[j+1:i].split(' ')
            result = solve_logical_expression(atomic_proposition)
            # Apply negation if necessary
            if is_negation[j]:
                result = not result
                return s[0:j-1] + str(result) + s[i+1:]
            return s[0:j] + str(result) + s[i+1:]


def solve_propositional_sentence(t, s, explain=False) -> bool:
    '''Solves the propositional sentence inputted by the user by iteratively
    passing it onto identify_atomic_proposition until the statement is composed
    of a single truth value.

    Parameters:
    -----------
        t: list
            The list of truth assignments entered by the user.
        s: str
            The propositional sentence entered by the user.
        explain: bool
            If set to true, function prints each step it iterates through in
            solving the propositional sentence.

    Returns:
    --------
        bool
            The final result of the propositional sentence.
    '''
    # Replace indices in the propositional sentence with their respective value
    t = {str(i): _ for i, _ in enumerate(t)}
    for k, v in t.items():
        s = s.replace(k, v)

    # If the user only provided one variable, return
    if len(s.split(' ')) == 1:
        return 'True' if s == '(T)' else 'False'

    # If the user provided more than one variable, solve the propositional
    # sentence by sequentially solving the atomic propositions within it
    i = 1
    while len(s.split(' ')) > 1:
        s = identify_atomic_proposition(s)
        if explain:
            print(f'Step {i}: {s}')
        i += 1
    return s.strip('()')


if __name__ == '__main__':
    print('\n========== GETTING USER INPUT ==========')
    t, s = get_user_input()

    print('\n========== SOLVING PROPOSITION ==========\n')
    r = solve_propositional_sentence(t, s, True)

    print(f'Final result: {r}')
