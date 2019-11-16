def definitions():
    def ML(stuff):
        # most likely word
        pass

    def word():
        # current word
        pass

    def sentence():
        # full sentence
        pass

# Wait for punctuation (. ! ?)

def main_loop():
    substring = word()
    string = sentence()

    output = ML(substring)

    conc = string + output

    result = ML(conc)

    # Checks if the word typed is spelled correctly
    def checker(test, answer):
        if test == answer:
            pass
        else:
            return answer

def correction():
    # Go back one space
    # display (string + substring)
    # clear (string + substring)
    pass
