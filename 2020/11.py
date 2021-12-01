def convert_to_digit(letter):
    alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if letter[0] == '-':
        letter = letter[1:]
        neg = True
    else:
        neg = False

    for i,c in enumerate(alf):
        if letter == c:
            if neg:
                return -(i+1)
            else:
                return i+1
            

def convert_to_letter(digit):
    alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(26):
        if i+1 == digit:
            return alf[i]

def get_candidates():
    f = open('opentaal-wordlist-master/basiswoorden-gekeurd.txt', 'r')
    words = f.read().split('\n')

    candidates = []
    for word in words:
        if len(word) == 9 and word[3:].upper() == 'TRA':
            candidates.append(word.upper())

    f.close()

    print(candidates)
    
    return candidates

def find_combinations(string, candidates):
    f = open('opentaal-wordlist-master/basiswoorden-gekeurd.txt', 'r')
    words = f.read().split('\n')

    for candidate in candidates:
        word = []
        cont = True
        for i,c in enumerate(candidate[:3]):
            if string[i] == '*':
                word.append(c)
            else:
                # digit = convert_to_digit(c) - convert_to_digit(string[i])
                digit = convert_to_digit(string[i]) - convert_to_digit(c)
                if digit < 1 or digit > 26:
                    cont = False
                    break
                word.append(convert_to_letter(digit))

        if cont:
            word = ''.join(word)
            print(candidate, '-', word, '=', ' '.join(string))
            # if word.lower() in words:
            #     print(candidate, '-', word, '=', ' '.join(string))

# string = 'G F -K Z E L'.split(' ')
# candidates = get_candidates()
# candidates.append('AARZEL')
# candidates.append('SUIZEL')
# candidates.append('DUIZEL')
# candidates.append('BEUZEL')
# candidates.append('GIJZEL')
# candidates.append('FOEZEL')
# candidates.append('JEUZEL')
# candidates.append('NEUZEL')
# candidates.append('PEUZEL')
# print('Found', len(candidates), 'candidates')

string = '* -K * D -O Q -T -R -A'.split(' ')
candidates = get_candidates()
candidates.append('CLEOPATRA')
candidates.append('TROELSTRA')
candidates.append('PALAESTRA')
print('Found', len(candidates), 'candidates')

find_combinations(string, candidates)