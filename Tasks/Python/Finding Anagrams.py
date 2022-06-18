# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

word=input("Please type your first word here: ")
anagram= input("Please type your second word here: ")

def find_anagram(word, anagram):
    if (sorted(word) == sorted(anagram)):
        print(True) # [assignment] Add your code here
    else: 
        print(False)
    return True
find_anagram