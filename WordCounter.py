import string #import string from the python library. 
def wordcount(filename): #takes a file.txt
    infile=open(filename) #open the file
    content=infile.read() #read the contents in the file
    #erasePunctuation will clean all the punctions like commas, periods, etc. and replace them with spaces
    erasePunctuation=str.maketrans(string.punctuation+string.digits,' '*len(string.punctuation+string.digits)) 
    cleanTxt=content.translate(erasePunctuation)
    wordDict={} #emtpy dictionary
    for word in cleanTxt.split(): #for words in cleantxt that are split
        if word not in wordDict.keys():
            wordCount=content.count(word)#counts teh number of words
            wordDict[word]=wordCount #adds the word and there occurences to the dictionary
            print('{:20}{}'.format(word,wordCount))#prints the dictionary 

