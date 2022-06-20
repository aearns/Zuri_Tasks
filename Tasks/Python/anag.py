input1 = input("Please type the first word:\n")
input2 = input("Please type the next word:\n")
def check(input1, input2):
    if(sorted(input1)==sorted(input2)):
        print("Yes! We have an anagram")
    else:
        print("Sorry, not an anagram")
check(input1, input2)


