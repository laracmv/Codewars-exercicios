#ENG - Given a string, return if a given letter always appears immediately before another given letter.

#PORT - Dada uma string, retorne se uma determinada letra sempre aparecer imediatamente antes de outra letra.

#---Mine Solution/ Minha solução
def best_friend(txt, a, b):
    i = 0 
    while i < len(txt):
        if txt[i] == a:
            #verifica se a a letra "a" é o ultimo elemento, se for nao tem como ter "b" como posterior
            if txt[i] == a and i == len(txt)-1:
                return False
           
            if txt[i] == a and txt[i+1] != b:
                return False
            #verifica se a e b são iguais, se forem "a" jamais será anterior a "b"
            if txt[i] == a and txt[i] == txt[i+1]:
                return False
        i+=1
    return True
print(best_friend("a test", "t", "e"))

#---Solution Codewars/ Solução Codewars

def best_friend(t,a,b):
 return t.count(a)==t.count(a+b)
