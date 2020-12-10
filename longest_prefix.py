#Algorithm
#1 Set the min word in the list of words to be the prefix
#2 loop through every word in the list of word and find the index of the prefix in that word,
#using the wordList[word].index(prefix). if it's not 0, remove a letter from the back of the prefix and 
#run the loop again, return prefix when done.

def longestCommonPrefix(wordList):
    if not wordList:
        return "" ##return " " if input is not valid
    prefix = min(wordList, key=len) ##get the smallest word in the input array
    for i, c in enumerate(prefix):
        for word in wordList:
            if word[i] != c:
                return prefix[:i]


test = ["flower", "flow", "flight"]

print(longestCommonPrefix(test))
