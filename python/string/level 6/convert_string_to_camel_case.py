# ENG - Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

# PORT - Faça uma função para que ele converta palavras delimitadas por traço/sublinhado em "camel casing". A primeira palavra na saída deve ser maiúscula apenas se a palavra original estiver em maiúscula (conhecida como Upper Camel Case, também conhecida como Pascal case). As próximas palavras devem ser sempre maiúsculas.

#----Solution 1/ Solução 1
import re
def to_camel_case(text):
    i = 0 
    lista = re.split(r'[-_]', text)
    #r = "regular", diz pro python usar a string exatamente com ela
    # o [...] serve para realizar o split com os itens dentro dele

    for f in range(len(lista)):
        if f > 0:
            lista[f] = lista[f].capitalize()

    lista= "".join(lista)
    return lista
print(to_camel_case('a-pippi-Is_pippi'))

#-----Solution 2 / Solução 2
def to_camel_case(text):
    especial = "-_"
    lista = []
    c = ""
    for char in text:
        if char in especial:
            if c:
                lista.append(c)
                c = ""
        else:
            c += char
    if c:
        lista.append(c)

    i = 1
    while i < len(lista):
        lista[i] = lista[i].capitalize()
        i+=1
    lista = "".join(lista)

    return lista

print(to_camel_case('a-pippi-Is_pippi'))