"Excersise 9-1"
fin = open("words.txt")
# print(fin.readline())
# i = 0
# for line in fin:
#     print(line)
#     i += 1
#
# print(i)

def print_words_length():
    for line in fin:
        if len(line.strip(" ")) > 20:
            print(line)

#count_words()
"Excersise 9-2"
def has_no_e(word):
    for letter in word:
        if letter == "e":
            return False
    return True

# print(has_no_e("Okay"))

def print_words_without_e():
    "prints out the words from word.txt that have no e and computes the ratio of e words to all words"

    ew=0
    aw=0
    for words in fin:
        aw += 1
        if has_no_e(words) == True:
            print(words)
            ew += 1
    print(round((ew/aw)*100,2),"%")

#print_words_without_e()

"Excersise 9-3"
def avoids(word,forbidden_letters):
    "Returns True if word avoids string of forbidden letters"
    for letter in word:
        n = 1

        while n <= len(forbidden_letters):

            if letter == forbidden_letters[n-1:n]:

                return False

            n += 1

    return True

# print(avoids("Yes Boyyy","hhy"))

def uses_only(word,allowed_letters):
    for letter in word:
        if letter not in allowed_letters:
            return false

    return True

# def uses_all(word,required_letters):
#     for letter in required_letters:
#         if letter not in word:
#             return False
#
#     return True

def uses_all(word, required):
    return uses_only(required,word)


"Excersise 9-6 |----------------------------------------"
# print(ord("A"))
def is_abecedarian(word):
    l_word= word.lower()
    p_letter = "a"
    for letter in l_word:
        if p_letter > letter:
            return False
        p_letter = letter

    return True

print(is_abecedarian(""))
