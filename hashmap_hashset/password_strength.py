"""
As an application developer, ensuring the security of user data is pivotal. A common measure to ensure robust 
security is testing the strength of passwords. A 'strong' password is usually defined as
one that is long (at least 8 characters) and includes a mix of uppercase characters, lowercase characters, and digit



A more polished and less time-consuming solution would be to traverse the password 
string just once while checking for all conditions. As we check each character, 
we can update a dictionary where each condition is a key, and its fulfillment (True or False) is the corresponding value.
This approach enables us to keep the code both elegant and efficient, making the best use of Python dictionaries.
"""

def password_strength_counter(password):
    strength = {
        "length" : False,
        "digit" : False,
        "lower": False,
        "upper": False
    }
    
    if len(password) >= 0:
        strength["length"] = True
        
    for char in password:
        if char.isdigit():
            strength["digit"]= True
        elif char.islower():
            strength["lower"] = True
        else:
            strength["upper"] = True
    return strength