# Noone needs this
def a_an(word):
    if word[0] in "aeiouAEIOU":
        return "an"
    else:
        return "a"
