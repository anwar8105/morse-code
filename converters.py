from morse_code import morseCode


class Converter:
    def convert_to_morse(lst, words):
        """Accepts strings and returns morse_code"""
        for letters in words:
            if letters in morseCode.keys():
                lst.append((letters, morseCode[letters]))   # append as tuple

        return lst

    def convert_to_alpha(converted_code, lst):
        """Accepts morse_code and returns strings"""
        for codes in lst:
            for key, value in morseCode.items():
                if codes == value:
                    converted_code.append((value, key))

        return converted_code
