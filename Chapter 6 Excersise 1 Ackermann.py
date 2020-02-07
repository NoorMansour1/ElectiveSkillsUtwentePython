"""given functions"""
def first(word):
    """ returns the first letter of a given word by choosing the first place in the array"""

    return word[0]

#print(first("bob"))
def last(word):
    """chooses last letter of an given word by choosing last
    letter of word (python Unique -1 is end of array)"""

    return word[-1]

def middle(word):
    """Chooses every letter of the word except
     the first and the second one"""

    return word[1:-1]

#print(middle(""))

def palindrom(word):
    if len(word)<=1:
        return True
    if first(word)!=last(word):
        return False

    print(" "*len(word),"Word length:",len(word))
    return palindrom(middle(word))

print(palindrom("abcddcba"))
