import io
import csv
import struct
from switcher import tmpl

name = tmpl[0][0]
file = open(tmpl[0][2] + "_input.bin", "rb")

anyEnumeratedSections = False

for item in tmpl:
    if item[4] > -1:
        anyEnumeratedSections = True

with open(name + "_output.csv", "w", newline="") as output:
    writer = csv.writer(output)

    for item in tmpl:

        headers = item[1]
        types = item[3]
        startIdx = item[4]
        rowCount = item[5]

        writer.writerow(headers)

        for i in range(rowCount):
            nextRow = []

            if startIdx >= 0:
                nextRow.append(str(i + startIdx))
            else:
                if anyEnumeratedSections:
                    nextRow.append("")

            for j in range(int(len(types) / 2)):
                for k in range(types[j * 2]):
                    nextRow.append(str(      struct.unpack(">" + types[(j * 2) + 1], file.read(4))[0]    ))
                                 #     round(                                                        , 3)
                                 # Balancing accuracy vs. readability.
                                 # This is probably better to ensure a byte-for-byte I/O loop.
            
            writer.writerow(nextRow)
