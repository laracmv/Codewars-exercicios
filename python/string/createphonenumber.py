# ENG: Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

# PORT: Escreva uma função que aceite um array de 10 números inteiros (entre 0 e 9), que retorne uma string desses números na forma de um número de telefone.

def create_phone_number(n):
    string = "(XXX) XXX-XXXX"
    for numero in n:
        numero = str(numero)
        string = string.replace("X", numero,1)
    return string

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))