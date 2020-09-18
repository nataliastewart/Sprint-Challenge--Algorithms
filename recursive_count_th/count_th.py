'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
# if the len(word) is less then 2 "th"
    if len(word) < 2:
        return 0
#  slice word -> if the string is in the first part of the word in the first two indexes (0 , 1) : 2 
    elif word[:2] == 'th':
        return 1 + count_th(word[1:])
    else:
# look in the remaining of the string AFTER the second index (1) 
        return count_th(word[1:])