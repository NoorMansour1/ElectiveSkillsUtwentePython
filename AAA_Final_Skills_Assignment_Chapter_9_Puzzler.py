"""Excersise 9-7 from Chapter 9; aka the elective skills goal.

Assignment description:
This question is based on a Puzzler that was broadcast on the radio program Car
Talk (http://www.cartalk.com/content/puzzlers): Give me a word with three
consecutive double letters. I’ll give you a couple of words that almost qualify,
but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. 5/3
It would be great except for the ‘i’ that sneaks in there.
Or Mississippi: M-i-s-s-i-s-s-i-pp-i.7/3 If you could take out those i’s it
would work. But there is a word that has three consecutive pairs of letters and
to the best of my knowledge this may be the only word. Of course there are
probably 500 more but I can only think of one. What is the word? Write a program """

""" FOR REPLICATION PLEASE INSTALL word.txt from: http://thinkpython2.com/code/words.txt and put it into the same document where this python file will be located."""
fileinput = open("words.txt") #Word.txt file, which is a list of words is used to find the word

def Check3Double(word):
    """ Function that checks if a single word has consecutve double letters by using recursion"""
    if len(word) <= 5: # word has to be at least 6 letters
        return False
    if word[0] == word[1] and word[2] == word[3] and word[4] == word[5]: # Concerns the double letters as well as the consecutivness of them.
        return True
    else:
        return Check3Double(word[1:])

#print(Check3Double("PPPPPP"))

def ConsecutiveDoubleLetter(fileinput):
     for word in fileinput: #Checks each word in the list
        if Check3Double(word) == True:
            print(word)

ConsecutiveDoubleLetter(fileinput)
