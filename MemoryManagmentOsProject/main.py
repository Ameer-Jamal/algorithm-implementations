# Ameer Jamal OS project Contiguous Memory Allocation Algorithms:
#   20180381       20180331


# we need this import for a deep copy to maintain the original box sizes
# with normal copies lists are referenced to each other so for example
# if we make x[i] = y[i] and then change y[i], x[i] will also change
# or at least that was a problem we ran into
import copy


# this function is for displaying all the data and stats of each algorithm
# this will be called in each function at the end to print
# the parameters explained :
# blockSize: to know which block we are working with and whats its size
# base size : so the block size changes so we need the base size (a deep copy of blockSIze) to have a static reference
# allocation : lets us know if or if not a process is allocated and if yes what block is it allocating
# processSize: a list of the process's we use with its size
# blockOccupation : tells us if a block is occupied or not

def printAllocation(blockSize, baseSize, allocation, processSize, blockOccupation):
    # define vars to understand which algorithm is performing better
    totalBlocksSize = 0
    totalOccupiedBlockSize = 0
    totalProcessSize = 0
    ########################################################################
          #process Number  size of this process     size of the block   space left from block             what block has
          #                                          (if occupied)      after occupation                  been occupied
    print("ProcessID       Process Size         Original blockSize      Internal fragmentation            Block no.")
    for i in range(len(processSize)):
        #     process number               process size of this process     if base size of block is allocated display its base size (original size) else n/a        if block is allocated display how much is left of it                                       display the number of the block only if the block is occupied else n/a
        print(i + 1, "                  ", processSize[i], "                     ", baseSize[allocation[i]] if allocation[i] != -1 else 'N/A', "                  ", blockSize[allocation[i]] if allocation[i] != -1 else 'N/A', "                          ", allocation[i]+1 if allocation[i] != -1 else 'N/A',"\n================================================================================================================================")

    ########################################################################
    # Finding the total size of process's (occupied or not)
    for i in range(len(processSize)):
        totalProcessSize += processSize[i]
    ########################################################################
    # Finding the total size of process's IF IT IS OCCUPIED (the point is to find how much space is totally occupied)
    for i in range(len(processSize)):
        if allocation[i] != -1:
            totalOccupiedBlockSize += processSize[i]
    ########################################################################
    # Finding the space of all blocks by going through every block occupied or not and then summing them
    for i in range(len(baseSize)):
        totalBlocksSize += baseSize[i]
    ########################################################################
    # Finding remaining space of blocks, by subtracting what has been occupied from the total
    totalBlockSizeLeft = totalBlocksSize - totalOccupiedBlockSize
    ########################################################################

    # printing out the information of the table we printed and calculated the stats for

    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("the total of all process sizes is: ")
    print(totalProcessSize)
    print('----------------------------------------------------------------------')
    print("the total of all block space is: ")
    print(totalBlocksSize)
    print('----------------------------------------------------------------------')
    print("the total wasted block space for this algorithm is: ")
    print(totalBlockSizeLeft)
    print('----------------------------------------------------------------------')
    print("the total used block space for this algorithm is: ")
    print(totalOccupiedBlockSize)
    print('----------------------------------------------------------------------')
    print("the size of process's that have not been occupied is: ")
    print(totalProcessSize-totalOccupiedBlockSize)
    print('----------------------------------------------------------------------')

    # here we are displaying a yes/no mini table for knowing which blocks have and have not been occupied
    # we are using ternary statements display x if (this condition true) else display y to help us write clean code
    print("has the block been occupied? ( \u2713 represents Yes and x represents No ) ")
    for i in range(len(blockOccupation)):
        print(f"Block {i + 1}    \u2713    size:{baseSize[i]}" if blockOccupation[i] else f'Block {i+1}    x    size:{baseSize[i]}')


    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

########################################################################################################################


# the idea here is to go over all of the blocks and make sure we are picking the Best fit for each process
# the way to do this is let the function know the process size , and all the block sizes then you logical statements
# to put it in the correct best block (the statements kinda like finding a max between two numbers statement
# where we are trying to find max block size for each process size to minimize internal fragmentation
def allocateBest(blockSize, processSize):
    # Storing into which block the process has been put into (-1 means it hasn't been put in any block yet)
    allocation = [-1] * len(processSize)    # statement: for each process initialize -1 as its allocation

    # Storing if the block has been occupied or not
    blockOccupation = [False] * len(blockSize)  # statement: for each block initialize to false

    # so we can make calculations and preserve the original block sizes
    baseSize = copy.deepcopy(blockSize)

    ###################################################################################################################
    # here we are starting the algorithm

    # scroll through all processes
    for i in range(len(processSize)):
        # set the best index to -1 assuming that the process has no block to go into
        bestIndex = -1
        # scroll through all blocks FOR EACH PROCESS processSize[i]
        for j in range(len(blockSize)):
            # if the block size is bigger than the process size AND the block isn't already occupied by some other process
            # set the best index to J (block number J)
            if blockSize[j] >= processSize[i] and not blockOccupation[j]:
                if bestIndex == -1:
                    bestIndex = j
                # else if there is a more optimal block to put the process into do that instead (as this is best fit)
                elif blockSize[bestIndex] > blockSize[j]:
                    bestIndex = j

        # If we found a block for this process
        if bestIndex != -1:
            # allocate block j to p[i] process and state that it is occupied
            allocation[i] = bestIndex
            blockOccupation[allocation[i]] = True

            # subtract memory in this block for calculations like how much block space we utilized.
            # this can help us find internal fragmentation
            blockSize[bestIndex] -= processSize[i]

    # after its all done, send the date to be printed by the print function we created
    printAllocation(blockSize, baseSize, allocation, processSize,blockOccupation)


########################################################################################################################


# the idea here is to fit the first block available for each process that is available
# id imagine this as a parking a car at a location with azmeh, as you are just looking for the first place your car
# can fit not the best or worst
def allocateFirst(blockSize, processSize):
    # Storing into which block the process has been put into (-1 means it hasn't been put in any block yet)
    allocation = [-1] * len(processSize)

    # Storing if the block has been occupied or not
    blockOccupation = [False] * len(blockSize)

    # so we can make calculations and preserve the original block sizes
    baseSize = copy.deepcopy(blockSize)

    ###################################################################################################################
    # here we are starting the algorithm

    # scroll through all processes
    for i in range(len(processSize)):
        # scroll through all blocks FOR EACH PROCESS processSize[i]
        for j in range(len(blockSize)):
            # if the block size is bigger than the process size AND the block isn't already occupied by some other process
            if blockSize[j] >= processSize[i] and not blockOccupation[j]:
                # allocate block j to p[i] process
                # the key difference here from bestAllocate for example is we arent checking every block
                # once we find any block that fits ( in other words the first block that fits)
                # we instantly put it then go to the next process and start over
                allocation[i] = j

                # Reduce available memory in this block for calculations like how much block space we utilized.d.
                # this can help us find internal fragmentation
                blockSize[j] -= processSize[i]
                # set this block to occupied.
                blockOccupation[allocation[i]] = True

                #once or if the process is put in, just stop looking and go to the next process
                break
    # after its all done, send the date to be printed by the print function we created
    printAllocation(blockSize, baseSize, allocation,processSize,blockOccupation)

########################################################################################################################

# the idea here is to go over all of the blocks and make sure we are picking the Worst fit for each process
# this is almost the exact opposite of the best fit algorithm
def allocateWorst(blockSize, processSize):

    # Storing into which block the process has been put into (-1 means it hasn't been put in any block yet)
    allocation = [-1] * len(processSize)

    # Storing if the block has been occupied or not
    blockOccupation = [False] * len(blockSize)

    # so we can make calculations and preserve the original block sizes
    baseSize = copy.deepcopy(blockSize)

    ###################################################################################################################
    # here we are starting the algorithm
    # scroll through all processes
    for i in range(len(processSize)):
        # set the best index to -1 assuming that the process has no block to go into
        worstIndex = -1
        # scroll through all blocks FOR EACH PROCESS processSize[i]
        for j in range(len(blockSize)):
            # at the start we are just doing looking for a block that fits but then in the elif statement things change

            # if the block size is bigger than the process size AND the block isn't already occupied by some other process
            #  set the worst index to J (block number J)
            if blockSize[j] >= processSize[i] and not blockOccupation[j]:
                if worstIndex == -1:
                    worstIndex = j
                # else if there is a WORSE block to put the process into do that instead (as this is worst fit)
                # notice that this block is still going to fit, it just going to maximize our internal fragmentation
                elif blockSize[worstIndex] < blockSize[j]:
                    worstIndex = j

        # If we found a block for this process ( knowing that it is the worst block possibly available)
        if worstIndex != -1:
            # allocate block j to p[i] process and state that it is occupied by setting blockOccupation of i to true
            allocation[i] = worstIndex
            blockOccupation[allocation[i]] = True

            # subtract memory in this block for calculations like how much block space we utilized.
            # this will be used to find internal fragmentation
            blockSize[worstIndex] -= processSize[i]
    # lets not forget to print the results we found
    printAllocation(blockSize, baseSize, allocation, processSize, blockOccupation)

########################################################################################################################


########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################

# Driver to run these algorithms
if __name__ == '__main__':

    #############################################################################################

    blockSize = [10, 30, 15, 40, 20]
    processSize = [20, 5, 13, 35, 27]
    baseSize = copy.deepcopy(blockSize)

    #############################################################################################

    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    for i in range(len(baseSize)):
        print(f" Block size {i + 1}: {baseSize[i]}")



    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    print("EXECUTING BEST FIT ALGORITHM")
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    allocateBest(blockSize, processSize)

    #############################################################################################

    blockSize = [10, 30, 15, 40, 20]
    processSize = [20, 5, 13, 35, 27]
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    print("EXECUTING FIRST FIT ALGORITHM")
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    allocateFirst(blockSize, processSize)

    #############################################################################################

    blockSize = [10, 30, 15, 40, 20]
    processSize = [20, 5, 13, 35, 27]
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    print("EXECUTING WORST FIT ALGORITHM")
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    allocateWorst(blockSize, processSize)
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

    #############################################################################################
    # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    # print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    # print( 'lets do some random tests to understand the algorithms on different numbers')
    # print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    #
    # import random
    #
    # # Generate 5 random numbers between 100 and 1000
    # randomBlockSize = random.sample(range(100, 1000), 5)
    # randomProcessSize = random.sample(range(10,500), 4)
    #
    # bsSave = copy.deepcopy(randomBlockSize)
    # psSave = copy.deepcopy(randomProcessSize)
    # baseSize = copy.deepcopy(randomBlockSize)
    #
    # bsSave2 = copy.deepcopy(randomBlockSize)
    # psSave2 = copy.deepcopy(randomProcessSize)
    # for i in range(len(baseSize)):
    #     print(f" Block size {i + 1}: {baseSize[i]}")
    #
    # allocateBest(randomBlockSize, randomProcessSize)
    #
    # baseSize = copy.deepcopy(baseSize)
    # allocateFirst(bsSave,psSave)
    #
    # baseSize = copy.deepcopy(baseSize)
    # allocateWorst(bsSave2,psSave2)