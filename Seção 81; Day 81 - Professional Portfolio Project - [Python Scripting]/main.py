# TODO - 1: Make a Text to Morse Code converter (using command line to get inputs)
# This is the first portfolio project from the course.
# My initial thoughts are: using a dictionary to hold the letters as key and morse as values
# Use a try block to handle the possible exceptions
# Use a loop to go through each letter and convert them

letter_morse_dict = {
    "a": ".-",
    "á": ".-",
    "à": ".-",
    "ã": ".-",
    "â": ".-",
    "ä": ".-",
    "b": "-...",
    "c": "-.-.",
    "ç": "-.-.",
    "d": "-..",
    "e": ".",
    "é": ".",
    "è": ".",
    "ê": ".",
    "ë": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "í": "..",
    "ì": "..",
    "î": "..",
    "ï": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "ñ": "-.",
    "o": "---",
    "ó": "---",
    "ò": "---",
    "õ": "---",
    "ô": "---",
    "ö": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "ú": "..-",
    "ù": "..-",
    "û": "..-",
    "ü": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "ý": "-.--",
    "ÿ": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    '"': ".-..-.",
    "$": "...-..-",
    "@": ".--.-.",
    " ": "||",
}


def text_to_morse():
    text_input = input("Type something to convert it to morse: ")
    text_list = [letter for letter in text_input.lower()]
    converted_text = ""
    while True:
        try:
            while len(text_list) > 0:
                current_letter = text_list.pop(0)
                morse = current_letter.replace(current_letter, letter_morse_dict[current_letter])
                converted_text += f"{morse} "
            break
        except KeyError:
            print(
                f'"{current_letter}" is not recognized in morse code. Try using letters without accents and/or symbols'
                'that are recognized.')
            converted_text += f"{current_letter} "
    return converted_text.strip()


def morse_to_text():
    morse_input = input("Type your morse code to be converted to text:\nSpaces shall be ||, do not use other symbols\n")
    morse_list = morse_input.split()
    converted_morse = ""
    while True:
        try:
            while len(morse_list) > 0:
                current_morse = morse_list.pop(0)
                text = current_morse.replace(current_morse, list(letter_morse_dict.keys())[
                    list(letter_morse_dict.values()).index(current_morse)])
                converted_morse += f"{text}"
            break
        except ValueError:
            print("Type a valid morse code.")
    return converted_morse.strip()


select_function = {"1": text_to_morse, "2": morse_to_text}
while True:
    choice = ""
    try:
        choice = input("Type 1 to encode your text to morse code\nType 2 to decode your morse code to text\n"
                       "Type 3 to exit\nOption: ")
        if choice == "3":
            print("Exiting...")
            break
    except KeyError:
        print("Use only the valid options")
    print(select_function[choice]())
