# Learnly
#### Video Demo:  <https://www.youtube.com/watch?v=b_zlyTmO52M>
#### Description:
    Learnly is inspired by Quizlet's Learning Mode, which makes learning terms and definitions a little easier and more fun! However, Quizlet now requires a subscription to use the learn mode. As a student, I don't want to have too many expensive subscriptions, and I haven't found a good free alternative, so I thought this project would be the perfect opportunity to make my own version.

    When starting Learnly, the user is presented with a description of the programme and how to navigate the menu. FIGlet was used to print the programme title and the different menu options to increase readability and ease of use. When the menu is displayed, the programme listens for a key to be pressed and acts before the user enters enter, using "getkey". If the key pressed does not match any of the menu options, the program will loop until it gets a match.

    If the user has not yet imported a CSV file with data, this can be done by pressing 'I' from the menu. The program will then check that the imported file exists and is correctly formatted.

    If the user presses 'L', the program will check that the user has imported a correct dataset and begin to test the user's knowledge of the definitions of the terms. If the user enters a correct definition at the first attempt, the next definition will be tested. However, if the input is incorrect, the user is given another try. If the input is too far off, the word is placed in a 'failed' list and is tested again when all the other words have been tested and a new term appears.

    Both the data and the words are separate classes. The word class consists of a word and a definition. The data handler class takes a filename when constructed and imports the words from that file if possible. The class has getters to return either a list of words, the file name, a list of terms or a list of definitions.

    To exit the programme, press 'E'.

    The requirements file lists all the required packages, one per line.