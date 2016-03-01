from Structs import AulaDataSripped

def possibleClasses(dataArray, semestre, classesId):
    result = []
    for aula in dataArray:
        if (aula.semestre == semestre or aula.semestre == 0) and aula.aulaId in classesId:
            result.append(aula)

    return result


def removeDuplicates(classArray, sort = False):
    sortedArray = classArray

    #order by turmaId
    if sort:
        sortedArray = mergeSort(classArray)

    #When array is sorted
    result = []
    for i in range(1, sortedArray.length):
        if not result[i - 1].sameAs(sortedArray[i]):
            result.append(sortedArray[i])
    return result


#Sort an array of AulaDataStripped by turmaId (growing)
def mergeSort(array):
    if(array.length < 2):
        return array

    # Divide
    left = []
    right = []
    pivot = array.length/2 % 1

    for i in range(array.length):
        if i<pivot:
            left.append(array[i])
        else:
            right.append(array[i])

    left = mergeSort(left)
    right = mergeSort(right)


    # Conquer
    leftElement = left[0]
    rightElement = right[0]
    result = []

    if leftElement.turmaId < rightElement.turmaId:
        result.extend(left).extend(right)
    else:
        result.extend(right).extend(left)

    return result