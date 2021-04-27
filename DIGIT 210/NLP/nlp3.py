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



def adverb(words):
    adv = []
    count = 0
    for token in words:
        if token.pos_ == "ADV":
            count += 1
            adv.append(token.lemma_)
        print(count, ": ", token, token.pos_, spacy.explain(token.pos_))
    return adv

listadv = adverb(disneywords)
adv_count = Counter(listadv)
top10 = adv_count.most_common(10)
print(top10)


bar_chartTop10= pygal.Bar()

bar_chartTop10.title = 'Top 10 Adverbs used in Disney Songs'

for t in top10:
    print(t[0], t[1])
    bar_chartTop10.add(t[0], t[1])

# print(bar_chart)
print(bar_chartTop10.render_to_file('bar_chartTop10Adv.svg'))

def pronfinder(words):
    pron = []
    count = 0
    for token in words:
        if token.pos_ == "PRON":
            count += 1
            pron.append(token.lemma_)
            print(count, ": ", token, token.pos_, spacy.explain(token.pos_))
    return pron

pronlist = pronfinder(disneywords)
proncount = Counter(pronlist)
top4 = proncount.most_common(4)
print(top4)


bar_chartPronouns = pygal.Bar()

bar_chartPronouns.title = 'Top 4 Pronouns used in Disney Songs'

for p in top4:
    print(p[0], p[1])
    bar_chartPronouns.add(p[0], p[1])

# print(bar_chart)
print(bar_chartPronouns.render_to_file('bar_chartPronouns.svg'))
