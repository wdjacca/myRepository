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



def punctuation(words):
    Punct = []
    count = 0
    for token in words:
        if token.pos_ == "PUNCT":
            count += 1
            Punct.append(token.lemma_)
            print(count, ": ", token, token.pos_, spacy.explain(token.pos_))
    return Punct

listPunct = punctuation(disneywords)
punct_count = Counter(listPunct)
topThree = punct_count.most_common(3)
print(topThree)


bar_chartTopThree = pygal.Bar()

bar_chartTopThree.title = 'Top Three Punctuation used in Disney Songs'

for t in topThree:
    print(t[0], t[1])
    bar_chartTopThree.add(t[0], t[1])

# print(bar_chart)
print(bar_chartTopThree.render_to_file('bar_chartTopThree.svg'))

def nounfinder(words):
    noun = []
    count = 0
    for token in words:
        if token.pos_ == "NOUN":
            count += 1
            noun.append(token.lemma_)
            print(count, ": ", token, token.pos_, spacy.explain(token.pos_))
    return noun

nounlist = nounfinder(disneywords)
nouncount = Counter(nounlist)
topFive = nouncount.most_common(5)
print(topFive)


bar_chartTopFive = pygal.Bar()
bar_chartOver10 = pygal.Bar()

bar_chartTopFive.title = 'Top Five Nouns used in Disney Songs'
bar_chartOver10.title = "Nouns that appeared over 10 times in Disney Songs"

for t in topFive:
    print(t[0], t[1])
    bar_chartTopFive.add(t[0], t[1])

for n in nouncount:
    print(n, nouncount[n])
    if nouncount[n] > 10:
        bar_chartOver10.add(n, nouncount[n])

# print(bar_chart)
print(bar_chartOver10.render(is_unicode=True), bar_chartTopFive.render_to_file('bar_chartTopFive.svg'),
bar_chartOver10.render_to_file('bar_chartOver10.svg'))
