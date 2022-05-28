# This scipt reads from a file and counts all words

file = open (r"C:\Users\aearn\Desktop\Github\Zuri\Tasks\Python\LETTER.docx", encoding="cp437")
data = file.read()
words = data.split()


print('Number of words in text file :', len(words))