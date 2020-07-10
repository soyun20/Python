line = 'The general pattern to count the words'
print(line.split())

counts = dict()
line = 'The general pattern to count the words in a line of text is to split the line into words, then loop through the words and use a dictionary to track the count of each word independently.'
words=line.split()
print('Words:',words)

for word in words:
    counts[word]=counts.get(word,0)+1
print('Counts',counts)
