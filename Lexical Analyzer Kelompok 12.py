import string

sentence = input("input: ")
inputStr = sentence.lower()+'#'

alphabetList = list(string.ascii_lowercase)
stateList = ['S', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16',
             'q17', 'q18', 'q19', 'q20', 'q21', 'FS']
transitionTable = {}

for state in stateList:
    for alphabet in alphabetList:
        transitionTable[(state, alphabet)] = 'error'
    transitionTable[(state, '#')] = 'error'
    transitionTable[(state, ' ')] = 'error'

#initial state
transitionTable['S', ' '] = 'S'

#ambo
transitionTable['S', 'a'] = 'q1'
transitionTable['q1', 'm'] = 'q2'
transitionTable['q2', 'b'] = 'q3'
transitionTable['q3', 'o'] = 'FS'

#andi
transitionTable['S', 'a'] = 'q1'
transitionTable['q1', 'n'] = 'q4'
transitionTable['q4', 'd'] = 'q5'
transitionTable['q5', 'i'] = 'FS'

#pakai
transitionTable['S', 'p'] = 'q15'
transitionTable['q15', 'a'] = 'q16'
transitionTable['q16', 'k'] = 'q17'
transitionTable['q17', 'a'] = 'q20'
transitionTable['q20', 'i'] = 'FS'

#bali
transitionTable['S', 'b'] = 'q18'
transitionTable['q18', 'a'] = 'q19'
transitionTable['q19', 'l'] = 'q20'
transitionTable['q20', 'i'] = 'FS'

#baok
transitionTable['S', 'b'] = 'q18'
transitionTable['q18', 'a'] = 'q19'
transitionTable['q19', 'o'] = 'q21'
transitionTable['q21', 'k'] = 'FS'

#goni
transitionTable['S', 'g'] = 'q6'
transitionTable['q6', 'o'] = 'q7'
transitionTable['q7', 'n'] = 'q8'
transitionTable['q8', 'i'] = 'FS'

#kaco
transitionTable['S', 'k'] = 'q9'
transitionTable['q9', 'a'] = 'q10'
transitionTable['q10', 'c'] = 'q12'
transitionTable['q12', 'o'] = 'FS'

#kau
transitionTable['S', 'k'] = 'q9'
transitionTable['q9', 'a'] = 'q10'
transitionTable['q10', 'u'] = 'FS'

#oto
transitionTable['S', 'o'] = 'q11'
transitionTable['q11', 't'] = 'q12'
transitionTable['q12', 'o'] = 'FS'

#onda
transitionTable['S', 'o'] = 'q11'
transitionTable['q11', 'n'] = 'q13'
transitionTable['q13', 'd'] = 'q14'
transitionTable['q14', 'a'] = 'FS'

#final state
transitionTable['FS', ' '] = 'FS2'
transitionTable['FS', '#'] = 'accept'
transitionTable['FS2', ' '] = 'FS2'
transitionTable['FS2', '#'] = 'accept'

#reverse
transitionTable['FS2', 'b'] = 'q18'
transitionTable['FS2', 'p'] = 'q15'
transitionTable['FS2', 'a'] = 'q1'
transitionTable['FS2', 'g'] = 'q6'
transitionTable['FS2', 'k'] = 'q9'
transitionTable['FS2', 'o'] = 'q11'

idxChar = 0
state = 'S'
currentToken = ''
while state != 'accept':
    currentChar = inputStr[idxChar]
    currentToken += currentChar
    state = transitionTable[(state, currentChar)]
    if state == 'FS':
        print('Current Token:', currentToken, 'valid')
        currentToken = ' '
    if state == 'error':
        print('error')
        break
    idxChar += 1

if state == 'accept':
    print('Semua token di input: ', sentence, ', valid')

"""Petunjuk menjalankan Lexical Analyzer
1.	Jalankan program
2.	Masukkan satu kata atau lebih yang ingin diperiksa kebenarannya (apakah bahasa minang atau bukan)
3.	Jika kata tersebut adalah Bahasa minang maka program akan mengeluarkan ‘valid’, jika tidak maka akan mengeluarkan 
    ‘error’"""

#Kelompok 12
