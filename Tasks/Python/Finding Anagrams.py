# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

word=input("Please type your first word here:\n")
anagram=input("Please type your second word here:\n")
def find_anagram(word, anagram):
    if (sorted(word.lower()) == sorted(anagram.lower())):
        print(True)
    else: 
        print(False)
    return True

find_anagram(word, anagram)