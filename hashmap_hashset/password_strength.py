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
    special_characters = "!@#$%^&*()-+"
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
        elif password.isupper():
            strength["upper"] = True
        else:
            pattern = '[' + re.escape(special_characters) + ']'
            strength["special_char"] = bool(re.search(pattern, password))
        #results.append(strength)
    return strength



def multi_password_strength_counter(passwords):
    special_characters = "!@#$%^&*()-+"

    results = []
    
    for password in passwords:
        strength = {
            "length": False,
            'digit': False,
            'lowercase': False,
            "uppercase": False,
            'special_char': False
        }
        if len(password) >= 8:
            strength["length"] = True
            
        for char in password: 
            if char.isdigit():
                strength["digit"] = True
            elif char.islower():
                strength["lowercase"] = True 
            elif char.isupper():
                strength["uppercase"] = True
            else:
                strength["special_char"] = char in special_characters
        results.append(strength)

    return results
    
passwords = ["password", "Pa$$w0rd", "SuperSecurePwd!", "weakpw"]
results = multi_password_strength_counter(passwords)
for result in results:
    print(result)

# The expected output is:
# {'length': True, 'digit': False, 'lowercase': True, 'uppercase': False, 'special_char': False}
# {'length': True, 'digit': True, 'lowercase': True, 'uppercase': True, 'special_char': True}
# {'length': True, 'digit': False, 'lowercase': True, 'uppercase': True, 'special_char': True}
# {'length': False, 'digit': False, 'lowercase': True, 'uppercase': False, 'special_char': False}