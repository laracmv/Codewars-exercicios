# ENG - Don Drumphet lives in a nice neighborhood, but one of his neighbors has started to let his house go. Don Drumphet wants to build a wall between his house and his neighbor’s, and is trying to get the neighborhood association to pay for it. He begins to solicit his neighbors to petition to get the association to build the wall. Unfortunately for Don Drumphet, he cannot read very well, has a very limited attention span, and can only remember two letters from each of his neighbors’ names. As he collects signatures, he insists that his neighbors keep truncating their names until two letters remain, and he can finally read them.
# Your code will show Full name of the neighbor and the truncated version of the name as an array. If the number of the characters in name is less than or equal to two, it will return an array containing only the name as is"

# PORT - Don Drumphet mora em um bairro agradável, mas um de seus vizinhos começou a alugar sua casa. Don Drumphet quer construir um muro entre a sua casa e a do vizinho e está a tentar fazer com que a associação de moradores pague por isso. Ele começa a solicitar a seus vizinhos que façam uma petição para que a associação construa o muro. Infelizmente para Don Drumphet, ele não consegue ler muito bem, tem uma capacidade de atenção muito limitada e só consegue lembrar duas letras do nome de cada um dos seus vizinhos. Enquanto coleta assinaturas, ele insiste que seus vizinhos continuem truncando seus nomes até que restem duas letras e ele possa finalmente lê-las.
# Seu código mostrará o nome completo do vizinho e a versão truncada do nome como um array. Se o número de caracteres no nome for menor ou igual a dois, retornará um array contendo apenas o nome como está"

def who_is_paying(name):
    if len(name) < 3:
        return [name]
    else:
        truncated = name[0:2]
        return [name, truncated]