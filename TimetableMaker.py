
def possibleClasses(dataArray, semestre, classesId):
    result = []
    for aula in dataArray:
        if aula.semestre == semestre and aula.aulaId in classesId:
            result.append(aula)
    return result

def splitClasses(classArray):
    print(classArray)