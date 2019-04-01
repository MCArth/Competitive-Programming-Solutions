# Solution to https://open.kattis.com/problems/outing

firstInput = input()

# Creates list out of first input, selects index in list which corresponds to the number of places available on the bus.
numPlaces = int(firstInput.rstrip().split()[1])

participantsAsStr = input()  # Takes participants info

# Creates list of participant info, converting each number to int
participants = [int(a) for a in participantsAsStr.rstrip().split()]

# Contains the size of each 'item', containing a length 2 list for each item.
# 0th index contains the number of mandatory participants, 1st index contains number of non-necessary participants.
# So min size is 0th index and max size is 0th index + 1st index for any given item.
stringSizes = []

# Counter which signifies what 'item' an individual is part of once they have been processed.

participantStringCounter = -2

# Checks each individual as a start node
for firstIndex in range(len(participants)):

    # Contains all individuals that have been processed to have requirements between each other
    currParticipantsString = []
    i = firstIndex  # Sets the index currently being processed as the element you start on

    # While still processing individuals as part of an item who have not been processed yet
    # Individuals that have been processed will be set to a flag less than 1 indicating their status
    while participants[i] > 0:
        
        nextIndex = participants[i]-1  # Gets the index of the dependant of the current individual
        currParticipantsString.append(i)  # Adds processed index to list of processed indices in this for loop
        participants[i] = 0  # Flag set to 0, indicating that it is an index currently stored in participantsString
        i = nextIndex  # Sets index to next individual to be processed

    # Once while loop exits, checks whether it was dependent on itself or on another 'item'

    # Was dependent on itself, forms its own new item
    if participants[i] == 0:
        participants[i] = -1  # Sets flag indicating that indices from then on are part of loop
        stringFlag = participantStringCounter  # Sets flag for this 'item' to counter
        participantStringCounter -= 1  # Decrements counter for next unique 'item'
        stringSizes.append([0, 0])  # Creates new length-two list for the size of this item to be stored in
    # If it's dependent on and leads into another 'item'
    else:
        stringFlag = participants[i]  # Sets flag to that of the 'item' it is part fo

    stringIndex = -stringFlag-2  # Gets the index of where the size of the item is stored

    inLoop = False  # If currently in a loop, incrementing essential member size

    # Goes through each participant Index that has been indexed in
    # the current item, setting their flags and determining item size
    for pI in currParticipantsString:

        # Indicates that that and all subsequent individuals are part of a loop
        if participants[pI] == -1:
            inLoop = True

        # Increments essential members size
        if inLoop:
            stringSizes[stringIndex][0] += 1
        # Increments non essential members size
        else:
            stringSizes[stringIndex][1] += 1

        # Sets their flag indicating what 'item' individuals are part of
        participants[pI] = stringFlag


# Dynamic programming portion of program:

# 2-d list that contains the max weight available for a case of up to a given weight j, including the first i numbers
maxMade = [[0]*numPlaces for x in range(len(stringSizes))]

# Including all items up to i in the case
for i in range(0, len(stringSizes)):
    # Max places on the bus, j
    for j in range(0, numPlaces):

        maxIncludingItem = 0  # The maximum weight that can be formed when including the ith index item up to j weight

        # Finding the maximum weight possible including ith item
        for optWeight in range(stringSizes[i][1]+1):

            # If weight including the optional weight formed is higher than weight allowed
            if j-(stringSizes[i][0]+optWeight) < 0:
                break
            # Checks for new maximum
            elif maxMade[i-1][j-(stringSizes[i][0]+optWeight)] + optWeight + stringSizes[i][0] > maxIncludingItem:
                    maxIncludingItem = maxMade[i-1][j-(stringSizes[i][0]+optWeight)] + optWeight + stringSizes[i][0]

        # For case of ith index item being first item used
        theWeight = 0
        # If weight of item is allowed within jth weight
        if stringSizes[i][0] <= j+1:
            theWeight = stringSizes[i][0]  # Sets weight as required weight
            # If all non-required individuals can fit
            if stringSizes[i][1] < j+1-stringSizes[i][0]:
                theWeight += stringSizes[i][1]
            # Includes the most non-required individuals
            else:
                theWeight += j+1-stringSizes[i][0]

        # Takes the maximum of the different cases
        maxMade[i][j] = max(maxIncludingItem, maxMade[i-1][j], theWeight)

print(maxMade[-1][-1])  # Prints result
