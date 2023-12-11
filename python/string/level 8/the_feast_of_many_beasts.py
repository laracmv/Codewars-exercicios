# ENG - All of the animals are having a feast! Each animal is bringing one dish. There is just one rule: the dish must start and end with the same letters as the animal's name. For example, the great blue heron is bringing garlic naan and the chickadee is bringing chocolate cake.
# Write a function feast that takes the animal's name and dish as arguments and returns true or false to indicate whether the beast is allowed to bring the dish to the feast.
# Assume that beast and dish are always lowercase strings, and that each has at least two letters. beast and dish may contain hyphens and spaces, but these will not appear at the beginning or end of the string. They will not contain numerals.

# PORT - Todos os animais estão em festa! Cada animal traz um prato. A regra é apenas uma: o prato deve começar e terminar com as mesmas letras do nome do animal. Por exemplo, a garça azul está trazendo alho naan e o chapim está trazendo bolo de chocolate.
# Escreva uma função banquete que receba o nome e o prato do animal como argumentos e retorne verdadeiro ou falso para indicar se o animal tem permissão para trazer o prato para o banquete.
# Suponha que besta e prato sejam sempre strings minúsculas e que cada uma tenha pelo menos duas letras. besta e prato podem conter hífens e espaços, mas estes não aparecerão no início ou no final da string. Eles não conterão numerais.

def feast(beast, dish):
    beast = beast.split()
    dish = dish.split()
    if beast[0][0] == dish[0][0] and beast[-1][-1] == dish[-1][-1]:
        return True
    else:
        return False

print(feast("great blue heron", "garlic naan"))