import itertools as it
import more_itertools as mit
from termcolor import colored

def waarde_woord(woord, loc, direction, board):
    letterwaarde = {"A":1, "B":4, "C":5, "D":2, "E":1, "F":4, "G":3, "H":4, "I":2, "J":4, "K":3, "L":3, "M":3, "N":1, "O":1, "P":4, "Q":10, "R":2, "S":2, "T":2, "U":2, "V":4, "W":5, "X":8, "Y":8, "Z": 5}
    empty = [".", "d", "t", "2", "3"]

    def add_som(x, y):
        if board[x[0]][x[1]] == 'd':
            p = letterwaarde[y] * 2
        elif board[x[0]][x[1]] == 't':
            p = letterwaarde[y] * 3
        else: 
            p = letterwaarde[y]
        
        return p

    loc_letters = []
    som = 0
    final_woord = []
    extra_woords = []
    mult = 1
    
    if direction == 'h': 
        count = 0
        end = loc[1]
        for i in range(loc[1], 15):
            
            if count == len(woord):
                break
            
            if board[loc[0]][i] in empty:
                if board[loc[0]][i] in ['2', '3']:
                    mult *= int(board[loc[0]][i])
                loc_letters.append([[loc[0], i] , woord[count]])
                som += add_som([loc[0], i], woord[count])
                final_woord.append(woord[count])
                count += 1
            else:
                som += add_som([loc[0], i], board[loc[0]][i])
                final_woord.append(board[loc[0]][i])
            
            end += 1
        
        if loc[1] > 0:
            for i in range(loc[1]-1, -1, -1):
                if board[loc[0]][i] in empty:
                    break
                
                som += add_som([loc[0], i], board[loc[0]][i])
                final_woord.insert(0, board[loc[0]][i])

        if loc[1]+end < 15:
            for i in range(loc[1]+end, 15):
                if board[loc[0]][i] in empty:
                    break
                
                som += add_som([loc[0], i], board[loc[0]][i])
                final_woord.append(board[loc[0]][i])

        som *= mult
        mult = 1

        for x in loc_letters:
            som_extra = 0
            w = [x[1]]
            counter = False
            if x[0][0] > 0:
                for i in range(x[0][0]-1, -1, -1):
                    if board[i][x[0][1]] in empty:
                        break
                    else: 
                        som_extra += add_som([i, x[0][1]], board[i][x[0][1]])
                        w.insert(0, board[i][x[0][1]])
                        counter = True

            if x[0][0] < 15:
                for i in range(x[0][0]+1, 15):
                    if board[i][x[0][1]] in empty:
                        break
                    else: 
                        som_extra += add_som([i, x[0][1]], board[i][x[0][1]])
                        w.append(board[i][x[0][1]])
                        counter = True

            if len(w) > 1:
                extra_woords.append(''.join(w))

            if counter:
                if board[x[0][0]][x[0][1]] in ['2', '3']:
                    mult *= int(board[x[0][0]][x[0][1]])
                som_extra += add_som(x[0], x[1])
                som += som_extra*mult
                

    if direction == 'v':
        count = 0
        end = loc[0]
        for i in range(loc[0], 15):
            if count == len(woord):
                break

            if board[i][ loc[1]] in empty:
                if board[i][ loc[1]] in ['2', '3']:
                    mult *= int(board[i][ loc[1]])
                loc_letters.append([[i, loc[1]] , woord[count]])
                som += add_som([i, loc[1]], woord[count])
                final_woord.append(woord[count])
                count += 1
            else:
                som += add_som([i, loc[1]], board[i][loc[1]])
                final_woord.append(board[i][loc[1]])

            end += 1
        
        if loc[0] > 0:
            for i in range(loc[0]-1, -1, -1):
                if board[i][loc[1]] in empty:
                    break

                som += add_som([i, loc[1]], board[i][loc[1]])
                final_woord.insert(0, board[i][loc[1]])

        if loc[0]+end < 15:
            for i in range(loc[0]+end, 15):
                if board[i][loc[1]] in empty:
                    break

                som += add_som([i, loc[1]], board[i][loc[1]])
                final_woord.append(board[i][loc[1]])

        som *= mult
        mult = 1

        for x in loc_letters:
            som_extra = 0
            counter = False
            w = [x[1]]
            if x[0][1] > 0:
                for i in range(x[0][1]-1, -1, -1):
                    if board[x[0][0]][i] in empty:
                        break
                    else: 
                        som_extra += add_som([x[0][0], i], board[x[0][0]][i])
                        w.insert(0, board[x[0][0]][i])
                        counter = True

            if x[0][1] < 15:
                for i in range(x[0][1]+1, 15):
                    if board[x[0][0]][i] in empty:
                        break
                    else: 
                        som_extra += add_som([x[0][0], i], board[x[0][0]][i])
                        w.append(board[x[0][0]][i])
                        counter = True

            if len(w) > 1:
                extra_woords.append(''.join(w))

            if counter:
                if board[x[0][0]][x[0][1]] in ['2', '3']:
                    mult *= int(board[x[0][0]][x[0][1]])
                som_extra += add_som(x[0], x[1])
                som += som_extra*mult
                
    return som, ''.join(final_woord), extra_woords

def add_word(woord, loc, dir, board):
    for i,c in enumerate(woord):
        if dir == 'h':
            board[loc[0]][loc[1]+i] = c
        if dir == 'v':
            board[loc[0]+i][loc[1]] = c

    return board

def print_board(board):
    empty = [".", "d", "t", "2", "3"]
    for line in board:
        for letter in line:
            if letter in empty:
                print(letter + ' ', end = '')
            else:
                print(colored(letter, 'red') + ' ', end ='')

        print('\n', end = '')
    print()

def find_words(minimum_letters, extra_letters, board, points, file_name):
    f = open(file_name, 'w')
    empty = [".", "d", "t", "2", "3"]

    # Loop over all tiles on board for starting position of word
    for i in range(15):
        for j in range(15): 
            
            # Check if tile is empty
            if board[i][j] in empty:

                # Try horizontal and vertical placement of word
                for direction in ['h', 'v']:

                    # Check possible word lengths
                    for n in range(len(extra_letters)+1):
                        if direction == 'h': 
                            spots = board[i][j:]
                        if direction == 'v':
                            spots = [x[j] for x in board[i:]]

                        empty_spots = sum([1 for x in spots if x in empty])

                        # If word fits in empty places on board and word is connected
                        word_len = len(minimum_letters) + n
                        if empty_spots >= word_len:
                            if is_word_connected([i, j], direction, word_len, board):

                                # Check all letter combinations
                                for letters in it.combinations(extra_letters, n):
                                    check_all_letters(list(letters) + minimum_letters, [i,j], direction, board, points, f)

                        else:
                            break
    f.close()


def is_word_connected(loc, direction, word_len, board):
    empty = [".", "d", "t", "2", "3"]

    tiles = []
    if direction == 'h':
        if loc[0] > 0:
            tiles = tiles + board[loc[0]-1][loc[1]:loc[1]+word_len]
        if loc[0] < 14:
            tiles = tiles + board[loc[0]+1][loc[1]:loc[1]+word_len]
        if loc[1] > 0:
            tiles = tiles + list(board[loc[0]][loc[1]-1])
        if loc[1]+word_len-1 < 14:
            tiles = tiles + list(board[loc[0]][loc[1]+word_len])

    if direction == 'v':
        if loc[1] > 0:
            tiles = tiles + [x[loc[1]-1] for x in board[loc[0]:loc[0]+word_len]]
        if loc[1] < 14:
            tiles = tiles + [x[loc[1]+1] for x in board[loc[0]:loc[0]+word_len]]
        if loc[0] > 0:
            tiles = tiles + list(board[loc[0]-1][loc[1]])
        if loc[0]+word_len-1 < 14:
            tiles = tiles + list(board[loc[0]+word_len][loc[1]])

    tiles = ''.join(tiles)

    for c in empty:
        tiles = tiles.replace(c, '')

    if len(tiles) == 0:
        return False
    else:
        return True                    

def check_all_letters(letters, location, direction, board, points, f):
    if len(letters) == 7:
        addFourty = True
    else:
        addFourty = False

    words = mit.distinct_permutations(letters)
    
    for word in words:
        waarde, final_woord, extra_woords = waarde_woord(list(word), location, direction, board)

        if addFourty:
            waarde += 40

        if waarde == points:
            # print('hit:', final_woord + ', [' + str(location[0]) + ',' + str(location[1]) + '], ' + direction)
            
            f.write(str(location) + direction + ' ' + ''.join(word) + ': ' + final_woord + ' ' + str(extra_woords)  + '\n')
    
def fill_board():
    f = open('14_board.txt')
    empty_board = f.read().split('\n')
    empty_board = [list(x) for x in empty_board]
    print_board(empty_board)

    board = add_word('SUCCES', [7,7], 'h', empty_board)
    board = add_word('ISOGRAM', [6,2], 'h', board)
    board = add_word('AT', [5,1], 'h', board)
    board = add_word('EQUINOX', [4,0], 'v', board)
    board = add_word('DINERBON', [0,4], 'v', board)
    board = add_word('BEDTIJDEN', [2,2], 'v', board)
    board = add_word('DOOR', [8,8], 'h', board)
    board = add_word('ZITZAK', [1,3], 'h', board)
    board = add_word('LASAGNE', [2,7], 'h', board)
    board = add_word('LARVE', [9,3], 'v', board)
    board = add_word('VER', [13,2], 'h', board)
    board = add_word('WANT', [1,10], 'v', board)
    board = add_word('N', [14,3], 'v', board)
    board = add_word('WIEREN', [5,11], 'v', board)
    board = add_word('PEGEL', [3,1], 'h', board)
    board = add_word('HYPNOSE', [10,8], 'h', board)
    board = add_word('EFFENEN', [13,5], 'h', board)
    board = add_word('THEEDOEK', [4,14], 'v', board)
    board = add_word('KWANTUMCOMPUTER', [0,10], 'v', board)
    print_board(board)

    return board

def use_wordlist(file_name, lengte = 0):
    f = open('opentaal-wordlist-master/basiswoorden-gekeurd.txt', 'r')
    woorden = f.read().split('\n')

    g = open('14_result.txt', 'r')
    opties = g.readlines()

    for optie in opties:
        y = optie.replace("'", '').replace('[', '').replace(']', '').replace(',', '')
        y = y.split(': ')
        y = y[1].split(" ")

        # if lengte and len(y[0].lower()) == lengte:
        #     print(optie)

        if y[0].lower() in woorden:
            print(optie)
    
def count_letters(board):
    alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    limit = [7,2,2,5,18,2,3,2,4,2,3,3,3,11,6,2,1,5,5,5,3,2,2,1,1,2]
    for n,c in enumerate(alf):
        som = 0
        for i in range(15):
            for j in range(15):
                if board[i][j] == c:
                    som += 1
        print(c + ': ' + str(som) + '/' + str(limit[n]), end = '')
        if som == limit[n]:
            print('----\n', end = '')
        else:
            print('\n', end = '')
   
board = fill_board()

# find_words(list('DOOR'), list(''), board, 30, '14_result.txt')
# find_words(list('ZZTAK'), list(''), board, 22, '14_result.txt')
# find_words(list('AAES'), list('GLN'), board, 75, '14_result.txt')
# find_words(list('AELRV'), list(''), board, 21, '14_result.txt')
# find_words(list('RV'), list(''), board, 7, '14_result.txt')
# find_words(list('T'), list('TNOTW'), board, 18, '14_result.txt')
# find_words(list('N'), list('N'), board, 12, '14_result.txt')
# find_words(list('INW'), list('EOT'), board, 12, '14_result.txt')
# find_words(list('PGL'), list('NN'), board, 18, '14_result.txt')
# find_words(list('EPSY'), list('OHT'), board, 150, '14_result.txt')
# find_words(list(''), list('EEEFFNN'), board, 64, '14_result.txt')
# find_words(list(''), list('DEEHKOT'), board, 88, '14_result.txt')
# print('word list created\n')

# use_wordlist('14_result.txt')

count_letters(board)

