# You're hanging out with your friends in a bar, when suddenly one of them is so drunk, that he can't speak, and when he wants to say something, he writes it down on a paper. However, none of the words he writes make sense to you. He wants to help you, so he points at a beer and writes "yvvi". You start to understand what he's trying to say, and you write a script, that decodes his words.

# Keep in mind that numbers, as well as other characters, can be part of the input, and you should keep them like they are. You should also test if the input is a string. If it is not, return "Input is not a string".

# Você está com seus amigos em um bar, quando de repente um deles está tão bêbado que não consegue falar e, quando quer dizer alguma coisa, escreve em um papel. No entanto, nenhuma das palavras que ele escreve faz sentido para você. Ele quer te ajudar, então aponta para uma cerveja e escreve “yvvi”. Você começa a entender o que ele está tentando dizer e escreve um roteiro que decodifica suas palavras.

# Lembre-se de que números, assim como outros caracteres, podem fazer parte da entrada e você deve mantê-los como estão. Você também deve testar se a entrada é uma string. Caso contrário, retorne "A entrada não é uma string".

def decode(string_):
    if type(string_) != str:
        return "Input is not a string"
    else: 
        alfabetosmall = "abcdefghijklmnopqrstuvwxyz"
        alfabetobig= alfabetosmall.upper()
        traducao = ""
        for letra in string_:
            if letra in alfabetosmall:
                posicao = alfabetosmall.index(letra)
                #Obs: a letra codificada está na posicao oposta com relação ao alfabeto
                novaposicao = len(alfabetosmall) - 1 - posicao
                traducao += alfabetosmall[novaposicao]
            elif letra in alfabetobig:
                posicao = alfabetobig.index(letra)
                novaposicao = len(alfabetobig) - 1 - posicao
                traducao += alfabetobig[novaposicao]
            else:
                traducao += letra
        return traducao

print(decode("Yvvi 10"))
