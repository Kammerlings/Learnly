import os, sys, random
from pyfiglet import Figlet
from project.data_handler import DataHandler
from getkey import getkey
from thefuzz import fuzz

def main():
    menu_text()
    data = None
    while True:
        data = menu_selection(getkey(), data)

def menu_text():
    # Clears the screen and presents menu
    os.system('clear')
    figlet = Figlet()
    figlet.setFont(font = "big")
    print(figlet.renderText("                                          Learnly"))
    print("                                     Coded by Fredrik Kämmerling from Motala, Sweden")
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("     Hi! Im Learnly, an alternative to Quizlet's learn function, which now is limited and costs money after 5 rounds.\n     I'm free and can be used for as namy rounds as you want.\n\n     To get started, choose between the options by pressing the corresponding key. ")
    figlet.setFont(font = "small")
    print(figlet.renderText("     I - IMPORT \n     L - LEARN \n     E - EXIT"))

def menu_selection(key, data):
    # Gets menu choice from user and executes the corresponding choice
    match key:
        case 'l':
            if data:
                learn_mode(data)
            else:
                print("Import words before entering learn-mode")
        case 'i':
            data = import_words()
            menu_text()
            return data
        case 'e':
            sys.exit()

def check_file_format(filename):
    # Checks the file format before sending it to the DataHandler constructor
    if not filename:
        raise ValueError("Must define filename")
    else:
        if len(filename.split()) > 1:
            sys.exit("Too many arguments")
        elif len(filename.split()) == 1 and filename.endswith(".csv"):
            return filename
        else:
            sys.exit("Not a CSV file")

def import_words():
    # Clears screen and promps the user for a file name containing terms and definitions
    os.system('clear')
    try:
        data = DataHandler(check_file_format(input("Type the name of the csv-file containing terms and definitions: ")))
    except EOFError:
        sys.exit("Input an CSV-file here")

    os.system('clear')
    print("Words imported:")
    spacing = len(max(data.terms, key = len))
    for word in data.words:
        print(term_and_definition(word, spacing))
    press_to_continue()
    return data

def term_and_definition(word, spacing):
    # Prints the term and its definition
    return ("Term: " + word.term + " " * (spacing - len(word.term)) + "   Definition: " + word.definition)

def learn(term_list: list) -> list:
    # Test users knowledge of the terms in "term_list" and returns the words the user got wrong.
    # In this case, the definition of wrong is words that gets less tahn 70 from the fuzz ratio.
    figlet = Figlet()
    failed_terms = []

    for term in term_list:
        print("Type the definition for: ")
        figlet.setFont(font = "small")
        print(figlet.renderText(term.term))

        while True:
            score = 0
            user_input = input("Answer: ").strip()
            score = evaluate_answer(user_input, term.definition)
            if score == 100:
                print("Good job!")
                break
            elif 70 < score < 100:
                print("You almost got it! Try again!")
            else:
                print("That was not correct, the answer is \"" + term.definition + "\". You will get a new chance later.")
                failed_terms.append(term)
                break

        press_to_continue()
        os.system('clear')
    return failed_terms

def evaluate_answer(user_input, definition):
    # Evaluates how similar the user input and the correct definition are.
    # Returns a score from 0 to 100
    return fuzz.ratio(user_input, definition)

def learn_mode(data):
    # Runs until all the user knows all the words
    os.system('clear')
    random.shuffle(data.words)
    mistakes = learn(data.words)

    if len(mistakes) > 0:
        keep_going()
        os.system('clear')
        while len(mistakes) > 0:
            mistakes = learn(mistakes)

    you_made_it()

def you_made_it():
    # Prints out Hooray with FIGlet
    os.system('clear')
    figlet = Figlet()
    figlet.setFont(font = "big")
    print(figlet.renderText("                                         Hooray!"))
    sys.exit("                                              You got all the words right!")

def keep_going():
    # Prints out Keep going! with FIGlet
    os.system('clear')
    figlet = Figlet()
    figlet.setFont(font = "big")
    print(figlet.renderText("                            Keep going!"))
    print("Alright! That was all of the words, let's revisit the terms you got wrong.")
    press_to_continue()

def press_to_continue():
    # Waits until the user presses a key
    while True:
        print("Press any key to continue.")
        getkey()
        break

if __name__ == "__main__":
    main()