"""
Math and Variables Lab
By: Chica Gomes
CSCI 110 Lab
Date: September 10th
 
Read and solve: Add Two Numbers - https://open.kattis.com/problems/addtwonumbers 
 
Algorithm steps:
  1. Read data as a line
  2. Split the line into two integers
  3. Add them up
  4. print the result
"""
def main():
    #read data
    line = input()
    #split the data into two numbers 
    a, b = line.split()
    #check to see if split correctly 
    #print (f'{a=},{b=}') #FIXME 1: comment/remove this line before submitting to kattis 
    #FIXME 2: convert string a into integer 
    a = int(a)
    b = int(b)
    #FIXME 3: convert string b into integer 
    ans=int(a+b)
    print(ans)
    #FIXME 4: add two numbers and store the result into ans variable
    #FIXME 5: print the answer as shown as sample ouput 
main()#call main function
