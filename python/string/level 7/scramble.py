# ENG - Given a string and an array of index numbers, return the characters of the string rearranged to be in the order specified by the accompanying array.
# Ex:
# scramble('abcd', [0,3,1,2]) -> 'acdb'
# The string that you will be returning back will have: 'a' at index 0, 'b' at index 3, 'c' at index 1, 'd' at index 2, because the order of those characters maps to their corresponding numbers in the index array.
# In other words, put the first character in the string at the index described by the first element of the array
# You can assume that you will be given a string and array of equal length and both containing valid characters (A-Z, a-z, or 0-9).

# PORT - Dada uma string e uma array de números de índice, retorne os caracteres da string reorganizados para estarem na ordem especificada pela array que a acompanha.
# Ex:
# 'abcd', [0,3,1,2]-> 'acdb'
# A string que você retornará terá: 'a' no índice 0, 'b' no índice 3, 'c' no índice 1, 'd' no índice 2, porque a ordem desses caracteres mapeia para seus números correspondentes na matriz de índice.
# Em outras palavras, coloque o primeiro caractere da string no índice descrito pelo primeiro elemento do array
# Você pode assumir que receberá uma string e uma array de comprimento igual e ambas contendo caracteres válidos (A-Z, a-z ou 0-9).

def scramble(strng, array):
    new = len(strng) * "x"
    n = []
    for i in range(len(new)):
        n.append(new[i])

    for i in range(len(strng)):
        elemento = strng[i]
        novoindice = array[i]
        n[novoindice] = elemento
    n = ''.join(n)

    return n

print(scramble('sc301s', [4,0,3,1,5,2]))
