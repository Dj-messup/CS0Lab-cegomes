"""
    StdI0 Lab
    ASCII Art - using literals and variables 

    Updated By: Chica Gomes #FIXME1
    Date: 08/31/2023 

    This program produces an ASCII art on the console. 

    Algorithm steps:
    1. Use variables to store data/values 
    2. Write a series of print statements to print the data/values to the console
"""
name = input("What is your name? ")
# FIXED: prompt user to enter their name and store the value into name variable using input function
# FIXED: greet the name using the variable as the following output
# must output: Nice meeting you, <name>!

# prompt user to enter the semester and store the value into semester variable using input function
print("Welcome ASCII Art Program...\n")
print("Nice meeting you,"+name)

# prompt user to enter the semester and store the value into semester variable using input function
semester: str = input("What semester is this [Fall/Spring]?")
print("This is "+semester+" semester.\n")

# FIXED: prompt user to enter the year and store the value into year variable using input function
# FIXED: print the year using the variable as the following output
# must output: This is <year> year.

year=input("What is the current year?")
print("This is "+year+ " year")

print("Hope you like my ASCII art...\n\n")

line1:str="   |\\_/|     **********************      (\\_/)"
print(line1)

line2:str="  / @ @ \    *     ASCII Lab      *     (='.'=) "
print(line2)

line3:str=" ( > 0 < )   *    Chica Gomes     *   ( ' )_( ' ) "
print(line3)

line4:str="   >>x<<     *       2023         * "
print(line4)

line5:str="  /  O  \    *      CSCI 111      * "
print(line5)

line6:str="             **********************"
print(line6)


 # FIXED: use variable to print the second line of the graphic 
 # FIXED: print the third line of the graphics 
 # FIXED: use variable to print the fourthline
 # FIXED: use variable to print the fifth line 
 #note you can add more lines or print more ASCII arts of your choice if you'd like 

print("Good bye"+name)
