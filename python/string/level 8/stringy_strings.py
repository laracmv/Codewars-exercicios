# ENG - Write me a function stringy that takes a size and returns a string of alternating 1s and 0s. The string should start with a 1. A string with size 6 should return :'101010'.The size will always be positive and will only use whole numbers.

# PORT - Escreva-me uma função stringy que tenha um tamanho e retorne uma sequência de 1s e 0s alternados. A string deve começar com 1. Uma string com tamanho 6 deve retornar: '101010'. O tamanho será sempre positivo e usará apenas números inteiros.

def stringy(size):
    i = 0
    string = ""
    while i < size:
        if i == 0 or i%2 == 0:
            string +="1"
        else:
            string += "0"
        i+=1
    return string
print(stringy(3))

