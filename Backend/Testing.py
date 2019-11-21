from spellchecker import *

spell = SpellChecker('en')  # English language

Elissa_dict = './dictionary.txt'
spell.word_frequency.load_text_file(Elissa_dict, 'utf-8')  # txt file containing correct words we want added


def cleanse():
    dirty = open('./bad_words.txt', 'r')
    for dirt in dirty:
        spell.word_frequency.remove(dirt)  # removes all words we don't want as corrections
    dirty.close()


cleanse()

string = "I thnk I jus foun a way to do this entire thhing wittout any TensorFlow and I does't evn try"
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
# There are other methods I gotta play with though.
