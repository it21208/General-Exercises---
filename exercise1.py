# count the frequency of each word with length larger than 4 characters in a given text file 
# and compute a list of words with the highest frequency of occurrence in the text

import collections

def mymethod(filepath):
    
    wordfreq = {}
    
    with open(filepath) as fp:
        line = fp.readline
        words = line.split()
        new_words = [i for i in words if len(i)>4]
        for word in new_words:
            if word not in wordfreq:
                wordfreq[word] = 0
        
        print('Dictionary of words: ', wordfreq)
        
        def top3words(text):
            counts = collections.Counter(text.split())
            return(counts.most_common(3))
        
        file = open(filepath, mode = 'r')
        fulltext = file.read()
        print(top3words(fulltext)) 

if __name__ == '__main__':
    filepath = 'home/pfb16181/text-file.txt'
    mymethod(filepath)
    print('Done')
