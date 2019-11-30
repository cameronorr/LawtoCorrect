from spellchecker import *

spell = SpellChecker('en')
Elissa_dict = './dictionary.txt'
spell.word_frequency.load_text_file(Elissa_dict, 'utf-8')

dirty = open('./bad_words.txt', 'r', encoding='utf-8-sig')
junk = dirty.read().splitlines()
dirty.close()
spell.word_frequency.remove_words(junk)


def new():
    current_string = open('./input.txt', 'r+', encoding='utf-8-sig')
    string = current_string.read()
    current_string.truncate(0)
    correct = spell.correction(string)
    if len(string) != 0 and string != correct:
        print(correct)
        return correct
    print("** Word Is Already Correct**")
