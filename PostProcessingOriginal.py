# using "python chess" library which reads PGNs and returns what all the errors are

# figure out which characters have a confidence of less than certain_conf, and out of those
# min_conf characters, which corresponding replacements have a value over the min_conf.

# "PSEUDO-CODE":

# INPUT FORMAT
# moves IS A LIST OF LISTS OF THE MOST LIKELY MOVES FOR EACH CHAR, MOVE DELIMITER == moves[n][0] == '_'
# confs IS A LIST OF LISTS OF THE PERCENT CERTAINTIES IN THOSE MOVES, MOVE DELIMITER == confs[n][0] == -1
# CONVERT moves TO template_pgn, REPLACING CHARACTERS WITH '_' IF char_conf < certain_conf
# CREATE LIST template_permutations WITH confs, WITH EACH SUBLIST CONTAINING POSSIBLE REPLACEMENTS FOR ONE '_'
# USE PERMUTATIONS OF template_permutations TO CREATE ALL POSSIBLE permutations
# ITERATE THROUGH template_pgn, REPLACING '_' WITH THE CORRESPONDING CHARACTER FROM permutations TO FORM pgn_string
# USE pgn_works TO TEST IF EACH PGN IS LEGAL
# PRINT PGNS WITH NO ERROR (TEST), THEN EXPORT TO FILE

# Created by Alex Fung on 1/4/19!

import time
import chess.pgn
import itertools  # because I modify PGNs as strings (this is used in the string to PGN conversion)
import io

start = time.time()

# the moves and confs listed here are just for testing purposes
# The moves with highest input confidence: 1. e8 e5. 'e' = 0.8, '8' = .8, 'e' = .8, '5' = 1, etc.
moves = [

    ['_'],  # 1

    ['e', 'c', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['e', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['5', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 2

    ['N', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['c', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['3', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['N', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['f', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['6', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 3

    ['N', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['f', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['3', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['N', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['c', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['6', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 4

    ['d', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['e', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['d', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 5

    ['N', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['d', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['B', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['b', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 6

    ['B', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['g', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['5', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['h', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['6', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 7

    ['B', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['h', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['g', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['5', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 8

    ['B', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['g', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['3', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['d', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['6', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 9

    ['R', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['c', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['1', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['N', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['d', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 10

    ['Q', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['d', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['B', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['f', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['5', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 11

    ['h', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['K', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['d', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['7', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 12

    ['R', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['d', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['1', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['N', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['e', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 13

    ['Q', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['e', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['5', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['B', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['c', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['3', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['+', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 14

    ['b', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['c', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['3', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['N', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['g', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['3', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 15

    ['f', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['g', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['3', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['B', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['g', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['6', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 16

    ['h', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['g', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['5', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['Q', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['g', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['5', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 17

    ['Q', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['f', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['R', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['a', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['e', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['8', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 18

    ['B', 'R', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['d', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['5', '6', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['Q', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['f', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 19

    ['g', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['f', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['b', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['6', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 20

    ['K', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['f', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['2', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['h', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['5', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 21

    ['e', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['3', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['h', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 22

    ['B', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['e', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['2', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['B', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['e', 'a', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', '7', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 23

    ['R', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['g', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['5', '6', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['R', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['e', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['g', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['8', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 24

    ['B', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['g', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['+', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['K', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['c', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['6', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 25

    ['R', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['g', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['8', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['R', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['g', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['8', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 26

    ['R', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['h', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['K', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['c', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['5', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 27

    ['B', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['f', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['3', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['B', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['f', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['3', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 28

    ['K', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['f', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['3', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['K', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['c', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 29

    ['R', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['h', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['7', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['R', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['f', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['8', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 30

    ['g', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['K', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['c', '0', 'o', 'x', 'x', 'x', 'x', 'x'],
    ['3', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 31

    ['K', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['e', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['c', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['5', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 32

    ['g', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['5', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['c', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 33

    ['K', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['d', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['5', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['K', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['b', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 34

    ['e', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['c', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['3', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 35

    ['R', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['h', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['2', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['R', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['c', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['8', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 36

    ['R', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['c', 'a', 'e', 'x', 'x', 'x', 'x', 'x'],
    ['2', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['b', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['5', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 37

    ['f', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['5', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['a', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['5', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 38

    ['K', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['d', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['6', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['K', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['c', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 39

    ['e', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['5', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['b', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 40

    ['K', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['d', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['7', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['R', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['a', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['8', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 41

    ['e', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['6', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['f', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['e', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['6', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 42

    ['f', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['6', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['a', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 43

    ['g', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['6', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['b', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['3', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 44

    ['a', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['b', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['3', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['+', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['a', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['b', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['3', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 45

    ['R', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['c', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['3', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['+', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['K', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['c', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['3', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 46

    ['f', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['7', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['b', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['2', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 47

    ['g', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['7', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['b', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['1', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['=', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['Q', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 48

    ['f', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['8', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['=', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['Q', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['Q', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['b', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['7', '4', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['+', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 49

    ['K', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['e', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['6', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['R', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['a', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['6', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['+', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 50

    ['K', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['e', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['5', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['Q', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['b', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['5', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['+', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 51

    ['K', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['f', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['R', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['a', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['+', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 52

    ['K', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['g', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['3', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['Q', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['d', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['3', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['+', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 53

    ['Q', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['f', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['3', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['R', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['a', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['8', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 54

    ['g', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['8', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['=', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['Q', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['R', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['g', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['8', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['+', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],


    ['_'],  # 55

    ['K', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['h', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['2', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['R', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['h', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['8', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['+', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 56

    ['K', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['g', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['1', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['R', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['g', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['8', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['+', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 57

    ['K', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['h', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['2', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['K', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['c', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['2', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 58

    ['Q', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['c', 'a', 'e', 'x', 'x', 'x', 'x', 'x'],
    ['6', '5', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['+', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['K', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['d', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['1', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 59

    ['Q', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['f', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['3', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['+', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['Q', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['c', 'e', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['2', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['+', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_']

]

confs = [
    [-1],  # 1

    [0.5, 0.5, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 2

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 3

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 4

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 5

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 6

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 7

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 8

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 9

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 10

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 11

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 12

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 13

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 14

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 15

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 16

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 17

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 18

    [0.5, 0.5, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0.5, 0.5, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 19

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 20

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 21

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 22

    [1, 0, 0, 0, 0, 0, 0, 0],
    [0.5, 0.5, 0, 0, 0, 0, 0, 0],
    [0.5, 0.5, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 23

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0.5, 0.5, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 24

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 25

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 26

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 27

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 28

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 29

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 30

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0.5, 0.5, 0.5, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 31

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 32

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 33

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 34

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 35

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 36

    [1, 0, 0, 0, 0, 0, 0, 0],
    [0.5, 0.5, 0.5, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 37

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 38

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 39

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 40

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 41

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 42

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 43

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 44

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 45

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 46

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 47

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 48

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0.5, 0.5, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 49

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 50

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 51

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 52

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 53

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 54

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 55

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 56

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 57

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 58

    [1, 0, 0, 0, 0, 0, 0, 0],
    [0.5, 0.5, 0.5, 0, 0, 0, 0, 0],
    [0.5, 0.5, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 59

    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [1, 0, 0, 0, 0, 0, 0, 0],
    [0.5, 0.5, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1]

]

certain_conf = 0.9  # chars will be double-checked if they have confidence below this
min_conf = 0.2  # chars will not be considered if their confidence is below this

template_pgn = []  # PGN with '_' when the confidence is low
template_permutations = []  # all the possible replacements for chars below certain_conf


# create template_pgn and template_permutations
def read_input(the_moves, the_confs):
    global template_pgn
    global template_permutations

    new_move = True
    move_num = 1  # counting "_" to determine whether to add a move number and a space, or just a space between moves
    for char in range(len(the_moves)):  # iterating through each sublist

        # when the char is a space between moves
        if the_moves[char][0] == '_':
            if new_move:
                if move_num != 1:
                    template_pgn.append(' ')  # spaces in between moves
                template_pgn.append(str(move_num) + '. ')  # move number
                move_num += 1
                new_move = False
            else:
                template_pgn.append(' ')  # space between white and black moves
                new_move = True

        # when the char is low-confidence
        elif the_confs[char][0] < certain_conf:
            # replacing low-confidence chars with '_'
            template_pgn.append('_')
            possible_chars = []
            # generating possible replacements for '_'
            appended = False  # make sure at least one value is available to replace the '_'
            for possible_char in range(len(the_moves[char])):
                if the_confs[char][possible_char] > min_conf:
                    possible_chars.append(the_moves[char][possible_char])
                    appended = True
            if not appended:
                possible_chars.append(the_moves[char][0])  # default value
            template_permutations.append(possible_chars)

        # when the char is high-confidence
        else:
            template_pgn.append(the_moves[char][0])

    return


# check if individual PGN is valid
def pgn_works(pgn_string):
    game_pgn = io.StringIO(pgn_string)  # string to PGN conversion
    if(chess.pgn.read_game(game_pgn)) == 'fails':
        return False  # source code is edited: each error returns "fails"
    else:
        return True


# outputs of the program
valid_pgns = []

total = 0


# iterate through all possibilities, find which PGNs are valid and export to valid_pgns and invalid_pgns
def record_if_valid():
    global valid_pgns
    global total

    for permutation in permutations:

        # generate PGNs
        permutation_index = 0  # replacing the '_' in order of permutation_index elements
        template_pgn_copy = template_pgn.copy()
        for char in range(len(template_pgn_copy)):
            if template_pgn_copy[char] == '_':
                template_pgn_copy[char] = permutation[permutation_index]
                permutation_index += 1
        # check PGNs
        pgn_string = ''.join(template_pgn_copy)
        if pgn_works(pgn_string):
            valid_pgns.append(pgn_string)
        total += 1
    return


# from input to template arrays
read_input(moves, confs)
# generating possible moves
permutations = itertools.product(*template_permutations)
# combine possible moves and template, use the Python Chess library to get valid PGNs
record_if_valid()

print('Total games analyzed: ')
print(total)

print('The following pgns are valid: ')
for pgn in valid_pgns:
    print(pgn)

end = time.time()
print('Time: ')
print(end - start)