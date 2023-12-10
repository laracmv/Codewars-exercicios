# ENG - An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# PORT - Um isograma é uma palavra que não possui letras repetidas, consecutivas ou não consecutivas. Implemente uma função que determine se uma string que contém apenas letras é um isograma. Suponha que a string vazia seja um isograma. Ignore letras maiúsculas e minúsculas.

#---Mine solution/ Minha solução
def is_isogram(string):
    word = {}
    for char in string:
        if char.lower() not in word:
            word[char.lower()] = 1
        else:
            word[char.lower()] +=1
            
    for item in word.values():
        if item >1:
            return False
    i = 0
    while i <len(string) - 1:
        if string[i].lower() == string[i + 1].lower():
            return False 
        i+=1
    return True
print(is_isogram("NKItWEPTlVOBfJHT"))

#---Codewars solution / Solução do Codewars
def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: return False
    return True
