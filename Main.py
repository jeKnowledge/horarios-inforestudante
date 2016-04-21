import DataParser
import ClassFilter
import TimetableMaker

print("started")

# Mock user data
semester = 1
classesId = [178880, 178754]

# Parse csv into array of stripped data
dataRawArray = DataParser.csvIntoRawArray(DataParser.openFile("HorariosRaw.csv"))
dataStrippedArray = DataParser.rawArrayToStrippedArray(dataRawArray)

# Filter and separate classes
aulas = {}
for disciplina in classesId:
    possibleClasses = ClassFilter.possibleClasses(dataStrippedArray, semester, disciplina) # All classes for the semester
    noDuplicates = ClassFilter.removeDuplicates(possibleClasses, True)
    aulas[disciplina] = ClassFilter.groupByType(noDuplicates)

# Make timetable
possibleCombinations = TimetableMaker.possibleCombinations(aulas)
noOverlaps = TimetableMaker.removeOverlaps(aulas, possibleCombinations)

# Output to Excel
wb = TimetableMaker.outputExcel(aulas, noOverlaps)

# Output to html
TimetableMaker.convertExcelToWeb(wb)