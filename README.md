# Password Strength Checker

## Description
This Python script evaluates the strength of a password based on security best practices. It helps ensure strong password policies for applications requiring secure authentication.

### Features
- Checks password strength based on:
  - Minimum length (8 or more characters)
  - Presence of uppercase letters
  - Presence of lowercase letters
  - Presence of numbers
  - Presence of special characters
- Categorizes passwords as **Weak**, **Moderate**, or **Strong**
- Accepts user input for real-time evaluation
- Useful for authentication systems and cybersecurity-focused projects

### Usage
1. Run the script.
2. Enter a password when prompted.
3. The script evaluates the password and provides strength feedback.

---

## Code
```python
import re

def check_password_strength(password):
    length_criteria = len(password) >= 16
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
