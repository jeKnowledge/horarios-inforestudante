import DataParser
import TimetableMaker

print("started")

# Mock schedule data
semester = 1
classesId = [178771]

# Parse csv into array of stripped data
dataRawArray = DataParser.csvIntoRawArray(DataParser.openFile("HorariosRaw.csv"))
dataStrippedArray = DataParser.rawArrayToStrippedArray(dataRawArray)

# Get out classes
possibleClasses = TimetableMaker.possibleClasses(dataStrippedArray, semester, classesId) #All classes for the semester
noDuplicates = TimetableMaker.removeDuplicates(possibleClasses, True)

#Test
for aula in noDuplicates:
    print(aula.dataStr())