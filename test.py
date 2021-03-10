import pytest
from part1 import solve_logical_expression, solve_propositional_sentence

class Test:
    def test_one(self):
        cases = [
            (['T', '^', 'T'], True),
            (['F', '^', 'T'], False),
            (['T', 'v', 'T'], True),
            (['F', 'v', 'T'], True),
            (['F', '->', 'F'], True),
            (['F', '->', 'T'], True),
            (['T', '<->', 'T'], True),
            (['T', '<->', 'F'], False),
            (['T', '^', 'T', '->', 'F'], False),
            (['T', '->', 'F', 'v', 'T'], True),
            (['F', '<->', 'T', '^', 'T'], False),
            (['F', 'v', 'F', '->', 'F'], True),
            (['T', 'v', 'T', 'v', 'T', 'v', 'T'], True),
            (['F', '^', 'F', '^', 'F', '^', 'F'], False),
        ]
        for (raw, expected) in cases:
            assert solve_logical_expression(raw) == expected

    def test_two(self):
        cases = [
            ((['T', 'T'], '((~0 ^ (0 v 1)) -> 1)'), 'True'),
            ((['F', 'F'], '((~0 ^ (0 v 1)) -> 1)'), 'True'),
            ((['T', 'T'], '(1 ^ (0 -> ~1) ^ (~0 -> ~1))'), 'False'),
            ((['F', 'F'], '(1 ^ (0 -> ~1) ^ (~0 -> ~1))'), 'False'),
            ((['T', 'T', 'T'], '((0 -> (1 -> 2)) -> ((0 -> 1) -> 2))'), 'True'),
            ((['F', 'T', 'T'], '((0 -> (1 -> 2)) -> ((0 -> 1) -> 2))'), 'True'),
            ((['F', 'T', 'F'], '((0 -> (1 -> 2)) -> ((0 -> 1) -> 2))'), 'False'),
            ((['F', 'F', 'F'], '((0 -> (1 -> 2)) -> ((0 -> 1) -> 2))'), 'False'),
            ((['T', 'F', 'T'], '(((0 v 2) ^ (1 v 2)) <-> ((0 ^ 1) v 2))'), 'True'),
            ((['T', 'F', 'F'], '(((0 v 2) ^ (1 v 2)) <-> ((0 ^ 1) v 2))'), 'True'),
            ((['F', 'F', 'T'], '(((0 v 2) ^ (1 v 2)) <-> ((0 ^ 1) v 2))'), 'True'),
            ((['F', 'F', 'F'], '(((0 v 2) ^ (1 v 2)) <-> ((0 ^ 1) v 2))'), 'True'),
            ((['T', 'T'], '((0 ^ ~(~0 v 1)) v (0 ^ 1))'), 'True'),
            ((['F', 'T'], '((0 ^ ~(~0 v 1)) v (0 ^ 1))'), 'False'),
            ((['T', 'T'], '((0 ^ (~1 -> ~0)) -> 0)'), 'True'),
            ((['T', 'F'], '((0 ^ (~1 -> ~0)) -> 0)'), 'True'),
            ((['T', 'F', 'T'], '(((0 -> 2) v (1 -> 2)) -> ((0 v 1) -> 2))'), 'True'),
            ((['T', 'F', 'F'], '(((0 -> 2) v (1 -> 2)) -> ((0 v 1) -> 2))'), 'False'),
            ((['F', 'T', 'F'], '(((0 -> 2) v (1 -> 2)) -> ((0 v 1) -> 2))'), 'False'),
            ((['F', 'F', 'F'], '(((0 -> 2) v (1 -> 2)) -> ((0 v 1) -> 2))'), 'True'),
            ((['T', 'T', 'T'], '((0 -> (1 -> 2)) <-> ((0 -> 1) -> 2))'), 'True'),
            ((['T', 'T', 'F'], '((0 -> (1 -> 2)) <-> ((0 -> 1) -> 2))'), 'True'),
            ((['F', 'T', 'F'], '((0 -> (1 -> 2)) <-> ((0 -> 1) -> 2))'), 'False'),
            ((['F', 'F', 'F'], '((0 -> (1 -> 2)) <-> ((0 -> 1) -> 2))'), 'False'),
        ]
        for (raw, expected) in cases:
            assert solve_propositional_sentence(*raw) == expected


for (raw, expected) in cases:
    r = solve_propositional_sentence(*raw)
    b = r == expected
    if b == False:
        print(raw, expected, r)
