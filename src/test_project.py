import pytest
from project.project import evaluate_answer, term_and_definition, check_file_format
from project.word import Word

def test_evaluate_answer():
    assert evaluate_answer("Frog", "Frog") == 100
    assert evaluate_answer("Frog", "Forg") == 75
    assert evaluate_answer("Fgro", "Frog") == 75
    assert evaluate_answer("grof", "Frog") == 50
    assert evaluate_answer("", "Frog") == 0
    assert evaluate_answer("bread", "Frog") == 22

def test_term_and_definition():
    word1 = Word("car", "vehicle")
    assert term_and_definition(word1, 6) == "Term: car      Definition: vehicle"
    word2 = Word("HOUSE", "BUILDING")
    assert term_and_definition(word2, 5) == "Term: HOUSE   Definition: BUILDING"
    word3 = Word(" ", "blank")
    assert term_and_definition(word3, 1) == "Term:     Definition: blank"
    with pytest.raises(ValueError):
        Word("", "should be an error here")
    with pytest.raises(ValueError):
        Word("should be error here too", "")

def test_check_file_format():
    assert check_file_format("hello.csv") == "hello.csv"
    with pytest.raises(ValueError):
        check_file_format("")
    with pytest.raises(SystemExit) as sample:
        check_file_format("hello hi.csv")
    with pytest.raises(SystemExit) as sample:
        check_file_format("words.jpg")
    with pytest.raises(SystemExit) as sample:
        check_file_format("terms_and_defs")
