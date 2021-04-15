import spacy
# nlp = spacy.cli.download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')

disneySongs = open('disneySongLyrics.txt', 'r')
text = disneySongs.read()
textstrings = str(text)
# print(textstrings)


# count=0
# for t in text:
#     count +=1
#     print (count, ": ", t)

disneyWords = nlp(textstrings)
for token in disneyWords:
     print(token.text, "---->", token.pos_, ":::::", token.lemma_)
