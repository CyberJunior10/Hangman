def instructions():
    print('Instructions:')
    print('You have 5 chances to guess the complete word.')
    print('If you guess the word, you win, If you dont guess the word, you lose.')
    print('If you guess the wrong letter, you lose one chance, You can enter only alphabetical characters.')
    print('It is just a simple game, Dont take it seriously.')
    print('Save the Hangman !, Enjoy !')


def victory():
    print('\/ _ |  |   |  | | |\ |  |')
    print(' |(_)|__|   \/\/ | | \|  .')
    print('The word is: ', words)
    print('   O \n'
          '  /|\ \n'
          '  / \ \n'
          'Safe to go home !!!')


def turns4():
    print('   _____ \n'
          '  |     | \n'
          '  |     |\n'
          '  |     | \n'
          '  |      \n'
          '  |      \n'
          '  |      \n'
          '__|__\n')


def turns3():
    print('   _____ \n'
          '  |     | \n'
          '  |     |\n'
          '  |     | \n'
          '  |     O \n'
          '  |      \n'
          '  |      \n'
          '__|__\n')


def turns2():
    print('   _____ \n'
          '  |     | \n'
          '  |     |\n'
          '  |     | \n'
          '  |     O \n'
          '  |    /|\ \n'
          '  |      \n'
          '__|__\n')


def turns1():
    print('   _____ \n'
          '  |     | \n'
          '  |     |\n'
          '  |     | \n'
          '  |     O \n'
          '  |    /|\ \n'
          '  |      \n'
          '__|__\n')


def turns0():
    print('   _____ \n'
          '  |     | \n'
          '  |     |\n'
          '  |     | \n'
          '  |     O \n'
          '  |    /|\ \n'
          '  |    / \ \n'
          '__|__\n'
          'Hanged, you were not able to save the Hangman !\n')


def draw():

    if turns == 4:
        turns4()
    elif turns == 3:
        turns3()
    elif turns == 2:
        turns2()
    elif turns == 1:
        turns1()
    elif turns == 0:
        turns0()


play_again = True
while play_again:
    name = input('Enter your name: ')
    turns = 5
    guesses = ''
    print('Hello ', name)
    print('Welcome to the game')
    print('Guess the word, save Hangman')

    words = name

    instructions()

    while turns > 0:
        failed = 0
        for char in words:
            if char in guesses:
                print(char, end=' ')
            else:
                print('_', end=' ')
                failed += 1
        if failed == 0:

            victory()

            break

        guess = input('guess a character: ')
        if len(guess) != 1:
            print('You can only enter one letter character !')
            continue
        guesses += guess
        if guess not in words:
            turns -= 1

            draw()

            print('You have', + turns, 'more guesses')
            if turns == 0:
                print('The word is: ', words)
                print('Game Over!')
    print('Do you want to play again (y/n)?')
    play_again = input()
    if play_again == 'y':
        play_again = True
    elif play_again == 'n':
        play_again = False
    else:
        print('Invalid input')
        play_again = False
else:
    print('Thank you for playing')