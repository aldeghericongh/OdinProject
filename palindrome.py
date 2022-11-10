def onlyalnum(word): # Return alphanumeric valid chars
    letters = ""
    for char in word: #Check char by char
        if char.isalnum(): # Check if each char is a letter or number
            letters += char # If it is a alphanumeric, concatenate the char
    return letters.lower()

def isPalindrome(word):
    word = onlyalnum(word)
    return word[::-1] == word # Check inverted word with normal word

print("Enter a word: ")
word = input()
print("{0} is{1}a Palindrome. ".format(word, " " if isPalindrome(word) else " not "))