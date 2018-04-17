import os

# def merge(files, step, listSize):



numberOfLines = sum(1 for line in open("integers.txt"))
oneLiners = []
fileNames = []
linecounter = 0
with open("integers.txt") as intfile:
    for line in intfile:
        lineAsList = [int(n) for n in line.split()]
        lineAsList.sort()
        sortedLine = ""
        for j in lineAsList:
            sortedLine += str(j) + " "
        oneLiners.append(open('oneLiner' + str(linecounter) + ".txt", 'w+'))
        fileNames.append('oneLiner' + str(linecounter) + ".txt")
        oneLiners[linecounter].write(sortedLine + "\r\n")
        oneLiners[linecounter].flush()
        oneLiners[linecounter].close()
        linecounter += 1

for loop in range(0, int((numberOfLines + 1) / 2)):
    leftStart = 0
    step = 2 ** loop
    while leftStart + step < numberOfLines:  # if there can't be any right list, stop
        rightStart = leftStart + step
        file1 = oneLiners[leftStart]
        file2 = oneLiners[rightStart]
        with open(fileNames[leftStart], 'r') as line:
            line = [x.strip() for x in line]
            for line1 in line:
                line1 = [int(n) for n in line1.split()]
        with open(fileNames[rightStart], 'r') as line:
            line = [x.strip() for x in line]
            for line2 in line:
                line2 = [int(n) for n in line2.split()]
        iterator1 = 0
        iterator2 = 0
        listcntr1 = leftStart
        listcntr2 = rightStart
        mergedList = []
        mergedFileNum = 0
        while line1[0] == 999999 and line2[0] == 999999:
            if iterator1 == len(line1) - 1:
                if listcntr1 + 1 < rightStart:
                    listcntr1 += 1
                    with open(fileNames[listcntr1], 'r') as line:
                        line = [x.strip() for x in line]
                        for line1 in line:
                            line1 = [int(n) for n in line1.split()]
                    iterator1 = 0
                else:
                    line1[0] = 999999
            if iterator2 == len(line2) - 1:
                if listcntr2 + 1 < rightStart + step:
                    listcntr2 += 1
                    with open(fileNames[listcntr2], 'r') as line:
                        line = [x.strip() for x in line]
                        for line2 in line:
                            line2 = [int(n) for n in line2.split()]
                    iterator2 = 0
                else:
                    line2[0] = 999999

            if line1[iterator1] < line2[iterator2]:
                mergedList.append(line1[iterator1])
                iterator1 += 1
            else:
                mergedList.append(line2[iterator2])
                iterator2 += 1
            if len(mergedList) == len(line1):
                open(fileNames[mergedFileNum], 'w')
                sortedLine = ""
                for j in mergedList:
                    sortedLine += str(j) + " "
                oneLiners[mergedFileNum].write(sortedLine + "\r\n")
                mergedFileNum += 1
        leftStart += step * 2  # next left is assigned

# merge(oneLiners,1,numberOfLines)
# os.remove("./integers.txt")
