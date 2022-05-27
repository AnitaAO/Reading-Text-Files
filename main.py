# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from fileinput import filename


def read_file_content(filename):
    # [assignment] Add your code here 
    with open("story.txt", 'r') as filename:
        filename = filename.read
    
    output = read_file_content('story.txt')
    print(output)


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    
    text=filename.split()
    print(text)
    text=filename.strip("punctuations")

    #the recreating dictionary
    count={}
    for text in filename:
        if text in count.keys():
            count[text]+=1

    else:
        count[text]=+1

    print(count)

   