def longestCommonPrefix(wordList):
    if not wordList:
        return ""
    prefix = min(test, key=len)
    for i in range(1, len(wordList)):
        while(wordList[i].index(prefix) != 0):
            prefix[:len(prefix) - 1]
    return prefix

test = ["flower", "flow", "flight"]
# pre = min(test, key=len)
# for i, c in enumerate(pre):
#     for words in test:
#         if word[i] != c:
#             return pre[:i]

# return(pre)

# if not wordList:
#         return ""
#     prefix = min(test, key=len)
#     for i, c in enumerate(prefix):
#         for word in test:
#             if word[i] != c:
#                 return prefix[:i]
#     return prefix    

print(longestCommonPrefix(test))


# word = ["flower", "flow", "flight"]
# test = min(word, key=len)
# for i in range(len(word)-1):
#     print(word[i].index(test))

#Algorithm
#1 Set the min word in the list of words to be the prefix
#2 loop through every word in the list of word and find the index of the prefix in that word,
#using the wordList[word].index(prefix). if it's not 0, remove a letter from the back of the prefix and 
#run the loop again, return prefix when done.