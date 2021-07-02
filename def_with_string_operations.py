##Q = Given a non-empty string and an int n, return a new string where the character at index n has been removed. 
# The value of n will be a valid index of a character in the original string (i.e. n will be in the range 0....len(str)-1 inclusive).
def missing_char(str, n):
	  return str.replace(str[n], "") 
print(missing_char("kitchen", 3))

##Define a function to take a word and return negative meaning.
#Given a word, return a new word where "not " has been added to the front. 
#However, if the word already begins with "not", return the string unchanged.
def not_string(word):
    if "not" in word:
        return (word)
    else:
        return ("not" + " " + word)
print(not_string("everything bad"))