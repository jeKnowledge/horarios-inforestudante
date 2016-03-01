import DataParser
import TimetableMaker

print("started")

# Mock schedule data
semester = 1
classesId = [178771]

# Parse csv into array of stripped data
dataRawArray = DataParser.csvIntoRawArray(DataParser.openFile("HorariosRaw.csv"))
dataStrippedArray = DataParser.rawArrayToStrippedArray(dataRawArray)

# Create timetable
possibleClasses = TimetableMaker.possibleClasses(dataStrippedArray, semester, classesId) #All classes for the semester
TimetableMaker.removeDuplicates(possibleClasses, True)