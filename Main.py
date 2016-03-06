import DataParser
import ClassFilter

print("started")

# Mock user data
semester = 1
classesId = [178771, 178867, 181136]

# Parse csv into array of stripped data
dataRawArray = DataParser.csvIntoRawArray(DataParser.openFile("HorariosRaw.csv"))
dataStrippedArray = DataParser.rawArrayToStrippedArray(dataRawArray)

#Filter and separate classes
aulas = {}
for disciplina in classesId:
    possibleClasses = ClassFilter.possibleClasses(dataStrippedArray, semester, disciplina) #All classes for the semester
    noDuplicates = ClassFilter.removeDuplicates(possibleClasses, True)
    aulas[disciplina] = ClassFilter.groupByType(noDuplicates)

#Make timetable
