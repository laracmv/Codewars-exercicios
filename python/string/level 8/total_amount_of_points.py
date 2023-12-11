# ENG - Our football team has finished the championship.
# Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.
# For example: ["3:1", "2:2", "0:1", ...]
# Points are awarded for each match as follows:
# if x > y: 3 points (win)
# if x < y: 0 points (loss)
# if x = y: 1 point (tie)
# We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.
# Notes:
# our team always plays 10 matches in the championship
# 0 <= x <= 4
# 0 <= y <= 4

# PORT - Nosso time de futebol terminou o campeonato.
# Os resultados dos jogos da nossa equipe são registrados em uma coleção de strings. Cada partida é representada por uma string no formato "x:y", onde x é a pontuação do nosso time e y é a pontuação do nosso adversário.
# Por exemplo: ["3:1", "2:2", "0:1", ...]
# Os pontos são concedidos para cada partida da seguinte forma:
# se x > y: 3 pontos (vitória)
# se x < y: 0 pontos (perda)
# se x = y: 1 ponto (empate)
# Precisamos escrever uma função que pegue essa coleção e retorne a quantidade de pontos que nosso time (x) obteve no campeonato pelas regras fornecidas acima.
# Notas:
# nosso time sempre joga 10 partidas no campeonato
# 0 <= x <= 4
# 0 <= y <= 4

def points(games):
    pontos = 0
    for i in range(10):
        home = games[i][0]
        visitant = games[i][2]

        if home > visitant:
            pontos +=3
        if home < visitant:
            pontos += 0
        if home == visitant:
            pontos += 1
        
    return pontos

print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))