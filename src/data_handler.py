import sys, csv
from project.word import Word

class DataHandler:
    def __init__(self, filename):
        temp = []
        try:
            with open(filename) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    temp.append(Word(row["term"], row["definition"]))
                self.words = temp
        except FileNotFoundError:
            sys.exit("Could not read file")
        except KeyError:
            sys.exit("File must start with \"term,definition\"")


    @property
    def terms(self):
        temp = []
        for word in self.words:
            temp.append(word.term)
        return temp

    @property
    def definitions(self):
        temp = []
        for word in self.words:
            temp.append(word.definition)
        return temp

    @property
    def filename(self):
        return self._filename

    @property
    def words(self):
        return self._words

    @filename.setter
    def filename(self, filename):
        self._filename = filename

    @words.setter
    def words(self, words):
        self._words = words
