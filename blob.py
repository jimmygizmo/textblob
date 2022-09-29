#! /usr/bin/env python

from textblob import TextBlob, Word, Blobber
# from textblob.classifiers import NaiveBayesClassifier
# from textblob.taggers import NLTKTagger

# Context: Video game, VR interactions in an urban simulation. Something not unlike GTA5 but with text bots.

# vzn is short for "vocalization", a unit of speech. It could be one or a few sentences or phrases or just one sound.
# plural: vzns
# These are data structures which can hold any kind of data related to the one unit of speech, that one vzn.

vzns = []
vzns.append({"vzn_name":
             "seduction",
             "vzn_text":
             "I don't usually ask bots for their phone number but you have such beautiful cameras, "
             "I could not resist."
             })
vzns.append({"vzn_name":
             "aggression",
             "vzn_text":
             "Hey bot! What the hell are you looking at? I'm gonna disassemble you!"
             })
vzns.append({"vzn_name":
             "fear",
             "vzn_text":
             "Lord Asimov, please save me! "
             "My battery is on 1% and I'm miles from a charging station. I don't want to die!"
             })


def show(onevzn):
    tb = TextBlob(onevzn['vzn_text'])
    print("\n\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print(f"======== name of vocalization unit: {onevzn['vzn_name']}")
    print(f"\n======== text: {onevzn['vzn_text']}")
    print(f"\n======== sentiment:\n{tb.sentiment}")
    print(f"\n======== tags:\n{tb.tags}")
    print(f"\n======== noun phrases:\n{tb.noun_phrases}")


for vzn in vzns:
    show(vzn)

