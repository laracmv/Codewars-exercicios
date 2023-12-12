# ENG - Given a string containing a list of integers separated by commas, write the function string_to_int_list(s) that takes said string and returns a new list containing all integers present in the string, preserving the order.
# For example, give the string "-1,2,3,4,5", the function string_to_int_list() should return [-1,2,3,4,5]
# Please note that there can be one or more consecutive commas whithout numbers, like so: "-1,-2,,,,,,3,4,5,,6"

# PORT - Dada uma string contendo uma lista de inteiros separados por vírgulas, escreva a função string_to_int_list(s) que pega a referida string e retorna uma nova lista contendo todos os inteiros presentes na string, preservando a ordem.
# Por exemplo, forneça a string "-1,2,3,4,5", a função string_to_int_list() deve retornar [-1,2,3,4,5]
# Observe que pode haver uma ou mais vírgulas consecutivas sem números, como: "-1,-2,,,,,,3,4,5,,6"

def string_to_int_list(s):
    s = s.split(",")
    contagem = s.count("")
    e = []
    i = 0
    while i < len(s):
        if s[i] == "":
            s.remove(s[i])
            i-=1
        else:
            e.append(int(s[i]))
        i+=1

    return e

print(string_to_int_list("1,2,,,,3,4,5"))
