import os


def retreive(onelinerNumber):
    with open(fileNames[onelinerNumber], 'r') as line:
        line = [x.strip() for x in line]
        for retrievedLine in line:
            return [int(n) for n in retrievedLine.split()]


numberOfLines = sum(1 for line in open("integers.txt"))
oneLiners = []
fileNames = []
linecounter = 0
# open integers.txt and sort, save each line to different oneliners
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
###################################################################

# now we have to merge these oneliners without wasting too much memory, first we merge two neighbor oneliners.
# The resulting line will have length of 2 oneliners. We have to divide the result into 2 files.
# After that we will take two sorted file groups and merge them until we have a sorted list across all files

for loop in range(0, int((numberOfLines + 1) / 2)):  # to calculate how many merges we require before a full sorted list
    leftStart = 0  # first file of left file group
    step = 2 ** loop  # to calculate the size of file groups
    rightStart = leftStart + step  # first file of right file group
    cursor1 = 0  # shows which index of list we are working with
    cursor2 = 0
    listOfGroupLeft = 0  # to calculate which file of group we are working with
    listOfGroupRight = 0
    line1 = retreive(leftStart)  # first files of two groups into lines
    line2 = retreive(rightStart)
    while leftStart + step < numberOfLines:  # if there can't be any right list, stop

        # Check if one of the lists have exhausted if so refresh it by retrieving another from next file of respective
        # group

        if cursor1 == len(line1):
            listOfGroupLeft += 1
            line1 = retreive(leftStart+listOfGroupLeft)
            cursor1 = 0
        if cursor2 == len(line2):
            listOfGroupRight += 1
            line2 = retreive(rightStart+listOfGroupRight)
            cursor2 = 0

        ###################################################################

        # now we must merge these two lists and store the result into another list. When we merge, we have to track
        # how many numbers we took from each group. When the number of took numbers hits the size of list in oneliner,
        # we update list of that group by retrieving next oneliner.
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
