from nltk.corpus import wordnet


while True:
    
    request = input("Type a word: ")
    if(request != 'q'):
        syn = list()

        ant = list()
        for synset in wordnet.synsets(str(request)):
            for lemma in synset.lemmas():
                syn.append(lemma.name())    #add the synonyms
                if lemma.antonyms():    #When antonyms are available, add them into the list
                    ant.append(lemma.antonyms()[0].name())
        print('Synonyms: ' + str(syn)+'\n')
        print('Antonyms: ' + str(ant)+'\n')

    else:
        break;
