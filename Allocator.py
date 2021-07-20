memoryFile = open("memory.txt", "r")
memoryFileList = []
outputFile = open("output.txt", "w")

for line in memoryFile:
    lineStr = line.rstrip("\n").split("\n")
    memoryFileList.append(lineStr)

newList = []
for element in memoryFileList:
    for i in element:
        elementStr = i.split(",")
        newList.append(elementStr)
memoryList = newList[0]
processList = newList[1]

for i in range(0, len(memoryList)): #switching all elements from string to integer
    memoryList[i] = int(memoryList[i])
for i in range(0, len(processList)):
    processList[i] = int(processList[i])
firstMemoryList =  memoryList.copy() #copying the list for each allocation algorithm
bestMemoryList = memoryList.copy()
worstMemoryList = memoryList.copy()

def FirstFitMemory(firstMemoryList,processList):
    print("First-Fit Memory Allocation", file = outputFile)
    print("-----------------------------------------------------------------------------------------------", file = outputFile)
    print("start =>", *firstMemoryList, file = outputFile)
    print("\n", file = outputFile)

    for process in processList: #for each process
        for memory in firstMemoryList: #for each memory partition in memory list
            if type(memory) != str and memory >= process: #if the memory is not like "115*" and memory is bigger than process
                ind = firstMemoryList.index(memory) #finding the memory's index
                firstMemoryList.insert(ind,str(process)+"*") #inserting the process with the "*"
                firstMemoryList[ind+1] -= process #subtracting the process from the memory
                print(process, "=>", *firstMemoryList, file = outputFile)
                print("\n", file = outputFile)
                break #breaking when it finds it
        else:
            continue

FirstFitMemory(firstMemoryList,processList)


def BestFitMemory(bestMemoryList, processList):
    print("Best-Fit Memory Allocation", file = outputFile)
    print("-----------------------------------------------------------------------------------------------", file = outputFile)
    print("start =>", *bestMemoryList, file = outputFile)
    print("\n", file = outputFile)

    secmemoryList = bestMemoryList.copy()
    bestMemoryList.sort() #sorting all elements
    for process in processList:
        for memory in bestMemoryList:
            if type(memory) != str and memory >= process:
                ind = secmemoryList.index(memory)
                secmemoryList.insert(ind,str(process)+"*")
                secmemoryList[ind+1] -= process
                bestMemoryList.append(secmemoryList[ind+1]) #adding the memory element that is deleted
                bestMemoryList.sort() #sorting the new list
                print(process, "=>", *secmemoryList, file = outputFile)
                print("\n", file = outputFile)
                bestMemoryList.remove(memory) #removing the memory because it is done
                break      
        else:
            continue       

BestFitMemory(bestMemoryList, processList)

def WorstFitMemory(worstMemoryList, processList):
    print("Worst-Fit Memory Allocation", file = outputFile)
    print("-----------------------------------------------------------------------------------------------", file = outputFile)
    print("start =>", *worstMemoryList, file = outputFile)
    print("\n", file = outputFile)

    thrmemoryList = worstMemoryList.copy()
    worstMemoryList.sort(reverse=True) #sorting reverse
    for process in processList:
        for memory in worstMemoryList:
            if type(memory) != str and memory >= process:
                ind = thrmemoryList.index(memory)
                thrmemoryList.insert(ind,str(process)+"*")
                thrmemoryList[ind+1] -= process
                worstMemoryList.append(thrmemoryList[ind+1])
                worstMemoryList.sort(reverse=True) #sorting reverse the new list
                print(process, "=>", *thrmemoryList, file = outputFile)
                print("\n", file = outputFile)
                worstMemoryList.remove(memory)
                break
            else: #if it can not find the memory that is bigger than the process
                print(process, "=>", "not allocated, must wait", file = outputFile)
                print("\n", file = outputFile)
                break
        else:
            continue

WorstFitMemory(worstMemoryList, processList)
memoryFile.close()
outputFile.close()
