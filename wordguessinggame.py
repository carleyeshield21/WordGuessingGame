import random
words = ['csharp', 'guitar', 'python']
rand = (random.choice(words))
print(rand)
display = []
for i in range(len(rand)):
    display += '_'
print(display)
counter = 0
endOfGame = False
while not endOfGame:
    guessletter = input('Guess a letter in the word: ').lower()
    for position in range(len(rand)):
        # print(position)
        letter = rand[position]
        if letter == guessletter:
            display[position] = letter
    if guessletter not  in rand:
        counter += 1
        if counter == 10:
            endOfGame = True
            print('Out of guesses')
    print(display)
    if '_' not in display:
        endOfGame = True
        # print(counter)
        print('Won')
        print(f'Number of wrong guesses: {counter}')