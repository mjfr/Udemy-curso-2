# TODO - 1: Make a Text to Morse Code converter (using command line to get inputs)
# This is the first portfolio project from the course.
# My initial thoughts are: using a dictionary to hold the letters as key and morse as values
# Use a try block to handle the possible exceptions
# Use a loop to go through each letter and convert them

# Using playsound 1.2.2 because 1.3.0 will throw lots of exceptions and will not play the file
from playsound import playsound
from time import sleep

letter_morse_dict = {
    "á": ".-",
    "à": ".-",
    "ã": ".-",
    "â": ".-",
    "ä": ".-",
    "a": ".-",
    "b": "-...",
    "ç": "-.-.",
    "c": "-.-.",
    "d": "-..",
    "é": ".",
    "è": ".",
    "ê": ".",
    "ë": ".",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "í": "..",
    "ì": "..",
    "î": "..",
    "ï": "..",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "ñ": "-.",
    "n": "-.",
    "ó": "---",
    "ò": "---",
    "õ": "---",
    "ô": "---",
    "ö": "---",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "ú": "..-",
    "ù": "..-",
    "û": "..-",
    "ü": "..-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "ý": "-.--",
    "ÿ": "-.--",
    "y": "-.--",
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


def listen_to_morse(morse):
    for sign in morse:
        if sign == ".":
            playsound("dot.mp3")
        elif sign == "-":
            playsound("dash.mp3")
        elif sign == " ":
            sleep(0.3)
        elif sign == "||":
            sleep(0.5)
    return ""


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
    print(f"Playing morse:\n{converted_text.strip()}")
    return listen_to_morse(converted_text)


def morse_to_text():
    morse_input = input("Type your morse code to be converted to text:\nSpaces shall be ||, do not use other symbols\n")
    morse_list = morse_input.split()
    converted_morse = ""
    while True:
        try:
            while len(morse_list) > 0:
                current_morse = morse_list.pop(0)
                text = {k: v for (v, k) in letter_morse_dict.items()}
                converted_morse += f"{text[current_morse]}"
            break
        except ValueError:
            print("Type a valid morse code.")
    return converted_morse.strip()


select_function = {"1": text_to_morse, "2": morse_to_text}
while True:
    try:
        choice = input("Type 1 to encode your text to morse code\nType 2 to decode your morse code to text\n"
                       "Type 3 to exit\nOption: ")
        if choice == "3":
            print("Exiting...")
            break
        print(select_function[choice]())
    except KeyError:
        print("Use only the valid options")
