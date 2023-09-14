'''
    Built-in and library functions Lab
    Updated By: Chica Gomes 
    CSCII 110 Lab
    Date: Sep 12 2023 
   Solution to Kattis problem - Buka: https://open.kattis.com/problems/buka

Algorithm steps:
  1. read the first line or 1st operand into a variable
  3. read the 2nd line or operator/symbol into a variable
  3. read the 3rd line or 2nd operand into a variable
  4. concatenate the variables into a single string
  5. use the built-in eval function on the concatenated string
  6. print the result of the eval as the answer
'''
import sys

# define a main function
def main():
  """Main function that solves the problem
  """
  # read/input the first operand into A variable using sys library's readline() method
  A = sys.stdin.readline().strip()
  symbol=sys.stdin.readline().strip()
  B = sys.stdin.readline().strip()
  # using sys library, read/input the 2nd line into operator variable
  print(f'{A=}', file=sys.stderr)
  # using sys library, read/input the 2nd operand into symbol variable
  print(f'{symbol=}', file=sys.stderr)
  # using sys library, read/input the 2nd operand into B variable
  print(f'{B=}', file=sys.stderr)
  # concatenate all three variables into a single variable called equation
  equation=(A+symbol+B)
  # call eval(equation) and assign the return value or result into ans variable
  ans=eval(equation)
   #find the answer using eval function
  # print the answer using sys library's stdout.write() method
  sys.stdout.write(f'{ans}\n') 
main()