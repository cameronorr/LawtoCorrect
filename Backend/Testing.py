from spellchecker import *

spell = SpellChecker('en')


def add_word(new):
    # word is a list of words we wanna add
    spell.word_frequency.load_words(new)


def remove_word(old):
    # word is a list of words we wanna add
    spell.word_frequency.remove_words(old)


add_word(["TensorFlow", "doesn't"])

remove_word(["wee"])

string = "I thinnk thst wee foud a way that desn't require TensorFlow"
string = string.split()
print(string)

# find those words that may be misspelled
misspelled = spell.unknown(string)

for word in misspelled:
    # Get the one `most likely` answer
    print(spell.correction(word))

    # Get a list of `likely` options
    print(spell.candidates(word))

# This model only touches words that actually have typos, context isn't really factored in.
# Also the output is just the corrections, not the whole sentence.
