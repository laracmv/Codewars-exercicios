# ENG - You are given two strings (st1, st2) as inputs. Your task is to return a string containing the numbers in st2 which are not in str1. Make sure the numbers are returned in ascending order. All inputs will be a string of numbers.
# Here are some examples:
# findAdded('4455446', '447555446666'); // '56667'
# findAdded('44554466', '447554466'); // '7'

# PORT - Você recebe duas strings (st1, st2) como entradas. Sua tarefa é retornar uma string contendo os números em st2 que não estão em str1. Certifique-se de que os números sejam retornados em ordem crescente. Todas as entradas serão uma sequência de números.
# Aqui estão alguns exemplos:
# findAdded('4455446', '447555446666'); // '56667'
# findAdded('44554466', '447554466'); // '7'

def find_added(st1, st2):
    num = ""
    for num2 in st2:
        if num2 in st1:
            st1 = st1.replace(num2, "",1)
        else:
            num += num2

    num = list(num) #Transforma os numeros de st2 que nao estao em st1 em uma lista
    org = sorted(num) #organiza do menor para o maior
    org = "".join(org) #junta tudo em uma string
    return org

print(find_added('4455446', '447555446666'))
    
