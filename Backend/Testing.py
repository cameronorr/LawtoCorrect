# from spellchecker import *
#
# spell = SpellChecker('en')
# Elissa_dict = './dictionary.txt'
# spell.word_frequency.load_text_file(Elissa_dict, 'utf-8')
#
# dirty = open('./bad_words.txt', 'r', encoding='utf-8-sig')
# junk = dirty.read().splitlines()
# dirty.close()
# spell.word_frequency.remove_words(junk)


# def cleanse():
#     dirty = open('./bad_words.txt', 'r', encoding='utf-8-sig')
#     junk = dirty.read().splitlines()
#     dirty.close()
#     spell.word_frequency.remove_words(junk)
#
#
# # removes all words we don't want as corrections
#
# cleanse()


def old():
    current_string = open('./input.txt', 'r', encoding='utf-8-sig')
    string = current_string.read()
    print("original text: ", string)
    string = string.split()
    current_string.close()

    correct = ""
    for word in string:
        correct += str(spell.correction(word)) + " "

    print("corrected text: ", correct.strip())
    # find those words that may be misspelled
    misspelled = spell.unknown(string)

    for word in misspelled:
        # Get the one "most likely" answer
        print("misspelled: ", spell.correction(word))

        # Get a list of "likely" options
        # print(spell.candidates(word))

    # This model only touches words that actually have typos, context isn't really factored in.
    # Also the output is just the corrections, not the whole sentence.
    # There are other methods I gotta play with though.


# def new():
#     current_string = open('./input.txt', 'r+', encoding='utf-8-sig')
#     string = current_string.read()
#     current_string.truncate(0)
#     correct = spell.correction(string)
#     if len(string) != 0 and string != correct:
#         print(correct)
#         return correct
#     print("** Word Is Already Correct**")
#
#
# new()
