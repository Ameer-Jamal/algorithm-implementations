import timeit

print()
print("//////////////////////////////////////////////////////////////////////////////////////")
print("//////////////////////////////////////////////////////////////////////////////////////")
print("Program written by Ameer Jamal 20180381\n")
print("Program written in Python 3.9.5 with imported libraries:  Timeit")
print()


def longestPalindrome(X, Y, m, n, T):
    # return an empty string if the end of either sequence is reached
    if m == 0 or n == 0:
        return ""

    # If the last character of `X` and `Y` matches
    if X[m - 1] == Y[n - 1]:
        # append current character (`X[m-1]` or `Y[n-1]`) to LCS of
        # substring `X[0…m-2]` and `Y[0…n-2]`
        return longestPalindrome(X, Y, m - 1, n - 1, T) + X[m - 1]

    # otherwise, if the last character of `X` and `Y` are different

    # if a top cell of the current cell has more value than the left
    # cell, then drop the current character of string `X` and find LCS
    # of substring `X[0…m-2]`, `Y[0…n-1]`

    if T[m - 1][n] > T[m][n - 1]:
        return longestPalindrome(X, Y, m - 1, n, T)

    # if a left cell of the current cell has more value than the top
    # cell, then drop the current character of string `Y` and find LCS
    # of substring `X[0…m-1]`, `Y[0…n-2]`

    return longestPalindrome(X, Y, m, n - 1, T)


# Function to find the length of LCS of substring `X[0…n-1]` and `Y[0…n-1]`
def LCSLength(X, Y, n, T):
    # Fill the lookup table in a bottom-up manner.
    # The first row and first column of the lookup table are already 0.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # if current character of `X` and `Y` matches
            if X[i - 1] == Y[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1

            # otherwise, if the current character of `X` and `Y` don't match
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])

    print("--------------------------------------------------------------------------------------")
    print("The table for this LCS is:")

    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in T]))
    print("--------------------------------------------------------------------------------------")

    return T[n][n]


print("//////////////////////////////////////////////////////////////////////////////////////")
print("///////////////////////////AMEER LONGEST PALINDROME///////////////////////////////////")
print("//////////////////////////////////////////////////////////////////////////////////////")
print()
X = input("please input a sequence to get the LPS for: ")
print("--------------------------------------------------------------------------------------")

# string `Y` is a reverse of `X`
Y = input("please input a second to get the LPS for: ")#X[::-1]
# `T[i][j]` stores the length of LCS of substring `X[0…i-1]` and `Y[0…j-1]`
T = [[0 for x in range(len(X) + 1)] for y in range(len(X) + 1)]
# find the length of the LPS using LCS

# Start timer
startTimer = timeit.default_timer()

print("The length of the longest palindromic subsequence is: ",
      LCSLength(X, Y, len(X), T))
print("--------------------------------------------------------------------------------------")

# print the LPS using a lookup table
print("The longest palindromic subsequence is: ",
      longestPalindrome(X, Y, len(X), len(X), T))
print("--------------------------------------------------------------------------------------")

# Stop timing
intTime = "%.5f" % ((timeit.default_timer() - startTimer) * 1)
message = "Ameer Elapsed Time: " + str(intTime)
# print timing results
print()
print(message, "Seconds")
print("--------------------------------------------------------------------------------------")

input("Program complete please press Enter to exist")
