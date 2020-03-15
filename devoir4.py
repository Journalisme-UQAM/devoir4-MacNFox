# coding : utf-8
#Importation du CSV et de SpaCy, en plus d'aller chercher mon Counter pour plus tard
#être en mesure de bien extraire l'information nécessaire
import csv, spacy
from collections import Counter

martino = "martino.csv"
#Ouverture de mon fichier CSV
f = open(martino)
interventions = csv.reader(f)
next = (interventions)

#Importation de la version fr de spacy, afin de charger les accents des textes correctement
tal = spacy.load("fr_core_news_md")
tal.Defaults.stop_words.add("musulm")

tousMots = []
bigrams = []
#Début de ma boucle pour aller chercher les éléments de mon texte
for inter in interventions:
    doc = tal(inter[3])
    tokens = [token.text for token in doc]
    print(tokens)
    print(len(tokens))
#Lemmatisation
    lemmes = [token.lemma_ for token in doc]
    print(lemmes)
    print(len(lemmes))

#Retrancher les lignes de mon texte pour éviter d'avoir des "y", "de", "le", etc. dans mes paragraphes
    tokens = [token.text for token in doc if token.is_stop == False]
    print(tokens)
    print(len(tokens))

    mots = [token.text for token in doc if token.is_stop == False and token.is_punct == False]
    mots = [token.lemma_ for token in doc if token.is_stop == False and token.is_punct == False]
    print(mots)
    print(len(mots))
    musulm = [token.lemma_ for token in doc if token.is_stop == False and token.is_punct == False]
    print(mots)
    print("#"*50)

for mot in mots:
    tousMots.append(mot)

freq = Counter(tousMots)
print(freq.most_common(25))
print(len(tousMots))
#Extraction de mes mots pour musulm-
for x, y in enumerate(mots[:-1]):
    bigrams.append("{} {}".format(mots[x],mots[x+1]))
print(bigrams)

freq = Counter(bigrams)
print(freq.most_common(50))
print(len(bigrams))

#Fidèle à mes scripts, je ne trouve pas comment réellement sortir l'expression et la quantifier.
#Merci JH de la correction ^-^