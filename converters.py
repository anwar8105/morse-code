from morse_code import morseCode


def convertToMorse(lst, words):
    for letters in words:
        if letters in morseCode.keys():
            lst.append((letters, morseCode[letters]))   # append as tuple

    return lst


def convertToAlpha(converted_code, lst):
    for codes in lst:
        for key, value in morseCode.items():
            if codes == value:
                converted_code.append((value, key))

    return converted_code
