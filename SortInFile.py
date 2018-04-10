import os

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


def mergeSort(a):
    if len(a) == 1:
        return a

    middle = len(a) // 2

    left = a[:middle]
    right = a[middle:]

    left = mergeSort(left)
    right = mergeSort(right)
    return list(merge(left, right))


numberOfLines = sum(1 for line in open("integers.txt"))
linesortedIntfile=open("linesorted.txt", "a+")
with open("integers.txt") as intfile:
    for line in intfile:
        lineAsList = [int(n) for n in line.split()]
        lineAsList.sort()
        sortedLine = ""
        for j in lineAsList:
            sortedLine += str(j) + " "
        linesortedIntfile.write(sortedLine+"\r\n")
        linesortedIntfile.flush()
linesortedIntfile.close()
#os.remove("./integers.txt")
