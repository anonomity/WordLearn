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
    filtered_words = list()
    if(len(sentence) != 0):
        for i in range(len(sentence)):
            sent = sentence[i].split(" ")

            for i in range(len(sent)):
                if(sent[i] not in stopwords.words('english')):
                    filtered_words.append(sent[i])
    else: 
        return False
    return filtered_words


def listToString(list):
    newString = ""
    for i in range(len(list)):
        newString = str(newString) + " "+ str(list[i])
    return newString

def modExamples(example,wordToRemove, wordToInput):
    lista = []
    #TODO: If the example is empty it needs to try to get another example
    if((example is not None) & (len(example) != 0)):
        lista =example[0].split(" ")
        for i in range(len(lista)):
            if(wordToRemove in lista[i]):
                lista[i] = str(wordToInput)
                break;
    modEx = listToString(lista)
    return modEx



#get example sentences from those words
def get3Samp(wordL, word):

    sampleL = list()

    for i in range(len(wordL)):
        syns = getWn(wordL[i])
                
        exams = getExample(syns)
        #print(str(i)," ",str(wordL[i])," ",str(exams))
        
        if((exams is not None)):
            if(len(exams) != 0):
                goodExamples = checkExam(wordL[i],exams)
####TODO: good examples sometimes are empty
                if(len(goodExamples) != 0): 
                    modExam = modExamples(goodExamples, wordL[i], word)
                    sampleL.append(modExam)
    return sampleL
    


#### This checks if the example sentence contains the word
def checkExam(word,example):
    goodExamps = list()
    for i in range(len(example)):

        if(str(word) in example[i]):
            goodExamps.append(example[i])
    return goodExamps
    
#Removes the getting the example from the study word
def removeAnswerWord(filt, defWord):
    newArr = list()
    for p in range(len(filt)):
        if(filt[p] != defWord):
            newArr.append(filt[p])
    return newArr


def genMC(examList, studyWord):
    question = "Which example is the best for the word " + str(studyWord)
    choices = list()
    if(len(examList) >= 3):
        for i in range(3):
            choices.append(examList[i])
    return question, choices
    
def listToOptions(exampleList):
    if(len(exampleList) == 3):
        choices = "A." + str(exampleList[0]) + "\n" + "B. " + str(exampleList[1]) + "\n" + "C. " + str(exampleList[2])
        return choices
    elif(len(exampleList) == 2):
        choices = "A." + str(exampleList[0]) + "\n" + "B. " + str(exampleList[1])

#make question  1. Which sentance makes sence a. I took a test yesterday b. The correct test is to first take out notebook... ect c. ...ect


if __name__ == '__main__':
    
    while True:
        
        word = input("enter word: ")
        
        if(word !='q'):

            syn = getWn(word)

            exam = getExample(syn)

            #print(str(exam)+"\n")
            
            

            filtWords = remStopwords(exam)
            if(filtWords == False):
                break;
            #print(str(filtWords) +"\n")

            
            doubleFilt = removeAnswerWord(filtWords, word)

            samplez = get3Samp(doubleFilt, word)
            
            #print(str(samplez)+"\n")
            
            MC = genMC(samplez, word)

            print("Question 1. "+ str(MC[0]))

            ch = listToOptions(MC[1])

            print(ch)
            sysn = wordnet.synsets(word)
            print("D. " + str(sysn[0].examples()[0]))


        else: 
            break;
