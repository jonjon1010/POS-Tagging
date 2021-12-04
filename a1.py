""" Following are some helper functions for Assignment 1. """

def convert_pos(pos) :
    """ Converts universal a pos tag to a compatible
         universal pos inn Brown corpus. """
    if pos=="CCONJ" :
        return "CONJ"
    elif pos=="AUX" :
        return "VERB"
    elif pos=="INTJ" :
        return "X"
    elif pos=="PART" :
        return "PRT"
    elif pos=="PROPN" :
        return "NOUN"
    elif pos=="PUNCT" :
        return "."
    elif pos=="SCONJ" :
        return "ADP"
    elif pos=="SYM" :
        return "X"
    else :
        return pos

def get_pos_from_stanza_output(output) :
    """ Converts Stanza output into a list of list of universal pos tags
        compatible with Brown corpus. """
    r = []
    for s in output.sentences : # loop through every sentence
        pos = []
        for w in s.words : # loop through every token
            pos.append(convert_pos(w.upos)) # converted universal pos tag
        r.append(pos)
    return r

def get_pos_from_nltk_tagged_sents(o) :
    """ Converts NLTK's tagged sentences into list of list of
        universal pos tags."""
    r = []
    for s in o : # loop through every sentence
        pos = []
        for w in s : # loop through every token
            pos.append(w[1]) # get the pos tag
        r.append(pos)
    return r
            
def accuracy(gold,output) :
    """ Computes accuracy by counting matches between gold-standard
        list of list and the output. The list dimensions must match. """
    correct = 0
    total = 0
    assert(len(gold)==len(output))
    for i in range(len(gold)) : # loop through every sentence
        assert(len(gold[i])==len(output[i]))
        total += len(gold[i])
        for j in range(len(gold[i])) :# loop through every token
            if gold[i][j]==output[i][j] : # match
                correct += 1
    print("Accuracy:",(correct*100)/total,"%")
