"""

Our first problem is about identifying the "majority" element in a list. 
The "majority element" in a list is an element that appears more than n / 2 times. *
Given a list of integers, our aim is to identify the majority element.

This problem could arise on numerous occasions. Imagine running a survey where
each participant selects a number from 1 to n to rate a product. After the survey, you want
to find out if there is a feature that received more than n / 2 votes. Or,
consider an internet voting system for an online event. 
You may need to identify if a candidate is leading by more than half the total votes.
"""

def solution(listA):
    count_dict = {}
    for element in listA:
        count_dict[element] = count_dict.get(element, 0) + 1
        if count_dict[element] > len(listA) // 2:
            return element
    return -1