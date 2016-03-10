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
    validCombinations = []
    for aula in dictionary:
        allClasses = []
        numberOfClassTypes = 0
        for tipo in dictionary[aula]:
            numberOfClassTypes += 1
            for turma in dictionary[aula][tipo]:
                allClasses.append((aula, tipo, turma))

        allClassCombinations = combinations(allClasses, numberOfClassTypes)

        #Remove all combinations that do not have every class type
        for comb in allClassCombinations:
            types = []
            for turma in comb:
                if turma[1] not in types:
                    types.append(turma[1])
            if len(types) == numberOfClassTypes:
                validCombinations.append(comb)
    return validCombinations
