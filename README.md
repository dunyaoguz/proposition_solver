# COMP5361

## Directory

* `user_instructions.py`: Gets user input based on a set of instructions, checks for their validity of them and parses them. 
* `part1.py`: Code that answers part 1 of the assignment. Solves a given propositional sentence, based on truth assignments entered by the user.
* `part2.py`: Code that answers part 2 of the assignment. Prints a truth table for a given propositional sentence and determines if its a tautology, contradiction or contingency. 
* `unit_tests.py`: Includes 20+ unit statements that test the correctness of the core functions in the program used to solve propositions against expected output. Not meant for end users.
* `screenshots/`: Includes screenshots of program output from the example propositional sentences given in the assignment.

## How to execute

* Simply run `python part1.py` from terminal to run part 1.
* Simply run `python part2.py` from terminal to run part 2.

## Example propositional sentences to run:
* ((0 ^ 1) v (2 ^ T)) v ((~0 ^ ~2) ^ 1)
* (~0 ^ (0 v 1)) -> 1
* 1 ^ (0 -> ~1) ^ (~0 -> ~1)
* (0 -> (1 -> 2)) -> ((0 -> 1) -> 2)
