from itertools import combinations

#Takes in dictionary of structure:
# { CLASS_ID:{
#       T:{
#           CLASS_T1,
#           CLASS_T...
#       },
#       TP:{
#           CLASS_TP...
#       },
#       ...
#   }, ...
# }

# Returns array of all possible class combinations
# Refers to elements in dictionary as tuples; (key, subKey, subSubKey)
# Make it work first, optimize later.
def possibleCombinations(dictionary):
    # Combinacoes de turmas validos (todos os tipos presentes)
    # Para cada aula, i.e., e necessario fazer combinacao de turmas
    combTurmasValidas = []

    aulas = []  # List de todas as aulas por numero

    #Fazer combinacoes dentro de cada aula
    for aula in dictionary:
        turmas = [] # List de de todas as turmas nesta aula (disciplina), como tuple
        tipos = []  # Tipos de aula (T/TP/PL)

        for tipo in dictionary[aula]:
            tipos.append(tipo)
            for turma in dictionary[aula][tipo]:
                turmas.append((aula, tipo, turma))

        combTurmas = combinations(turmas, len(tipos))   # Todas as combinacoes possiveis, incluindo (TP,TP,TP,TP)

        for comb in combTurmas:
            tiposNaComb = []    # Quais os tipos de aula nesta combinacao; deverao ser todos
            for turma in comb:
                tipo = turma[1] # Cada turma é representada por uma tuple (aula, tipo, turma); turma[1] devolve tipo

                if tipo not in tiposNaComb:
                    tiposNaComb.append(tipo)

            #Se a combinacao possuir todos os tipos de aula e valida
            if set(tiposNaComb) == set(tipos):
                combTurmasValidas.append(comb)

        aulas.append(aula)

    # Fazer combinacoes de aulas, tendo em conta combinacoes "legais" de turmas
    # Pelo mesmo processo que para as aulas:
    # Fazer todas as combinacoes possiveis e remover as que nao incluirem todas as aulas
    combAulas = combinations(combTurmasValidas, len(aulas))

    combAulasValidas = []   # Combinacoes de turmas com todas as aulas

    for comb in combAulas:
        aulasInComb = []    # List de aulas incluidas nesta combinacao; deverao ser todas
        for turmaComb in comb:  # Combinacao de turmas para uma aula; tira-se o id da aula pelo primeiro elemento
            if turmaComb[0][0] not in aulasInComb:
                aulasInComb.append(turmaComb[0][0])    # comb[0] == (aula, tipo, turma); tuple[0] == aula

        if set(aulasInComb) == set(aulas):
            combAulasValidas.append(comb)   # Se esta combinacao de turmas possuir todas as aulas, e valida

    return combAulasValidas
