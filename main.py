# Read text from a file, and count the occurence of words in that text
# Example
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from ast import Return
from collections import Counter
from fileinput import filename
from importlib.resources import contents


import os
import sys 
with open(os.path.join(sys.path[0], 
"story.txt"), "r") as f: 
    print (f.read())

def read_file_content():
    # [assignment] Add your code here 
    content = f.read()

    return content   
print(f)

def count_words():
    text = read_file_content('./story.txt')
    # [assignment] Add your code here
    words = text.split()
    print(words)
    count = dict()
    
    for word in words:
        if word in count.keys():
            count[word] += 1
        else:
            count[word] = 1
    return count
print(count_words())