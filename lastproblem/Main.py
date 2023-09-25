'''
    User-defined functions and unittest lab
     Updated By: Chica Gomes
     CSCI 110 Lab
     Date: September 21st 
     
Read and solve - The Last Problem: https://open.kattis.com/problems/thelastproblem

Algorithm:
1. Read the input string using function
2. read the data as an input and return the first fruitful function
3. Create the output as asked and print it using function
4. run the codes/fruitful functions through main and store it into an answer variable
5. print answer variable and call main function
6. test the main function in test_main.py by importing Main
'''
 
import sys


def main():
    """Main function that solves the problem.
    """
    # Call answer function passing data as an argument
    data=read_data()
    # store the returned result into ans variable
    ans=answer(data)
    #print the result
    print(ans)
    return 0


def read_data() -> str:
    """Reads the twilight data from std input and returns it.
    Returns:
      str: data read from std input
    """
    S=input()
    return S
    # read and store the input line into data variable
    # return data
    


def answer(data: str) -> str:
    """Creates the twilight output and returns it.
    Args:
      data (str): name of the person
    Returns:
      str: twilight output
    """
    # create the output as asked and store it into ans variable
    ans = "Thank you, "+data+", and farewell!"
    return ans


if __name__ == "__main__":
    main()
    # call main function
    
