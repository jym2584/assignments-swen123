from practice14_1 import *

def test_pig_latin_translator():
    #setup
    word = "bagel"
    word2 = "smile"
    word3 = "apple"
    word4 = "egg"
    #invoke
    translated = pig_latin_translator(word)
    translated2 = pig_latin_translator(word2)
    translated3 = pig_latin_translator(word3)
    translated4 = pig_latin_translator(word4)
    #assert
    assert translated == "agelbay"
    assert translated2 == "ilesmay"
    assert translated3 == "appleay"
    assert translated4 == "eggay"