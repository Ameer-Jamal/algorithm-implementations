import sys

def fibRec(number):
    if number == 1 or number == 2:
        return 1
    else:
        return fibRec(number - 1) + fibRec(number - 2)


def fibDyn(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b


# code
# A Dynamic Programming based Python
# Program for 0-1 Knapsack problem
# Returns the maximum value that can
# be put in a knapsack of capacity W


def knapSackProfit(W, wt, val, n):
    dp = [0 for i in range(W + 1)]  # Making the dp array

    for i in range(1, n + 1):  # taking first i elements
        for w in range(W, 0, -1):  # starting from back,so that we also have data of
            # previous computation when taking i-1 items
            if wt[i - 1] <= w:
                # finding the maximum value
                dp[w] = max(dp[w], dp[w - wt[i - 1]] + val[i - 1])

    return dp[W]  # returning the maximum value of knapsack
def knapSackElements(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    res = K[n][W]
    print("The result is " + str(res))
    print("the elements are:")

    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break

        if res == K[i - 1][w]:
            continue
        else:
            print("element of weight of : " + str(wt[i - 1]))

            res = res - val[i - 1]
            w = w - wt[i - 1]







val = [0,3,6,2,1]
wt = [0,1,3,4,5]
W = 8
n = len(val)

# print(str(fibDyn((10))))




knapSackElements(W, wt, val, n)

print("-------------------------------")

# Dynamic Programming Python implementation of Matrix
# Chain Multiplication. See the Cormen book for details
# of the following algorithm


