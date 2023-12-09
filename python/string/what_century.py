# ENG - Return the century of the input year. The input will always be a 4 digit string, so there is no need for validation.

# PORT - Retorne o século do ano de entrada. A entrada será sempre uma string de 4 dígitos, portanto não há necessidade de validação.

def what_century(year):
    inicio = year[0:2]
    fim = year[2:4]
    if 0 < int(fim) < 100:
        seculo = int(inicio) + 1
    if fim == "00":
        seculo = int(inicio)
    
    seculo = str(seculo)
    if seculo[-1] == "1" and seculo[0] != "1":
        seculo = seculo + "st"
    elif seculo[-1] =="2" and seculo[0] != "1":
        seculo = seculo + "nd"
    elif seculo[-1] == "3" and seculo[0] != "1":
        seculo = seculo + "rd"
    else:
        seculo = seculo + "th"
    return seculo
print(what_century("1234"))



