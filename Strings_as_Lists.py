#### Listing a Sentence
bonjour='Hello World!'
for letter in bonjour:
    print(letter)

# #### Sentence List
print(list(bonjour))

# #### Sentence Slices
firstFive=(bonjour[:5])
MiddleFive=(bonjour[2:7])
LastFive=(bonjour[-5:])
print(firstFive,MiddleFive,LastFive)

# #### Finding Python

sentence='Hello people of Python, I hate snake but I love Python!'
print('Python' in sentence)
print(sentence.find('Python'))
print(sentence.rfind('Python'))
print(sentence.count('Python'))
splitSentence=sentence.split(' ')
print(splitSentence)
for word in splitSentence:
    print(word)
print(sentence.replace('Python', 'Ruby'))
