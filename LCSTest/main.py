import os
import sys
import timeit  # we will need this for the timing of the functions
print()
print("//////////////////////////////////////////////////////////////////////////////////////")
print("//////////////////////////////////////////////////////////////////////////////////////")
print("Program written by Ameer Jamal 20180381\n")
print("Program written in Python 3.9.5 with imported libraries: OS, SYS, and Timeit")
print()
sys.setrecursionlimit(999999999)
print("The recursion limit set for this program is: " + str(sys.getrecursionlimit()))
print("//////////////////////////////////////////////////////////////////////////////////////")
print("//////////////////////////////////////////////////////////////////////////////////////")


def lcs3(a, b, c):
    m = len(a)
    l = len(b)
    n = len(c)
    dynamicArr = [[[0 for k in range(n+1)] for j in range(l+1)] for i in range(m+1)]

# This loop goes through every letter in a b and c and checks for matches
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            for k, z in enumerate(c):
                if x == y and y == z:
                    dynamicArr[i+1][j+1][k+1] = dynamicArr[i][j][k] + 1 # if all three match add one into the dynamic array
                else: # if it doesnt take the max from i+1 j+1 k , i j+1 k+1 , i+1 j k+1
                    dynamicArr[i+1][j+1][k+1] = max(dynamicArr[i+1][j+1][k],
                                              dynamicArr[i][j+1][k+1],
                                              dynamicArr[i+1][j][k+1])
    # return dynamicArr[-1][-1][-1] for the last result in the array, this gives us the LCS length

    lcs = "" # defining a variable to put the LCS values in

    # here we are going through the array and getting back the values by seeing if we have a match,
    # then appending that match from the corresponding array
    while m > 0 and l > 0 and n > 0:
        step = dynamicArr[m][l][n]
        if step == dynamicArr[m-1][l][n]:
            m -= 1
        elif step == dynamicArr[m][l-1][n]:
            l -= 1
        elif step == dynamicArr[m][l][n-1]:
            n -= 1
        else:
            lcs += str(a[m-1])
            m -= 1
            l -= 1
            n -= 1

    # lcs[::-1 ] means Return the slice of the string that starts at the end and steps backward one element at a time:
    # so basically print the letters in reverse order
    # and dynamicArr[-1][-1][-1] just returns the last element
    result = [lcs[::-1], dynamicArr[-1][-1][-1]]
    return result


# Recursive Programming implementation of LCS problem
def lcsRecursive(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m - 1] == Y[n - 1]:
        return 1 + lcsRecursive(X, Y, m - 1, n - 1)
    else:
        return max(lcsRecursive(X, Y, m, n - 1), lcsRecursive(X, Y, m - 1, n))


# Dynamic Programming implementation of LCS problem

def lcsDynamic(X, Y):
    # find the length of the strings and set them to variables
    strLenOfX = len(X)
    strLenOfY = len(Y)

    # declaring the array for storing the LCS values
    dynamicArr = [[None] * (strLenOfY + 1) for i in range(strLenOfX + 1)]

    # We will now be building the array from the bottom up
    for i in range(strLenOfX + 1):
        for j in range(strLenOfY + 1):
            if i == 0 or j == 0: # Setting our base cases
                dynamicArr[i][j] = 0
            elif X[i - 1] == Y[j - 1]: # Adding one if there is a match
                dynamicArr[i][j] = dynamicArr[i - 1][j - 1] + 1
            else:
                # if not a match take the max between [i-1][j] and [1][j-1]
                dynamicArr[i][j] = max(dynamicArr[i - 1][j], dynamicArr[i][j - 1])

    # dynamicArr[strLenOfX][strLenOfY] contains the length of LCS
    # as the answer in the Dynamic array is always going to be in the last element on the bottom right corner
    # That's what we'll return
    return dynamicArr[strLenOfX][strLenOfY]


def makeFile(fileName):
    try:  # make a file if not available
        f = open(fileName, "x")
        makeXsequence = input("Enter your X sequence: ")
        makeYsequence = input("Enter your Y sequence: ")
        # f = open("userData.txt", "a")
        f.write(makeXsequence + "\n" + makeYsequence)
        f.close()
        print("file was made successfully")
    except:
        # if file already created return as this function is only
        # responsible for making a file if not available
        return


def readFile(fileName):
    try:
        # delegating responsibility and making sure file is made
        makeFile(fileName)
        f = open(fileName, "r")
        # Using readlines() to read each line in the file
        # and save it to the data list
        Lines = f.readlines()
        # Strips the newline character and makes
        # sure its clean text
        data = []
        for line in Lines:
            data.append(line.strip())
            f.close()
        # print("file was read successfully")
        return data
    except:
        # if an error has occurred then reset the file
        print("error file reading encountered an issue a problem ")
        print("please try resetting the file")
        resetFile(fileName)


def resetFile(fileName):
    char = input("please type R to reset (this will delete your file) the X and Y Sequence or 'x' to go back: ")
    if char == "r" or char == "R":
        os.remove(fileName)
        makeFile(fileName)
    elif char == 'x':
        return
    else:
        print("wrong character")
        resetFile(fileName)


# Driver program to test the above functions'
choice = input("Please hit Enter for normal data or input 1 for DNA file Provided with assignment or -1 for for Huge "
               "Data: ")
if choice == "-1":
    myFileName = "userDataThatIsTooBigToTest.txt"
elif choice == "1":
    myFileName = "DNA.txt"
else:
    myFileName = "userData.txt"

makeFile(myFileName) # this will make sure there is a file to be read from with at least one x and y string
# initializing array to fill in and find the LCS between
X = []
Y = []

# Loop below fills up the arrays
for w in range(len(readFile(myFileName))):
    if w % 2 == 0:
        X.append(readFile(myFileName)[w])
    elif w % 2 != 0:
        Y.append(readFile(myFileName)[w])


print("======================================================================================")
print("These will be the DNA sequences we will be testing\nThe Values are generated from "
      "https://www.bioinformatics.org/sms2/random_dna.html")
print("======================================================================================")

# Prints what tests we are going to do
for x in range(len(X)):
    print("The values for test number " + str(x + 1) + ". Of length " + str((len(X[x]))) + " are:")
    print(X[x] + "\n" + Y[x])
    print("======================================================================================")


print()
print("//////////////////////////////////////////////////////////////////////////////////////")

print("//////////////////////////////DYNAMIC APPROACH////////////////////////////////////////")

print("//////////////////////////////////////////////////////////////////////////////////////")
print()


# Prints the LCS and the duration of finding LCS using dynamic programming
for x in range(len(X)):
    # Start timer
    startTimer = timeit.default_timer()
    print("Length of LCS using Dynamic Programing for test number " + str(x+1) + " Of length " + str((len(X[x]))) +" is:\n", lcsDynamic(X[x], Y[x]))
    # Stop timing
    intTime = "%.7f" % ((timeit.default_timer() - startTimer) * 1)
    message = "Ameer Elapsed Time: " + str(intTime)
    # print timing results
    print()
    print(message, "Seconds")
    print("--------------------------------------------------------------------------------------")
print()
print("//////////////////////////////////////////////////////////////////////////////////////")

print("/////////////////////////LCS OF 3 STRINGS APPROACH////////////////////////////////////")

print("//////////////////////////////////////////////////////////////////////////////////////")
print()
# defining variables to test the lcs3 function from lcs3 txt file
a = readFile("lcs3Data.txt")[0]
b = readFile("lcs3Data.txt")[1]
c = readFile("lcs3Data.txt")[2]

print("the 3 strings of length " + str(len(a)) + " that we are going to find lcs for are:\n\"" + a + "\"\n\"" + b + "\"\n\"" + c + "\"\n" )
# the second element the lcs3 returns is the length, so we are printing that

print("The length of the LCS is")

print(lcs3(a, b, c)[1])
# Start timer
startTimer = timeit.default_timer()
# we then print the values
print("the values for the lcs are :")
print(lcs3(a, b, c)[0])
# Stop timing
intTime = "%.5f" % ((timeit.default_timer() - startTimer) * 1)
message = "Ameer Elapsed Time: " + str(intTime)
# print timing results
print()
print(message, "Seconds")


print()
print("//////////////////////////////////////////////////////////////////////////////////////")

print("//////////////////////////////RECURSIVE APPROACH//////////////////////////////////////")

print("//////////////////////////////////////////////////////////////////////////////////////")
print()

# Prints the LCS and the duration of finding LCS using the recursive approach
for x in range(len(X)):
    # Start timer
    startTimer = timeit.default_timer()
    print("Length of LCS using Recursive approach for test number " + str(x+1) + " Of length " + str((len(X[x]))) +" is:\n",  lcsRecursive(X[x], Y[x], len(X[x]), len(Y[x])))
    # Stop timing
    intTime = "%.5f" % ((timeit.default_timer() - startTimer) * 1)
    message = "Ameer Elapsed Time: " + str(intTime)
    # print timing results
    print()
    print(message, "Seconds")
    print("--------------------------------------------------------------------------------------")

input("Program complete please press Enter to exist")

