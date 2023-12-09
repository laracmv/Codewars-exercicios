def what_century(year):
    inicio = year[0:2]
    fim = year[2:4]
    if 0 < int(fim) < 100:
        seculo = int(inicio) + 1
    if fim == "00":
        seculo = int(inicio)
    
    seculo = str(seculo)
    if seculo[-1] == "1":
        seculo = seculo + "st"
    elif seculo[-1] =="2":
        seculo = seculo + "nd"
    elif seculo[-1] == "3":
        seculo = seculo + "rd"
    else:
        seculo = seculo + "th"
    return seculo
print(what_century("2154"))
