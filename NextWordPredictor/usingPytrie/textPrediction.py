import pickle

def topWordsPrediction(fileName,text):
    lowerText = text.lower()
    with open(fileName,'rb') as trieObject:
        trie = pickle.load(trieObject)
        predictiveText = trie.values(lowerText)
        predictiveTextList = []
        for index, values in enumerate(predictiveText):
            predictiveTextList.append(values)
        return predictiveTextList

print(topWordsPrediction('trie.pkl','Data'))
