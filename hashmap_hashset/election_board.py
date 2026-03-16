"""
Imagine you are in a corporate setting and you have a list of employee votes represented as integers like 
 These integers actually represent the IDs of your fellow employees. And yes, people can indeed vote for themselves!

An employee gets elevated to the exclusive board member position only if they bag at least n / 3 votes, with n being the total number of votes. Your task: find out the ID of this popular employee. If no one hits the vote mark, return -1. If multiple employees received at least n / 3 votes, return any of them!

The votes are delivered to you in list format. As an illustration, [1, 2, 3, 3, 3] means employees 1 and 2 voted for themselves, and employee 3 received three votes. Hang tight-there can be edge cases, such as no votes or everybody voting for themselves.

Your end goal is to return the lucky candidate's ID if they secure a seat on the board. If no one qualifies, return -1. 

 if there are 5 votes, 
5
/
3
=
1.666...
5/3=1.666....

If you round down, someone with just 1 vote would qualify, which isn't really "at least a third."
By rounding up (using ceil), you require 2 votes, which is the smallest integer greater than 
n/3

"""

def elect_board_member(votes):
    from collections import defaultdict
    import math
    
    vote_count = defaultdict(int)
    for vote in votes:
        vote_count[vote] += 1
        if vote_count[vote] >= math.ceil(len(votes) / 3):
            return vote
    return -1
        

print(elect_board_member([1, 2, 3, 3, 3]))  # Expected output: 3
print(elect_board_member([1, 2, 3, 4, 5]))  # Expected output: -1
print(elect_board_member([1, 1, 1, 2, 2, 3, 3, 3]))  # Expected output: 1