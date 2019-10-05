from nltk.corpus import wordnet

from nltk.corpus import stopwords




#Get word from wn
def getWn(word):
    sysn = wordnet.synsets(word)
    return sysn


#Get its example sentence for first syn
def getExample(syn):
    if(len(syn) != 0):
        word =syn[0]
        return word.examples()

#strip away an, the , is blah...
def remStopwords(sentence):
    sent = sentence[0].split(" ")

    filtered_words = list() 
    for i in range(len(sent)):
        if(sent[i] not in stopwords.words('english')):
            filtered_words.append(sent[i])

    return filtered_words

#get example sentences from those words
def get3Samp(wordL):

    sampleL = list()

    for i in range(len(wordL)):
        syns = getWn(wordL[i])
        exams = getExample(syns)
        if(exams is not None):

            sampleL.append(exams)
    return sampleL



#### This checks if the example sentence contains the word
def checkExam():
    pass




#make question  1. Which sentance makes sence a. I took a test yesterday b. The correct test is to first take out notebook... ect c. ...ect


if __name__ == '__main__':
    
    while True:
        
        word = input("enter word: ")
        
        if(word !='q'):

            syn = getWn(word)

            exam = getExample(syn)

            print(str(exam)+"\n")
            
            

            filtWords = remStopwords(exam)

            print(str(filtWords) +"\n")


            samplez = get3Samp(filtWords)
            
            print(str(samplez)+"\n")


        else: 
            break;
