import DataParser
import ClassFilter
import TimetableMaker

print("started")

# Mock user data
semester = 1
classesId = [178771, 178867, 181136, 181692, 181695, 182399, 180876]

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
TimetableMaker.outputExcel(aulas, noOverlaps)