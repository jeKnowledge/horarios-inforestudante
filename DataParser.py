import csv
import datetime
import re
from Structs import AulaDataRaw
from Structs import AulaDataSripped


def openFile(filePath):
    return open(filePath)

def csvIntoRawArray(csvFile):
    # Array of arrays(lines) with data
    filereader = csv.reader(csvFile)

    # We will be returning an array of AulaDataRaw
    # each corresponding to a line

    aulaDataRawArray = []
    for row in filereader:
        # Skip labels row
        try:
            int(row[0])
        except ValueError:
            continue

        aulaDataRawArray.append(AulaDataRaw(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

    return aulaDataRawArray


def rawArrayToStrippedArray(rawArray):
    result = []
    for raw in rawArray:
        # Skip label
        if raw.aulaId == "FE_ID":
            continue

        result.append(rawToStripped(raw))

    return result


# Converts from Structs.AulaDataRaw to Stucts.AulaDataStripped
def rawToStripped(dataRaw):
    # Semestre:
    # 1, 2 ou Anual (0)
    if dataRaw.semestre == "Anual":
        semestre = 0
    else:
        semestre = int(dataRaw.semestre[0]) # 1o caractere (1/2)

    aulaCodigo = int(dataRaw.aulaId)
    turmaId = int(dataRaw.turmaId)
    dia = dmytimeToDayOfWeek(dataRaw.dataInicio)
    horaInicio = dmytimeToTime(dataRaw.dataInicio)
    horaFim = dmytimeToTime(dataRaw.dataFim)
    turma = dataRaw.turma
    tipo = getClassType(dataRaw.turma)

    return AulaDataSripped(aulaCodigo, semestre, turmaId, dia, horaInicio, horaFim, turma, tipo)

# "10-JAN-2015 20:30:12" -> 203012
def dmytimeToTime(timeString):
    timeStr = re.search("\d\d:\d\d:\d\d", timeString).group(0).replace(":", "")
    return int(timeStr)


# Monday -> 0
# Sunday -> 6
def dmytimeToDayOfWeek(timeString):
    day = int(re.search("\d\d(?=-\w\w\w-\d\d\d\d)", timeString).group(0))
    monthStr = re.search("(?<=\d\d-)\w\w\w(?=-\d\d\d\d)", timeString).group(0)
    month = monthStrToNumber(monthStr)
    year = int(re.search("(?<=\d\d-\w\w\w-)\d\d\d\d", timeString).group(0))

    return datetime.datetime(year, month, day).weekday()


# Converts JAN -> 1
#          FEB -> 2 ...
def monthStrToNumber(monthString):
    upperString = str(monthString).upper()

    # Oh, no switch statements. Of course.
    us = upperString
    if us == "JAN":
        return 1
    if us == "FEV" or us == "FEB":
        return 2
    if us == "MAR":
        return 3
    if us == "ABR":
        return 4
    if us == "MAI":
        return 5
    if us == "JUN":
        return 6
    if us == "JUL":
        return 7
    if us == "AGO":
        return 8
    if us == "SET":
        return 9
    if us == "OUT":
        return 10
    if us == "NOV":
        return 11
    if us == "DEZ":
        return 12

    return -1


# Returns array of classes in strippedArray that match classIds in
# classIdArray.
# Caution: WILL return all classes (i.e., TP1, TP2, T1, T2, ...)
def getClasses(strippedArray, semester, classIdArray):
    myClasses = []
    for data in strippedArray:
        if data.aulaId not in classIdArray or data.semestre != semester:
            continue
        myClasses.append(data)
    return myClasses

def getClassType(turma):
    return re.search(".+(?=\d)", turma).group(0)
