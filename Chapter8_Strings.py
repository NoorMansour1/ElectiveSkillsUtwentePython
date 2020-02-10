

def traverse_string(word):
    n=-1
    while True:
        letter= word[n]
        print(letter)
        if n== (-len(word)):
            break
        n = n-1

#traverse_string("Noor Mansour")

def traverse_for(word):
    for letter in word:
        print(letter)

#traverse_for("WTF")

def abecedarian():
    prefixes="JKLMNOPQ"
    for letter in prefixes:

        if letter== "O" or letter=="Q":
            suffix="uack"
        else:
            suffix="ack"

        print(letter+suffix)

#abecedarian()
fruit="banana"
#print(fruit[:])


def find(word,letter,start):
    index=start
    while index<len(word):
        if word[index]==letter:
            return letter
        index=index+1
    return -1

#print(find("Kanone","a",3))

def count(word,letter):
    count=0
    for place in word:
        if place==letter:
            count=count+1
    print(count)


"Excersise 8-2 --------------------------------------------------------"

word ="banana"

#print("Banana".count("a"))

"Excersise 8-3-------------------------------------------------------"
"One line is_palindrome with step size of -1"

#print(word[0:5:2])# ADDITIONAL THIRD INDEX IS USED FOR THE STEPS THAT ARE TAKEN

"Reverse writing with third Index"
#print(word[::-1])

def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

#print(is_palindrome("BOBOB"))

"Excersise 8-4 Caeser cypher-------------------------------------------------"
print(ord("a"))
chr(ord("A"))


def rotate_word(word, rotation):
    "Encrypts a string into ceaser cypher a with rotation -1 becomes z"
    word1 =word.lower()
    for letter in word1:
        newnumber=ord(letter)+rotation
        if newnumber > 122:
            newnumber= 96+ (newnumber-122)
        newword= chr(newnumber)
        print(newword,end="")

rotate_word("Uv gurer. Guvf vf abg ernyyl wbxr. Whfg univat fbzr sha jvgu gubfr jub pnag ebg13 na negvpyr Gb  ernyyl zrna, sbyybj-hc gb guvf negvpyr jvgu fbzrguvat yvxr Obl, gung jnf gur shaavrfg wbxr V rire urneq!",13)
