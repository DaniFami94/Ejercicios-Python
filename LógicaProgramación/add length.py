"""
What if we need the length of the words separated by a space to be added at the end of that same word and have it returned as an array?

Example(Input --> Output)

"apple ban" --> ["apple 5", "ban 3"]
"you will win" -->["you 3", "will 4", "win 3"]
Your task is to write a function that takes a String and returns an Array/list with the length of each word added to each element .

Note: String will have at least one element; words will always be separated by a space.
"""


def add_length(str_): 
    #your code here
   return [f"{word} {len(word)}" for word in str_.split()] #return a list comprehension that iterates over the words in the string and returns the word and its length
    
  
def add_length2(str_):
    arrayOfWords = [] #initialize an empty list to store the words and their lengths
    for word in str_.split(): #loop through the words in the string
        arrayOfWords.append(word + ' ' + str(len(word))) #append the word and its length to the arrayOfWords list
    return arrayOfWords


print(add_length("apple ban"))
print(add_length2("hello my name is Peter I am 26 years old"))