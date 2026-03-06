# Take input string from user
string = input("Enter a string: ")

# Initialize counters
vowels = 0
consonants = 0
spaces = 0
lowercase = 0

# Traverse each character in the string
for ch in string:
    
    # Check for vowels
    if ch in 'aeiouAEIOU':
        vowels += 1
    
    # Check for spaces
    elif ch == ' ':
        spaces += 1
    
    # Check for consonants (alphabet but not vowel)
    elif ch.isalpha():
        consonants += 1
    
    # Check for lowercase letters
    if ch.islower():
        lowercase += 1

# Display results
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
print("Number of spaces:", spaces)
print("Number of lowercase letters:", lowercase)