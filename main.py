#!/usr/bin/python
# Madlibs.py
__author__ = "David White"
__version__ = "1.0"
import nltk
from nltk.tokenize import PunktSentenceTokenizer
import random
import textwrap
# gets the correct downloads onto the computer of the user for the code to run
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def main():
    player = input("What is your name? ")
    age = int(input("What is your age "))
    print(len(player) + age, "is what the length of your name and your age added together is" )
    print(player, "We will now start our madlibs")
    adventures = open("adventures.txt", encoding="utf-8")  # decodes text of utf-8
    book_text = adventures.read()
    scarlet = open("Sherlock.txt", encoding="utf-8") #
    training_text = scarlet.read()
    PunktSentenceTokenizer(book_text)
    x = 0
    final = []

    # dictionary to translate from pos-tag to english
    Pos_dict = {"CC": "a coordinating conjunction", "CD": "a cardinal digit", "DT": "a determiner", "EX": "an existential there",
                "FW": "a piece of random gibberish", "IN": "a preposition or an subordinating conjunction",
                "JJ": "an adjective", "JJR": "a comparative adjective", "JJS": "a superlative adjective", "LS": "a list marker",
                "MD": "a modal", "NN": "a singular noun", "NNS": "a plural noun", "NNP": "a proper noun",
                "NNPS": "a plural proper noun", "PDT": "a predeterminer", "POS": "a possessive ending",
                "PRP": "personal pronoun", "PRP": "a possessive pronoun", "RB": "an adverb",
                "RBR": "a comparative adverb", "RBS": "a superlative adverb", "RP": "a participle", "TO": "a means of transport",
                "UH": "interjection", "VB": "a verb in base form", "VBD": "a verb in past tense",
                "VBG": "a verb in the present participle", "VBN": "a verb in the past participle", "VBP": "a verb in the singular present that is not 3d",
                "VBZ": "a verb in the third person singular present", "WDT": "a determiner beginning in wh", "WP": "a pronoun starting in W H",
                "WP$": "a possessive pronoun starting with wh", "WRB": "an adverb starting with wh"}

    def process_content(x):
        tokenizer = PunktSentenceTokenizer(training_text)  # the formation of a tokenizer which will understand texts
        tokenized = tokenizer.tokenize(book_text)  # preparing the text to be tagged
        # try to tag all of the words, in the exception of an error.
        try:
            # gives the number of lines to be tagged
            for tokens in tokenized[x:x + 10]:
                words = nltk.word_tokenize(tokens)  # gives the words postags
                tagged = nltk.pos_tag(words)
                for tag in tagged:  # creates a tagged section and a word section
                    word = tag[0]
                    pos_tag = tag[1]
                    if random.randint(1, 100) > 90 and len(word) > 2:  # makes 10% of words replaced
                        print("For your next word please give me", Pos_dict[pos_tag], "thanks ")
                        word = input()
                    final.append(word)  # adds the word to the list
        except Exception as e:
            print(e)
    while True:
        process_content(x)
        # turns the string
        final_word = " ".join(final)
        # removes everything nonessential
        final_word = final_word.replace(" ,", ",")
        final_word = final_word.replace(" .", ".")
        final_word = final_word.replace(" !", "!")
        final_word = final_word.replace(" ;", ";")
        final_word = final_word.replace(" ’ s", "'s")
        final_word = final_word.replace(" ?", "?")
        final_word = final_word.replace('" ', '"')
        print('\n'.join(textwrap.wrap(final_word, 70)))
        run_more = input("You would like to continue playing yes or no?")
        if run_more != "yes":
            break
        print("When you want to end close the code")
        x += 10
main()

