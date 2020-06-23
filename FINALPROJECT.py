# Tic Tac Toe

import random

class TicTacToe():
    def drawBoard(board):
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')

        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')

    def inputPlayerLetter():
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print()
            print(p1name+': X or O?')
            letter = input().upper()
            print()

        if letter == 'X':
            print(p2name+' is O.')
            print()
            return ['X', 'O']
        else:
            print (p2name+' is X.')
            return ['O', 'X']


    def playAgain():
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    def makeMove(board, letter, move):
        board[move] = letter

    def isWinner(bo, le):
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
        (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
        (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
        (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
        (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
        (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
        (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
        (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

    def getBoardCopy(board):
        dupeBoard = []

        for i in board:
            dupeBoard.append(i)

        return dupeBoard

    def isSpaceFree(board, move):
        return board[move] == ' '

    def getPlayer1Move(board):
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not x.isSpaceFree(board, int(move)):
            print(p1name+'\'s move. (1-9)')
            move = input()
            print()
        return int(move)

    def getPlayer2Move(board):
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not x.isSpaceFree(board, int(move)):
            print(p2name+'\'s move. (1-9)')
            move = input()
            print()
        return int(move)


    def isBoardFull(board):
        for i in range(1, 10):
            if x.isSpaceFree(board, i):
                return False
        return True


gameIsPlaying = True
print('Insert player 1\'s name: ', end='')
p1name=input()
print()
print('Insert player 2\'s name: ', end='')
p2name=input()
turn = p1name
p1=0
p2=0
score={p1name:p1, p2name:p2}
while True:
    x=TicTacToe
    theBoard = [' '] * 10
    playerLetter, computerLetter = x.inputPlayerLetter()
    print(turn+' will go first.')
    print()
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == p1name:
            print(p1name.upper()+':')
            x.drawBoard(theBoard)
            turn = p2name
            move = x.getPlayer1Move(theBoard)
            x.makeMove(theBoard, playerLetter, move)
            if x.isWinner(theBoard, playerLetter):
                x.drawBoard(theBoard)
                print(p1name+' wins!')
                print()
                n=score.get(p1name)
                score.update({p1name:n+1})
                gameIsPlaying = False
            elif x.isBoardFull(theBoard):
                x.drawBoard(theBoard)
                print('The game is a tie!')
                print()
                break

        elif turn == p2name:
            print(p2name.upper()+':')
            x.drawBoard(theBoard)
            turn = p1name
            move = x.getPlayer2Move(theBoard)
            x.makeMove(theBoard, computerLetter, move)

            if x.isWinner(theBoard, computerLetter):
                x.drawBoard(theBoard)
                print(p2name+' wins!')
                print()
                n=score.get(p2name)
                score.update({p2name:n+1})
                gameIsPlaying = False
            elif x.isBoardFull(theBoard):
                x.drawBoard(theBoard)
                print('The game is a tie!')
                print()
                break

    print('SCORE:')
    print(p1name+'.......... '+str(score.get(p1name)))
    print(p2name+'.......... '+str(score.get(p2name)))
    print()
    if not x.playAgain():
        break
