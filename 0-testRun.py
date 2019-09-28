from nltk.corpus import wordnet


word = input("Type word: " )

sysns = wordnet.synsets(word)

length = len(sysns)

for i in range(length): 
    print(i+1," " ,sysns[i].name(), ": ", sysns[i].definition(),"\n")

choice = input("which definition suits you? [1 - "+ str(length)+ "] \n") 

#user choice about which definition is most relative/ must reduce by one 

choice = sysns[int(choice)-1]


length = len(choice.lemmas())

print("Some Examples")
print("-----------------------------------------------------------\n")
print(choice.examples())


print( "LEMMAS AND DEFINITIONS")
print("-----------------------------------------------------------\n")

for i in range(length):
    word =str(choice.lemmas()[i].name())
    



