# Ameer Jamal 20180381 Sorting Assignment for Algorithms and Design
# This program is made in python 3.9.5 the latest as of july 6th 2021
import random  # we will need this for the declaration of a random array
import timeit  # we will need this for the timing of the functions
from statistics import mean  # This will be use in the sort_time_tester function to take the mean of all times


# First we will be defining all the algorithms needed
def original_quick_sort(UnSortedArray):
    # If the length of the array after recursion gets to one then return the array
    length = len(UnSortedArray)
    if length <= 1:
        return UnSortedArray
    else:
        # Make the pivot last number in the array and delete it (basically pivot = UnSortedArray.pop)
        pivot = UnSortedArray[length - 1]
        del UnSortedArray[length - 1]

    # Defining two arrays for the numbers smaller than the pivot and the numbers Larger
    numbers_greater = []
    numbers_lower = []

    # If the number is bigger than the pivot append it  in the numbers greater than pivot array
    # Else it would mean the number is smaller so append the number in the less than pivot array
    for number in UnSortedArray:
        if number > pivot:
            numbers_greater.append(number)

        else:
            numbers_lower.append(number)
    # Recursively call the sorting algorithm for each of the bigger than pivot and smaller than pivot array
    # while concatenating them with the pivot itself between them
    return original_quick_sort(numbers_lower) + [pivot] + original_quick_sort(numbers_greater)


# the difference between the original and the other quicksort implementations is mainly
# what pivot we are selecting and how to select it
def median_quick_sort(UnSortedArray):
    length = len(UnSortedArray)
    if length <= 1:
        return UnSortedArray
    else:
        # to take the median as the pivot we will take the first element
        # last element and middle element then sort them and choose the middle element
        # as our pivot point this will help in cases such as a sorted or reversed array
        mid = int(length / 2)
        right = length - 1
        left = 0
        # From my research to take full advantage of median quick sort we must sort the first middle and last value
        # in the array and here is a couple of if statements to do that
        if UnSortedArray[right] < UnSortedArray[left]:
            # in python we can swap elements using the x,y = y,x method
            UnSortedArray[right], UnSortedArray[left] = UnSortedArray[left], UnSortedArray[right]
        if UnSortedArray[mid] < UnSortedArray[left]:
            UnSortedArray[mid], UnSortedArray[left] = UnSortedArray[left], UnSortedArray[mid]
        if UnSortedArray[right] < UnSortedArray[mid]:
            UnSortedArray[right], UnSortedArray[mid] = UnSortedArray[mid], UnSortedArray[right]

        pivot = UnSortedArray[mid]
        del UnSortedArray[mid]

    numbers_greater = []
    numbers_lower = []

    for numbers in UnSortedArray:
        if numbers > pivot:
            numbers_greater.append(numbers)

        else:
            numbers_lower.append(numbers)

    return median_quick_sort(numbers_lower) + [pivot] + median_quick_sort(numbers_greater)


def random_quick_sort(UnSortedArray):
    length = len(UnSortedArray)
    if length <= 1:
        return UnSortedArray
    else:
        # here we take the pivot point to be a random value between 0 and the last index
        # of the array
        randomValue = random.randint(0, length - 1)
        pivot = UnSortedArray[randomValue]
        del UnSortedArray[randomValue]

    numbers_greater = []
    numbers_lower = []

    for numbers in UnSortedArray:
        if numbers > pivot:
            numbers_greater.append(numbers)

        else:
            numbers_lower.append(numbers)

    return random_quick_sort(numbers_lower) + [pivot] + random_quick_sort(numbers_greater)


# this will be a non recursive insertion sort implementation
def insertion_sort(UnSortedArray):
    # For i in range between 1 and length
    # (1 because we assume the 0 index to be sorted)
    # go through the array
    for i in range(1, len(UnSortedArray)):
        # here we are preserving the value of i in a key called savedValue
        # as when shifting we don't want to lose that value
        savedValue = UnSortedArray[i]
        # We then move the j counter to j-1
        j = i - 1
        # another loop is used to see if the savedValue is bigger or smaller than the
        # array at j value index it will then either shift and swap the values if the savedValue is smaller
        # this will happen in a loop to shift the entire array forward or if the number is bigger
        # then we will skip the loop and go onto swapping the j+1 value with the saved value
        while j >= 0 and savedValue < UnSortedArray[j]:
            UnSortedArray[j + 1] = UnSortedArray[j]
            j -= 1
        UnSortedArray[j + 1] = savedValue
    # after this process is complete all the numbers will be sorted , we  will then return the array
    return UnSortedArray


# This function will be able to automate comparison testing between algorithms
# it will run each sort many times (depending on the iterations parameter)
# and also depending on the type wanted , random or sorted or reversed
# and take the avg overall time and display it
# for timing purposes I will be using the "timeit" library as it remains accurate for quicker runtimes
# when compared to the standard time.time() in python
def sort_time_tester(iterations, arrayType, amount):
    # this is to check and display the type of array in the output
    if arrayType == 's':
        arrayTypeWord = "Sorted"
    elif arrayType == 'r':
        arrayTypeWord = "Reversed"
    else:
        arrayTypeWord = "Random"

    # define an array to store each run time we will need to redefine this array
    # after every algorithm run through to reEmpty and recalculate the values
    timings = []


    # loop for the amount passed in through the iteration argument
    for x in range(1, iterations):
        UnsortedArray = [random.randint(1, 9999) for _ in range(amount)]
        # Checking if we would like to use a sorted , reversed or random array
        # we will need to check each time to make sure the array is never sorted before entering
        # any of the algorithms
        if arrayType == 's':
            UnsortedArray.sort()
        elif arrayType == 'r':
            UnsortedArray.sort(reverse=True)
        else:
            UnsortedArray = [random.randint(1, 9999) for _ in range(amount)]
        # Start timer
        startTimer = timeit.default_timer()
        original_quick_sort(UnsortedArray)
        # Stop timing
        # we multiply the time taken by 10^6 to get it in microseconds for easier readability
        # and take it to six significant figures
        timeTaken = "%.6f" % ((timeit.default_timer() - startTimer) * 10000000)
        # after the time has been take we append it to the array we declared earlier
        timings.append(timeTaken)
    # We format the array into a float so we can use and pass
    # it through the mean() function provided by the statistics library
    timingsToFloat = [float(numeric_string) for numeric_string in timings]
    print(mean(timingsToFloat))
    print("is the Average MicroSeconds taken for original quick sort to run over " + str(
        iterations) + " iterations for " + arrayTypeWord + " values")
    print("=====================================================================")

    # emptying the array
    timings = []
    # repeat the same process as before just changing the type of sort being run
    # loop for the amount passed in through the iteration argument
    UnsortedArray = [random.randint(1, 9999) for _ in range(amount)]
    for x in range(1, iterations):
        # Checking if we would like to use a sorted , reversed or random array
        if arrayType == 's':
            UnsortedArray.sort()
        elif arrayType == 'r':
            UnsortedArray.sort(reverse=True)
        else:
            UnsortedArray = [random.randint(1, 9999) for _ in range(amount)]
        # Start timer
        startTimer = timeit.default_timer()
        random_quick_sort(UnsortedArray)
        # Stop timing
        timeTaken = "%.2f" % ((timeit.default_timer() - startTimer) * 10000000)
        timings.append(timeTaken)

    timingsToFloat = [float(numeric_string) for numeric_string in timings]
    print(mean(timingsToFloat))
    print("is the Average MicroSeconds taken for random quick sort to run over " + str(
        iterations) + " iterations for " + arrayTypeWord + " values")
    print("=====================================================================")

    # emptying the array
    timings = []

    # loop for the amount passed in through the iteration argument
    for x in range(1, iterations):
        # the reason here that the checking array type is in the for loop is because
        # throughout the median sort there is a change in position of the values
        # this will insure reRandomizing of values everytime
        UnsortedArray = [random.randint(1, 9999) for _ in range(amount)]
        # Checking if we would like to use a sorted , reversed or random array
        if arrayType == 's':
            UnsortedArray.sort()
        elif arrayType == 'r':
            UnsortedArray.sort(reverse=True)
        else:
            UnsortedArray = [random.randint(1, 9999) for _ in range(amount)]

        # Start timer
        startTimer = timeit.default_timer()
        median_quick_sort(UnsortedArray)
        # Stop timing
        timeTaken = "%.2f" % ((timeit.default_timer() - startTimer) * 1000000)
        timings.append(timeTaken)

    timingsToFloat = [float(numeric_string) for numeric_string in timings]
    print(mean(timingsToFloat))
    print("is the Average MicroSeconds taken for median quick sort to run over " + str(
        iterations) + " iterations for " + arrayTypeWord + " values")
    print("=====================================================================")

    # emptying the array
    timings = []
    # loop for the amount passed in through the iteration argument
    for x in range(1, iterations):
        # the reason here that the checking array type is in the for loop is because
        # after the first insertion sort the array will be sorted
        # so this will insure reRandomizing of values everytime/sorting/reversing
        UnsortedArray = [random.randint(1, 9999) for _ in range(amount)]
        # Checking if we would like to use a sorted , reversed or random array
        if arrayType == 's':
            UnsortedArray.sort()
        elif arrayType == 'r':
            UnsortedArray.sort(reverse=True)
        else:
            UnsortedArray = [random.randint(1, 9999) for _ in range(amount)]

        # Start timer
        startTimer = timeit.default_timer()
        insertion_sort(UnsortedArray)
        # Stop timing
        timeTaken = "%.2f" % ((timeit.default_timer() - startTimer) * 10000000)
        timings.append(timeTaken)

    timingsToFloat = [float(numeric_string) for numeric_string in timings]
    print(mean(timingsToFloat))
    print("is the Average MicroSeconds taken for insertion sort to run over " + str(
        iterations) + " iterations for " + arrayTypeWord + " values")
    print("=====================================================================")
















# Driver code:
# define an array of integers with size of amount with values from 1 to 9999
amount = 250
array = [random.randint(1, 500) for _ in range(amount)]
# Checking if we would like to use a sorted , reversed or random array
arrayType = input('Please enter \n\'s\' for sorted array \n\'r\' for reversed array \n or press enter for a random '
                  'array:')
if arrayType == 's':
    array.sort()  # we are using the built in sort function in python
elif arrayType == 'r':
    array.sort(reverse=True)  # here the built in sort function takes in a argument that reverses the array

# this is to check and display the type of array in the output
if arrayType == 's':
    arrayTypeWord = "Sorted"
elif arrayType == 'r':
    arrayTypeWord = "Reversed"
else:
    arrayTypeWord = "Random"

print()
print("=====================================================================")
print("The amount of numbers in the array to be tested are ", amount)
print("this sorting will be done on " + arrayTypeWord + " values")
print("=====================================================================")


# For all the methods below we will be using the exact same technique, only changing the sort type
print("======================METHOD 1 ORIGINAL QUICKSORT======================")
# Here we print the array as original
print("Ameer UnSorted Array: ")
print(array)
print()

# Here we will be timing the run time of the sort using the timeit library
startTimer = timeit.default_timer()  # Starts the timer

sortedArray = original_quick_sort(array)  # Runs the sort

# Stops the timer by subtraction of the current time from the start time
# We multiply by 10^6 to get time in microseconds as its easier to read
intTime = "%.2f" % ((timeit.default_timer() - startTimer) * 1000000)
message = "Ameer Elapsed Time: " + str(intTime)  # defines the amount of time taken as a message

# Prints the sorted Array
print("Ameer Sorted Array: ")
print(sortedArray)
print(message, "Microseconds")  # prints the time taken message
print()

print("======================METHOD 2 RANDOM QUICKSORT======================")
print("Ameer UnSorted Array: ")
print(array)
print()

# Start timer
startTimer = timeit.default_timer()
sortedArray = random_quick_sort(array)
# Stop timing
intTime = "%.2f" % ((timeit.default_timer() - startTimer) * 1000000)
message = "Ameer Elapsed Time: " + str(intTime)
print("Ameer Sorted Array: ")
print(sortedArray)
# print timing results
print(message, "Microseconds")
print()

print("======================METHOD 3 MEDIAN QUICKSORT======================")

print("Ameer UnSorted Array: ")
print(array)
print()

# Start timer
startTimer = timeit.default_timer()
sortedArray = median_quick_sort(array)
# Stop timing
intTime = "%.2f" % ((timeit.default_timer() - startTimer) * 1000000)
message = "Ameer Elapsed Time: " + str(intTime)
print("Ameer Sorted Array: ")
print(sortedArray)
# print timing results
print(message, "Microseconds")
print()

print("======================METHOD 4 INSERTION SORT======================")
if arrayType == 'r':
    array.sort(reverse=True)

print("Ameer UnSorted Array: ")
print(array)
print()

# Start timer
startTimer = timeit.default_timer()
sortedArray = insertion_sort(array)
# Stop timing
intTime = "%.2f" % ((timeit.default_timer() - startTimer) * 1000000)
message = "Ameer Elapsed Time: " + str(intTime)
print("Ameer Sorted Array: ")
print(sortedArray)
# print timing results
print(message, "Microseconds")

print("=====================================================================")
print()
print("=====================================================================")
print("The amount of numbers in the array to be tested are ", amount)
print("=====================================================================")
# after each of the sort algorithms run we call the sort_time_tester() function to
# get a better sense of timing, we will iterate these same algorithms a thousand times
# and take an average of their time , for better statistics
sort_time_tester(1000, arrayType, amount)

input("please press enter to close")
