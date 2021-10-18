from scrabble import validate_word, score_word, score_word_timed

def test_special_chars_1():
    assert validate_word('abc!', 4) == False

def test_special_chars_space():
    assert validate_word('a  c', 4) == False

def test_dictionary():
    assert validate_word('abc', 3) == False

def test_dictionary_2():
    assert validate_word('car', 3) == True

def test_dictionary_3():
    assert validate_word('testing', 7) == True

def test_score_word_1():
    assert score_word('car') == 5

def test_score_word_2():
    assert score_word('market') == 12

def test_score_word_3():
    assert score_word('cabbage') == 14

def test_score_word_4():
    assert score_word('zebra') == 16

def test_score_word_5():
    assert score_word('justice') == 16

def test_score_word_6():
    assert score_word('quiz') == 22

def test_score_word_7():
    assert score_word('formula') == 12

def test_timed_score_1():
    assert score_word_timed(10, 12) == 8

def test_timed_score_2():
    assert score_word_timed(10, 0) == 0

def test_timed_score_3():
    assert score_word_timed(20, 5) == 6