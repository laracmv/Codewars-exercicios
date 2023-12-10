# ENG - Your task is to create a function that takes a string of two words, separated by a space and returns a spoonerism of those words in a string, as in the example "not picking" --> "pot nicking". A "word" in the context of this kata can contain any of the letters A through Z in upper or lower case, and the numbers 0 to 9. Though spoonerisms are about letters in words in the domain of written and spoken language, numbers are included in the inputs for the random test cases and they require no special treatment.

# PORT - Sua tarefa é criar uma função que pegue uma string de duas palavras, separadas por um espaçoe retorne um conjunto dessas palavras em uma string, como no exemplo "not picking" --> "pot nicking".Uma "palavra" no contexto deste kata pode conter qualquer uma das letras de A a Z em maiúsculas ou minúsculas e os números de 0 a 9. Embora os colheres sejam sobre letras em palavras no domínio da linguagem escrita e falada, os números são incluídos nas entradas para os casos de teste aleatórios e não requerem tratamento especial.

def spoonerize(words):
    lista = words.split()
    novalista = []
    i = 0
    f = 1
    for palavra in lista:
        novalista.append(lista[f][0] + lista[i][1:])
        i+=1
        f-=1

    palavra = " ".join(novalista)
    return palavra

print(spoonerize("pot nicking"))