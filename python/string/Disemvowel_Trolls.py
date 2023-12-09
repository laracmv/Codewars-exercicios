# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.

# Trolls estão atacando sua seção de comentários!
# Uma forma comum de lidar com essa situação é remover todas as vogais dos comentários dos trolls, neutralizando a ameaça.
# Sua tarefa é escrever uma função que receba uma string e retorne uma nova string com todas as vogais removidas.

def disemvowel(string_):
    novastring = ""
    vogal = "aeiouAEIOU"

    for letra in string_:
        if letra not in vogal:
            novastring += letra

    return novastring

print(disemvowel("This website is for losers LOL!"))