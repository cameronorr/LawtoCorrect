from spellchecker import *

spell = SpellChecker('en')
# English language spellchecker

Elissa_dict = './dictionary.txt'
spell.word_frequency.load_text_file(Elissa_dict, 'utf-8')
# txt file containing "new" corrections


def cleanse():
    dirty = open('./bad_words.txt', 'r', encoding='utf-8-sig')
    junk = dirty.read().splitlines()
    dirty.close()
    spell.word_frequency.remove_words(junk)
# removes all words we don't want as corrections


cleanse()

current_string = open('./input.txt', 'r', encoding='utf-8-sig')
string = current_string.read().split()
current_string.close()
print(string)

# find those words that may be misspelled
misspelled = spell.unknown(string)

for word in misspelled:
    # Get the one "most likely" answer
    print(spell.correction(word))

    # Get a list of "likely" options
    print(spell.candidates(word))

# This model only touches words that actually have typos, context isn't really factored in.
# Also the output is just the corrections, not the whole sentence.
# There are other methods I gotta play with though.
