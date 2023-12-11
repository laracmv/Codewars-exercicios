# ENG - Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

#PORT - Dada uma string indicando um intervalo de letras, retorne uma string que inclua todas as letras desse intervalo, incluindo a última letra. Observe que se o intervalo for fornecido em letras maiúsculas, retorne a string também em maiúsculas!

def gimme_the_letters(sp):
    alfa = "abcdefghijklmnopqrstuvwxyz"
    alfabig = alfa.upper()

    first=  sp[0]
    last = sp[2]
    new = ""
    if first in alfa:
        pos1 = alfa.index(first)
        pos2 = alfa.index(last)
        new = alfa[pos1:pos2+1]
        for i in range(pos1, pos2 + 1):
            new += alfa[i]
    else:
        pos1 = alfabig.index(first)
        pos2 = alfabig.index(last)
        for i in range(pos1, pos2 + 1):
            new += alfabig[i]

    return new

print(gimme_the_letters("A-E"))