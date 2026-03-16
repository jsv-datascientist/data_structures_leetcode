"""
As a software developer in an HR or Finance team,
you might need to work on tasks related to personnel management.
For instance, suppose your firm has just approved a new policy to give all developers
a bonus equal to 10% of their salary. Your task is to update the database to reflect this new policy


Soln 
An initial thought might be to create a new list of dictionaries, 
where each dictionary contains an employee's information and the calculated bonus
if the employee's role is 'developer'. However, creating a new list and new dictionaries
would represent an unnecessary allocation of extra memory. Besides, 
copying data may risk data inconsistency if the original data is updated during the process. 
Therefore, we need to find a method that doesn't involve duplicating our data.

An efficient approach here is to add a 'bonus' field to the dictionary of
each employee who is a developer, updating the ones we 
already have instead of creating new dictionaries. Therefore, we can avoid duplicating the data list.
"""

def bonus_calculator(employees):
    
    for emp in employees:
        bonus = 0
        if emp["role"] == "developer":
            bonus = emp["salary"] * 0.10
        emp["bonus"] = bonus
    return employees