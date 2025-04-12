import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[\W_]', password))

    criteria_count = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    if criteria_count == 5:
        return "Strong"
    elif criteria_count >= 3:
        return "Moderate"
    else:
        return "Weak"

# Take password input from the user
password = input("Enter your password: ")
strength = check_password_strength(password)
print(f"The password strength is: {strength}")
