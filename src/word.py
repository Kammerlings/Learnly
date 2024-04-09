class Word:
    def __init__(self, term: str, definition: str):
        if not term:
            raise ValueError("No term exists")
        else:
            self.term = term
        if not definition:
            raise ValueError("No definition exists")
        else:
            self.definition = definition

    def __str__(self):
        return self.term + self.definition

    @property
    def term(self):
        return self._term

    @property
    def definition(self):
        return self._definition

    @term.setter
    def term(self, term):
        self._term = term

    @definition.setter
    def definition(self, definition):
        self._definition = definition
