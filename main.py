# Read text from a file, and count the occurence of words in that text
# Example
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from ast import Return
from collections import Counter
from fileinput import filename
from importlib.resources import contents


file = open('./story.txt', 'r')
content = file.read()

def read_file_content():
    # [assignment] Add your code here 
    content = file.read()

    return content
    
print(content)
def count_words(content):
    counts = dict()
    text = content.split()

    for word in text:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


    # print(read_file_content("story.txt"))

def count_words(filename):
    
    text = read_file_content("story.txt")

    # [assignment] Add your code here
    counts = dict()
    text = filename.split()

    for word in text:

        if word in counts:
            counts() +- 1
        else:
            counts() - 1
    return counts