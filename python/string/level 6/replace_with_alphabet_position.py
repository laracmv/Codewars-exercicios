# ENG - In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.

# PORT - Neste kata você deve, dada uma string, substituir cada letra pela sua posição no alfabeto.
# Se alguma coisa no texto não for uma letra, ignore e não devolva.
# "a" = 1, "b" = 2, etc.


def alphabet_position(text):
    text = text.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    position = ""
    for letter in text:
        if letter in alphabet:
            position += str(alphabet.index(letter) + 1) + " "

    position = position.strip()
        
    return position

print(alphabet_position("The sunset sets at twelve o' clock."))  


