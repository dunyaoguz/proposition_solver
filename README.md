# COMP5361

## Directory

* `user_instructions.py`: Gets user input based on a set of instructions, checks for their validity and parses them. 
* `part1.py`: Code that answers part 1 of the assignment. Solves a given propositional sentence, based on truth assignments entered by the user.
* `part2.py`: Code that answers part 2 of the assignment. Prints a truth table for a given propositional sentence and determines if its a tautology, contradiction or contingency. 
* `unit_tests.py`: Includes 30+ unit tests that test the correctness of the core functions of the program. Checks whether the output of the functions aligns with what's expected for some propositions that have been pre-solved manually.
* `screenshots/`: Includes screenshots of program output from the example propositional sentences given in the assignment.

## Expected Inputs 

The program asks the user for two inputs. First is a list of truth assignments for any number of variables. The truth assignments must be entered as T for true and F for false. Each truth value must be separated with a space. 

#### Example input: T F F T F F T T

The second input that must be entered by the user is a propositional sentence. The propositional sentence must refer to the variables entered previously using their index in the list. As an example, to refer to the first truth assignment in the list, users must enter 0. Logical operators must be represented using the following symbols:

   1. Negation: ~
   2. Conjuction: ^
   3. Disjunction: v
   4. Conditional: ->
   5. Biconditional: <->

Paranthesis must be used to dictate precedence. The negation symbol must directly precede variables or parantheses. Every other logical operator must be separated with a space. Refer to the examples below for further clarification.

#### Example propositional sentences:
* `((0 ^ 1) v (2 ^ T)) v ((~0 ^ ~2) ^ 1)`
* `(~0 ^ (0 v 1)) -> 1`
* `1 ^ (0 -> ~1) ^ (~0 -> ~1)`
* `(0 -> (1 -> 2)) -> ((0 -> 1) -> 2)`

## Program Execution

* Simply run `python part1.py` from terminal to run part 1.
* Simply run `python part2.py` from terminal to run part 2.

