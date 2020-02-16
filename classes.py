import numpy as np
from itertools import compress
import copy
import pygame


class Session:
    # initiate session
    def __init__(self):
        self.player = Player('you', 0)                 # initiate Player object
        self.computer = Computer('hal 9000', 1)        # initiate Computer object
        self.current_board = Board()                   # initiate Board object
        self.games = 0
        self.name_list = [self.player.name, self.computer.name]
        self.score = '%s  %d:%d  %s' % (self.player.name, self.player.wins, self.computer.wins, self.computer.name)

        print('\n')
        print(self.score)
        print('\n')
        self.current_board.show()
        print('\n')
        print('your move...')

    # initiates new board at the end of a game
    def new_game(self):
        self.current_board = Board()
        self.games += 1
        print('-- new game --')
        print('\n')

        if self.name_list[self.games%2] == self.computer.name:
            print("{}'s move...".format(self.computer.name))
            self.computer.move(self, self.current_board)
            print('\n')
        else:
            print('your move...')
            self.current_board.show()

    def show(self):
        print('players:', self.name_list)
        print('games finished:', self.games)
        print('score:', self.score)


class Board:
    def __init__(self):
        self.col1, self.col2, self.col3, self.col4 = [], [], [], []
        self.board = [self.col1, self.col2, self.col3, self.col4]
        self.col_list = ['col1', 'col2', 'col3', 'col4']

    def update(self):
        self.board = [self.col1, self.col2, self.col3, self.col4]

    def show(self):
        print_grid(self.board)


class Player:
    def __init__(self, name, counter):
        self.name = name
        self.counter = counter
        self.wins = 0

    def move(self, session, board, column):
        if len(column) < 4:
            column.append(self.counter)
            board.update()

            if check_win(board.board) == True:
                print('\n')
                board.show()
                print(self.name, 'win!')
                self.wins += 1
                session.score = '%s  %d:%d  %s' % (self.name, self.wins, session.computer.wins, session.computer.name)
                print(session.score)
                print('\n')
                session.new_game()

            else:
                print('\n')
                board.show()
                print('\n')
                # automatically starts computer's move after player's move
                # this should be implemented within Session() class - i.e Session() class should dictate who's move it is
                print("{}'s move...".format(session.computer.name))
                session.computer.move(session, board)

        else:
            print('\n')
            print('Invalid move')
            print('\n')

    def show(self):
        print('name:', self.name)
        print('counter:', self.counter)
        print('wins:', self.wins)


class Computer:
    def __init__(self, name, counter):
        self.name = name
        self.counter = counter
        self.wins = 0

    def move(self, session, board):
        possible_cols = []
        for col in range(4):
            if len(board.board[col]) < 4:
                possible_cols.append(board.col_list[col])
            else:
                pass

        # computer makes random move
        choice = np.random.choice(possible_cols)

        if choice == 'col1':
            board.col1.append(self.counter)
        elif choice == 'col2':
            board.col2.append(self.counter)
        elif choice == 'col3':
            board.col3.append(self.counter)
        elif choice == 'col4':
            board.col4.append(self.counter)
        else:
            pass
        board.update()
        board.show()

        if check_win(board.board) == True:
            print(self.name, 'wins!')
            self.wins += 1
            session.score = '%s  %d:%d  %s' % (session.player.name, session.player.wins, self.wins, self.name)
            print(session.score)
            print('\n')
            session.new_game()
        else:
            pass

    def show(self):
        print('name:', self.name)
        print('counter:', self.counter)
        print('wins:', self.wins)


# helper function - checks for a winning board-state
def check_win(board):
    win = False

    # vertical
    for col in range(4):         # change when expanding dimensions of board
        for i in range(4):       # change when expanding dimensions of board
            try:
                if board[col][i] == board[col][i+1] and board[col][i+1] == board[col][i+2]:        # 3 in a row
                    win = True
                else:
                    pass
            except:
                pass

    # horizontal
    for i in range(4):           # change when expanding dimensions of board
        for col in range(4):     # change when expanding dimensions of board
            try:
                if board[col][i] == board[col+1][i] and board[col+1][i] == board[col+2][i]:        # 3 in a row
                    win = True
                else:
                    pass
            except:
                pass

    # diagonal
    for col in range(4):         # change when expanding dimensions of board
        for j in range(4):       # change when expanding dimensions of board
            try:
                if board[col][j] == board[col+1][j+1] and board[col+1][j+1] == board[col+2][j+2]:  # 3 in a row
                    win = True
                else:
                    pass
            except:
                pass
        for k in range(4):       # change when expanding dimensions of board
            try:
                if board[col][k+2] == board[col+1][k+1] and board[col+1][k+1] == board[col+2][k]:  # 3 in a row
                    win = True
                else:
                    pass
            except:
                pass
    return win


# helper function - prints board in grid format
def print_grid(board):
    display_board = copy.deepcopy(board)

    # pads all columns to length 4
    for col in display_board:
        col.insert(0,'─')
        while len(col) < 5:
            col += [' ']

    # prints grid
    display_board = [x[::-1] for x in display_board]
    display_board = [['|','|','|','|',' ']] + display_board + [['|','|','|','|',' ']]
    for a,b,c,d,e,f in zip(*display_board):
        print(a,b,c,d,e,f)
