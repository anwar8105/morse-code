from converters import convertToMorse, convertToAlpha
from sys import exit
import string

# Punctuations
all_punctuations = string.punctuation
alphabets = string.ascii_lowercase

# coverted code
converted_code = []


def alphaToMorse():
    '''Convert alphabets to morse code'''

    while True:
        try:
            print('\nEnter alphabets or words')
            print('To jump back to main menu enter \'#\'')
            ask = input('\n>> ').lower().strip()
        except KeyboardInterrupt:
            print('Emergency Exit Triggered')
            exit()
        else:
            if ask == '#':                              # return to main menu
                mainMenu()
            elif not ask in all_punctuations:          # only accept alphabets, not punctuation
                convertToMorse(converted_code, ask)
                print('\nHere\'s the Converted Code\n')
                print(f"letter\t\t|   Morse Code\n{'=' * 30}")

                # unpack tuple values
                for tups in converted_code:
                    letter, code = tups
                    print(f"{letter}\t\t|   {code}")

                converted_code.clear()  # clearing the appended list
            else:
                print('Special characters are not allowed')
                print('\nEnter \'#\' to go back to main menu')
                print('Remember to enter alphabets only')
                continue


def morseToAlpha():
    '''Convert morse-code into alphabets'''

    while True:
        try:
            print('\nEnter morse-code separated by , with a space after comma e.g : . _, _ . . .')
            print('To jump back to main menu enter \'#\'')
            ask = input('\n>> ').lower().strip()
        except KeyboardInterrupt:
            print('Emergency Exit Triggered')
            exit()
        else:
            if ask == '#':  # return to main menu
                mainMenu()
            elif not ask in all_punctuations and not ask in alphabets:  # only accept alphabets, not punctuation
                lst = list(ask.split(', '))  # split

                convertToAlpha(converted_code, lst)
                print('\nHere\'s the Converted Code\n')
                print(f"Morse Code\t|   Letter\n{'=' * 30}")

                # unpack tuple values
                for tups in converted_code:
                    code, letter = tups
                    print(f"{code}\t\t|   {letter}")

                converted_code.clear()  # clearing the appended list
            else:
                print('Special characters are not allowed')
                print('\nEnter \'#\' to go back to main menu')
                print('Remember to enter alphabets only')
                continue


def mainMenu():
    converter = True   # true flag

    while converter:
        print('\n0. Convert alphabets to morse code')
        print('1. Convert morse code to Alphabets')
        print('\nOr enter (\'q\' or \'quit\') to exit')

        try:
            option = input('\nEnter your choice : ').lower().strip()
        except KeyboardInterrupt:
            print('Emergency Exit Triggered')
            exit()
        else:
            if option == str(0):
                alphaToMorse()
            elif option == str(1):
                morseToAlpha()
            elif option == 'q' or option == 'quit':
                exit()
            else:
                continue


print(f"""
{'=' * 55}
Hi!, and Welcome, to the morse code converter
{'=' * 55}
Select any options from below
""")

mainMenu()
