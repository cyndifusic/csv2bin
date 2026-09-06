import io
import csv
import struct
from switcher import tmpl

name = tmpl[0][0]
file = open(tmpl[0][2] + "_output.bin", "wb")

anyEnumeratedSections = False

for item in tmpl:
    if item[4] > -1:
        anyEnumeratedSections = True

readStart = 1 if anyEnumeratedSections else 0

with open(name + "_input.csv", newline="") as input:
    reader = csv.reader(input)
    rows = list(reader)
    rowsRead = 0
    countRowsRead = 0

    for item in tmpl:

        types = item[3]
        startIdx = item[4]
        rowCount = item[5]

        expandedTypes = []
        for i in range(int(len(types) / 2)):
            for j in range(types[i * 2]):
                expandedTypes.append(types[(i * 2) + 1])

        for i in range(rowCount + 1):
            if i > 0:
                for j in range(readStart, len(expandedTypes) + readStart):
                    
                    # >:( Grrrrrrr!!!!!
                    match expandedTypes[j - readStart]:
                        case "f":
                            file.write(struct.pack(">f", float(rows[i + rowsRead][j])))
                        case "i":
                            file.write(struct.pack(">i", int(rows[i + rowsRead][j])))
                        case "I":
                            file.write(struct.pack(">I", int(rows[i + rowsRead][j])))
            countRowsRead += 1

        rowsRead = countRowsRead
