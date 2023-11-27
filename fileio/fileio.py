"""
File I/O Lab
By: Chica Gomes

CSCI 110
Date: unknown

Program prompts user to enter name of the file that contains 10 integers.
It opens, reads and stores the numbers into a list.
Program will then sort the numbers in the list in ascending and descending orders
Program will then print the sorted lists to an output file along with the 
largest and smallest values in the list.

NOTE: All fixme's are each worth 10 points except for the FIXME1 which is worth 20 points
"""

from typing import List

totalInts = 10


def readData() -> List[int]:
    intList = []
    file_name = input("Enter the name of the file: ")
    try:
        with open(file_name, 'r') as file:
            for line in file:
                intList.append(int(line.strip()))
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    return intList


def sortListInAscendingOrder(lstInts: List[int]):
    lstInts.sort()


def sortListInDescendingOrder(lstInts: List[int]):
    lstInts.sort(reverse=True)


def printList(printFile, lstInts: List[int]):
    for n in lstInts:
        printFile.write(str(n) + '\n')
    printFile.write('\n')


def main():
    # No need to assign an empty list here
    integers = readData()

    outputFileName = input('Enter a file to write output to: ')
    printFile = open(outputFileName, 'w')

    printFile.write("Numbers entered:\n")
    printList(printFile, integers)

    # Sort numbers
    sortListInAscendingOrder(integers)
    printFile.write("Numbers sorted in ascending order:\n")
    printList(printFile, integers)

    # Call sortListInDescendingOrder function
    sortListInDescendingOrder(integers)

    # Write the sorted list in descending order to the output file
    printFile.write("Numbers sorted in descending order:\n")
    printList(printFile, integers)

    # Print the largest number to the output file
    printFile.write("Largest number: {}\n".format(max(integers)))

    # Print the smallest number to the output file
    printFile.write("Smallest number: {}\n".format(min(integers)))

    printFile.close()
    print('Done executing the program! Check the output file for results.')


if __name__ == "__main__":
    main()
