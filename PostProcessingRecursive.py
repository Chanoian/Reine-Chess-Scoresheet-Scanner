# the example game is Paul Keres vs. Kurt Paul Otto Joseph Richter, 22 Sep 1942
# number of 'wrong' moves: 35
# Created by Alex Fung on 1/16/19!

import time
import chess.pgn
import itertools  # because I modify PGNs as strings (this is used in the string to PGN conversion)
import io

start = time.time()

# the moves and confs listed here are just for testing purposes
moves = [

    # 1

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

    ['B', 'R', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['g', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['4', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['+', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['K', 'B', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['c', 'e', 'a', 'x', 'x', 'x', 'x', 'x'],
    ['6', '5', 'x', 'x', 'x', 'x', 'x', 'x'],

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

    ['B', 'R', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['f', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['3', '6', 'x', 'x', 'x', 'x', 'x', 'x'],

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

    ['R', 'B', 'K', 'x', 'x', 'x', 'x', 'x'],
    ['c', 'e', 'a', 'g', 'x', 'x', 'x', 'x'],
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
    ['5', '6', '3', '8', 'x', 'x', 'x', 'x'],
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

    ['R', 'B', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['h', 'b', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['8', '3', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['+', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],  # 56

    ['K', 'B', 'Q', 'x', 'x', 'x', 'x', 'x'],
    ['g', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['1', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],

    ['_'],

    ['R', 'B', 'K', 'x', 'x', 'x', 'x', 'x'],
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
    # 1

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

    [0.5, 0.5, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [0.5, 0.5, 0, 0, 0, 0, 0, 0],
    [0.5, 0.5, 0.5, 0, 0, 0, 0, 0],
    [0.5, 0.5, 0, 0, 0, 0, 0, 0],

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

    [0.5, 0.5, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0.5, 0.5, 0, 0, 0, 0, 0, 0],

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

    [0.5, 0.5, 0.5, 0, 0, 0, 0, 0],
    [0.5, 0.5, 0.5, 0.5, 0, 0, 0, 0],
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
    [0.5, 0.5, 0.5, 0.5, 0, 0, 0, 0],
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

    [0.5, 0.5, 0, 0, 0, 0, 0, 0],
    [0.5, 0.5, 0, 0, 0, 0, 0, 0],
    [0.5, 0.5, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],  # 56

    [0.5, 0.5, 0.5, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],

    [-1],

    [0.5, 0.5, 0.5, 0, 0, 0, 0, 0],
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


# create the_possible_chars
def read_input(move_input, probability_input):
    all_the_possible_chars = []  # all possible variations of each move
    this_move = []  # find the possibilities for each move separately so we can iterate one-by-one

    for char in range(len(move_input)):  # iterating through the possibilities for each char

        # when the char is a space between moves
        if move_input[char][0] == '_':
            all_the_possible_chars.append(itertools.product(*this_move))
            this_move = []

        # when the char is low-confidence
        elif min_conf < probability_input[char][0] < certain_conf:
            possible_chars = []
            # generating possible chars
            for possible_char in range(len(move_input[char])):
                if probability_input[char][possible_char] > min_conf:
                    possible_chars.append(move_input[char][possible_char])
            this_move.append(possible_chars)

        # when the char is high-confidence
        else:
            this_move.append([move_input[char][0]])

    return all_the_possible_chars


# since the smallest unit we can check for validity is the move, we first find the possible variations of each move
def chars_to_moves(all_possible_chars):
    the_possible_moves = []

    for move_list in all_possible_chars:
        new_list = []
        for possible_move in move_list:
            new_move = ''
            for char in possible_move:
                new_move += char
            new_list.append(new_move)
        the_possible_moves.append(new_list)

    return the_possible_moves


possible_pgns = []
possible_moves = chars_to_moves(read_input(moves, confs))
pgn = []
boards = []
for move in range(len(possible_moves)):
    pgn.append('')
    boards.append('')  # filling up the list so we can set the value of list elements instead of appending
boards.append('')  # we use the board of move_num + 1 to calculate validity, thus one extra element is needed
boards[0] = chess.pgn.read_game(io.StringIO('e4')).board()  # just getting an empty starting board
best_guess = []


def check_variations(move_num):
    global best_guess
    highest_checked = 0

    for possible_move in possible_moves[move_num]:
        boards[move_num + 1] = boards[move_num].copy()

        try:
            boards[move_num + 1].push_san(possible_move)
            if move_num == len(possible_moves) - 1:
                pgn[move_num] = possible_move
                possible_pgns.append(pgn.copy())
            else:
                pgn[move_num] = possible_move
                # if there is no error, we recursively check until we either reach an error or find a completely
                #   valid game
                check_variations(move_num + 1)

        except ValueError:
            if move_num > highest_checked:
                best_guess = pgn.copy()
                highest_checked = move_num
            continue
    return


# removing pgns including moves that have moves which are notated as, but are not, checks
def check_for_checks(possible_pgn_list):
    checked_pgns = []
    for possible_pgn in possible_pgn_list:
        valid = True
        board = boards[0].copy()  # playing the game out again
        for half_move in possible_pgn:
            board.push_san(half_move)
            if half_move.endswith('+'):
                if not board.is_check():
                    valid = False
        if valid:
            checked_pgns.append(possible_pgn)
    return checked_pgns


# checked_pgns format is a list of single-unit lists, we need to reformat it into a pgn
def list_to_pgn(checked_pgn):
    reformatted = ''
    new_move = True
    move_num = 1
    for half_move in checked_pgn:
        if new_move:
            reformatted += str(move_num) + '.' + half_move + ' '
            new_move = False
        else:
            reformatted += half_move + ' '
            new_move = True
            move_num += 1

    return reformatted


# different result depending on how many error-free PGNs are found
def print_result(checked_pgns):
    if len(checked_pgns) == 1:
        valid_pgn = list_to_pgn(checked_pgns[0])
        print('The following pgn is valid:')
        print(valid_pgn)

    elif not len(checked_pgns) > 0:
        print('Sorry, we couldn\'t find a complete PGN--here\'s as far as we got:')
        print(best_guess)

    else:
        valid_pgn = list_to_pgn(checked_pgns[0])
        print('We found multiple possible PGNs--here\'s our best guess:')
        print(valid_pgn)

        print('The moves you should check are:')
        for half_move in range(len(checked_pgns[0])):
            correct = True

            for possible_pgn in range(len(checked_pgns) - 1):
                if checked_pgns[len(checked_pgns) - 1][half_move] != checked_pgns[possible_pgn][half_move]:
                    correct = False
            if not correct:
                if half_move % 2 == 0:
                    print('Move ' + str(int(half_move / 2 + 1)) + ' for white')
                else:
                    print('Move ' + str(int((half_move + 1) / 2)) + ' for black')
    return


# outputs of the program
check_variations(0)
print_result(check_for_checks(possible_pgns))

end = time.time()
print('Time: ')
print(end - start)