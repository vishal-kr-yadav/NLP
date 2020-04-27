# Function which returns all strings
# that contains given prefix
import pickle

from pytrie import StringTrie

def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def prefixSearch(arr, modelName):
    # create empty trie
    trie = StringTrie()

    # traverse through list of strings
    # to insert it in trie. Here value of
    # key is itself key because at last
    # we need to return
    for key in arr:
        trie[key] = key
    save_object(trie, modelName)

# Driver program
arr = ['Data Engineering', 'Data Science', 'Data Analytics', 'Data profiling']
lowerArr = [eachElement.lower() for eachElement in arr]
modelName =  'trie.pkl'
output = prefixSearch(lowerArr,modelName)


