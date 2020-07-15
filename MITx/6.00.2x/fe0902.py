def loadFile():
    inFile = open('julytemps.txt')
    high = []
    low = []
    for line in inFile:
        fields = line.split()
        # FILL THIS IN
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return (low, high)