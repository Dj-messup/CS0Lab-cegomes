"""
Lists and Unittest Lab
Updated By: Chica Gomes
CSCI 110 Lab
Date: Oct 18

Read and solve - Pet: https://open.kattis.com/problems/pet 

Algorithm steps:
    1. Create a list to store the total scores of each contestant
    2. Repeat 5 times:
        i. Read the input line
        ii. Split the line into a list of numbers
        iii. Convert the list of strings into a list of ints
        iv. Sum the list of ints
        v. Append the sum to the list of scores
    3. Find the max score in the list of scores
    4. Find the index of the max score in the list of scores
    5. Print the index of the max score + 1 and the max score
"""


from typing import List

def main() -> None:
    """Main function that solves the problem
    """
    # Step 1: Create a list to store the total scores of each contestant
    scores = []
    
    # Step 2-6: Repeat the following 5 times
    for _ in range(5):
        # Step 2: Read the input line as a list of integers using get_data function
        input_data = get_data()
        
        # Step 3: Find the sum of scores using list_sum function
        line_sum = list_sum(input_data)
        
        # Step 4: Append the sum to the list of scores
        scores.append(line_sum)
    
    # Step 5: Calculate the winner
    winner = answer(scores)
    
    # Step 6: Print the winner
    print(f"The winner is contestant {winner[0]} with a total score of {winner[1]} points.")

def get_data() -> List[int]:
    """Reads the data from std input and returns it as a list of ints
    Returns:
        List[int]: list of ints
    """
    input_data = []
    for _ in range(5):
        line = input("Enter 4 grades for a contestant: ")
        contestant_grades = [int(grade) for grade in line.split()]
        input_data.extend(contestant_grades)
    return input_data

def list_sum(numbers: List[int]) -> int:
    """Finds and returns the sum of the numbers in the list.
    Args:
        numbers: List[int]: takes a list of numbers as a parameter

    Returns:
        int: sum of the numbers in the list
    """
    return sum(numbers)  # Find the sum of the numbers in the list and return it

def answer(scores: List[int]) -> List[int]:
    """Calculates the winner of the show based on the highest score.
    Args:
        scores (List[int]): List of 5 contestants' scores

    Returns:
        List[int]: winner's number and points
    """
    max_score = max(scores)
    winner_number = scores.index(max_score) + 1
    return [winner_number, max_score]  # Return the winner's number and points as a list

if __name__ == "__main__":
    main()
