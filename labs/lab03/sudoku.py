"""
Run the various CSP solvers on selected Sudoku puzzles.
These calls are mostly copied/adapted from AIMA Python.

@author: kvlinden
@version 14feb2013
"""
from csp import Sudoku, easy1, AC3, harder1, backtracking_search, mrv, \
    forward_checking, min_conflicts
from search import depth_first_graph_search
import time

# 1. Set up the puzzle.
# Examples from the textbook
solved_fig64b = Sudoku('483921657967345821251876493548132976729564138136798245372689514814253769695417382')
easy_fig64a = Sudoku('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')
# Example from the AIMA csp.py library
harder_aima_csp = Sudoku('4173698.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......')
# Example from http://zonkedyak.blogspot.com/2006/11/worlds-hardest-sudoku-puzzle-al.html
hardest_escargot = Sudoku('1....7.9..3..2...8..96..5....53..9...1..8...26....4...3......1..4......7..7...3..')
puzzle = harder_aima_csp

print('\nStart:')
puzzle.display(puzzle.infer_assignment())

# 2. Solve the puzzle.
tic= time.perf_counter() # start timer

#depth_first_graph_search(puzzle)
#AC3(puzzle)
backtracking_search(puzzle, inference=forward_checking)
# Consider adding: select_unassigned_variable=mrv & inference=forward_checking
#min_conflicts(puzzle)

toc= time.perf_counter() #end timer
run_time = toc -tic


# 3. Print the results.  
if puzzle.goal_test(puzzle.infer_assignment()):
    print('\nSolution:')
    puzzle.display(puzzle.infer_assignment())
else:
    print('\nFailed - domains: ' + str(puzzle.curr_domains))
    puzzle.display(puzzle.infer_assignment())

print("Completed after", run_time, "seconds")

