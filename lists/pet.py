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
    scores = []

    for _ in range(5):
        contestant_scores = get_data()
        total_score = list_sum(contestant_scores)
        scores.append(total_score)

    result = answer(scores)
    print(result)

def get_data() -> List[int]:
    str_nums = input().split()
    return [int(num) for num in str_nums]

def list_sum(numbers: List[int]) -> int:
    return sum(numbers)

def answer(scores: List[int]) -> str:
    max_score = max(scores)
    index = scores.index(max_score)
    # Return the index+1 and the max number in the list as a string
    return f"{index + 1} {max_score}"

if __name__ == "__main__":
    main()
