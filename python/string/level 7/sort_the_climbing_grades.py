# ENG - In rock climbing (bouldering specifically), the V/Vermin (USA) climbing grades start at 'VB' (the easiest grade), and then go 'V0', 'V0+', 'V1', 'V2', 'V3', 'V4', 'V5' etc. up to 'V17' (the hardest grade). You will be given a list (lst) of climbing grades and you have to write a function (sort_grades) to return a list of the grades sorted easiest to hardest.
# If the input is an empty list, return an empty list; otherwise the input will always be a valid list of one or more grades.

# PORT - Na escalada em rocha (especificamente no boulder), os graus de escalada V/Vermin (EUA) começam em 'VB' (o grau mais fácil) e depois vão para 'V0', 'V0+', 'V1', 'V2', 'V3' , 'V4', 'V5' etc. até 'V17' (a nota mais difícil). Você receberá uma lista (lst) de notas de escalada e deverá escrever uma função (sort_grades) para retornar uma lista das notas classificadas do mais fácil ao mais difícil.
# Se a entrada for uma lista vazia, retorne uma lista vazia; caso contrário, a entrada será sempre uma lista válida de uma ou mais notas.



def sort_grades(lst):
    grades = ['VB', 'V0', 'V0+'] 
    for i in range(1,18): 
        grades.append(f"V{i}")

    final = []
    for i in grades:
        if i in lst:
            final.append(i)
    return final

print(sort_grades(['V7', 'V12', 'V1']))