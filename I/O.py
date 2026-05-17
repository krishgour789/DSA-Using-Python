'''msg = "Hello This is Krish Gour and i am here ot help you in learning python programming language"
f = open("write.txt","w")
f.write(msg)
f.close()
'''
# f = open('write.txt','r')
# print(f.readlines(16))

"""Create a Project that will read a text file and count the number of words in it. The program should also display the most common word and its frequency."""

def count_words(file_name):
    with open(file_name,'r') as f:
        text = f.read()
        words = text.split()
        words_count = len(words)
        word_freq = {}
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

    return words_count
file_name = 'write.txt'
words_count = count_words(file_name)
print(f'The number of words in the file is: {words_count}')
