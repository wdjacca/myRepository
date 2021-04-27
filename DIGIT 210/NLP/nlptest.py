from collections import Counter
import pygal
import spacy
# Need line 8 the first time: Then comment it out after the first time you run it:
# nlp = spacy.cli.download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')
lemmatizer = nlp.get_pipe("lemmatizer")
print(lemmatizer.mode)  # 'rule'

disneysongs = open('disneySongLyrics.txt', 'r')
words = disneysongs.read()
disneywords = nlp(words)


#
# def punctuation(words):
#     Punct = []
#     count = 0
#     for token in words:
#         if token.pos_ == "PUNCT":
#             count += 1
#             Punct.append(token.lemma_)
#             print(count, ": ", token, token.pos_, spacy.explain(token.pos_))
#     return Punct
#
# listPunct = punctuation(disneywords)
# punct_count = Counter(listPunct)
# topThree = punct_count.most_common(3)
# print(topThree)
#
#
# bar_chartTopThree = pygal.Bar()
#
# bar_chartTopThree.title = 'Top Three Punctuation used in Disney Songs'
#
# for t in topThree:
#     print(t[0], t[1])
#     bar_chartTopThree.add(t[0], t[1])
#
# # print(bar_chart)
# print(bar_chartTopThree.render_to_file('bar_chartTopThreePunct.svg'))
#
# def nounfinder(words):
#     noun = []
#     count = 0
#     for token in words:
#         if token.pos_ == "NOUN":
#             count += 1
#             noun.append(token.text)
#             print(count, ": ", token, token.pos_, spacy.explain(token.pos_))
#     return noun
#
# nounlist = nounfinder(disneywords)
# nouncount = Counter(nounlist)
# listofnouns = nouncount.most_common()
# topFive = nouncount.most_common(5)
# print(nouncount)
# print(listofnouns)
# print(topFive)
#
# bar_chartNounList = pygal.Bar()
#
# bar_chartNounList.title = 'List of Nouns used in Disney Songs'
#
# for n in listofnouns:
#     print(n[0], n[1])
#     bar_chartNounList.add(n[0], n[1])
#
# print(bar_chartNounList.render_to_file('bar_chartNounListNotLemma.svg'))

def entitypeople(words):
    ents = []
    count = 0
    for token in words.ents:
        if token.label_ == "PERSON" or token.label_ =="ORG":
            count += 1
            ents.append(token.text)
            print(count, ": ", token, token.label_, spacy.explain(token.label_))
    return ents

ppllist = entitypeople(disneywords)
pplcount = Counter(ppllist)
listofentities = pplcount.most_common()
print(listofentities)
# listofnouns = nouncount.most_common()
# topFive = nouncount.most_common(5)
# print(nouncount)
# print(listofnouns)
# print(topFive)

# bar_chartNounList = pygal.Bar()
#
# bar_chartNounList.title = 'List of Nouns used in Disney Songs'
#
# for n in listofnouns:
#     print(n[0], n[1])
#     bar_chartNounList.add(n[0], n[1])
#
# print(bar_chartNounList.render_to_file('bar_chartNounListNotLemma.svg'))







