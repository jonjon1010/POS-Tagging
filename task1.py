# CompSci 723 - Intro to NLP 
# Assignment 1 
# Name: Jonathan Nguyen 
# Date: 10/16/2021
# Version: 1.0 

# Setup: 
# 1. Install Python, NLTK and Stanza
# Note: It seems stanza.download("en") gives an error on the latest version of Python (3.10.0). 
# If this happens with you then please install and use an older version of  Python (e.g. 3.9.6).
# 2. Get pretokenized sentences and gold-standard pos tags from Brown corpus for a genre using NLTK
# 3. Use Stanza to generate pos-tags for pretokenized sentences
# 4. Convert universal pos-tags from Stanza to pos-tags of Brown corpus
# 5. Evaluate the accuracy of pos tagging
# A helper program a1.py is also provided.

# Tasks: 
# 1. Choose any three genres from Brown corpus. For each genre, obtain pretokenized 
# sentences and obtain their universal pos-tags using Stanza. Evaluate the performance 
# in terms of accuracy using the correct (gold-standard) universal pos-tags as annotated in the Brown corpus.
# 2. Come up with at least five interesting sentences on your own in which one or more pos tags are not trivial 
# to tag. Obtain pos tags from Stanza and qualitatively evaluate whether it did the right thing.

# Submit: 
# 1. Report: Write a report in which you include:
# (5 points) The accuracies obtained for Task 1 in a table or a graph.
# (2 points) Write some comments about the results obtained in Task 1.
# (2 points) Show the sentences you tried for Task 2 mentioning why they were interesting.
# (1 points) Show the pos tags that were obtained using Stanza for Task 2.
# (2 points) Write comments about your qualitative evaluation of Task 2 (for example, point out the errors it made and possibly why).
# 2. Code:
# (3 points) Submit all the code you wrote for doing this assignment as an executable .py file. The grader should be able to replicate your results.
 
import a1 
import nltk 
import stanza 

pos_tagger = stanza.Pipeline(processors="tokenize,pos",tokenize_pretokenized=True)

# Task 1: 

# First Genre:
s1 = nltk.corpus.brown.tagged_sents(categories="fiction", tagset="universal")
s1_list = [] 
for s in s1: 
    w_list = []
    for w in s:
        w_list.append(w[0])
    s1_list.append(w_list)
g1 = a1.get_pos_from_nltk_tagged_sents(s1)
o1 = pos_tagger(s1_list)
o1 = a1.get_pos_from_stanza_output(o1)
print("Finding accuracy of the genre fiction:")
a1.accuracy(g1, o1)
print()

# Second Genre:
s2 = nltk.corpus.brown.tagged_sents(categories="romance", tagset="universal")
s2_list = []
for s in s2: 
    w_list = []
    for w in s:
        w_list.append(w[0])
    s2_list.append(w_list)
g2 = a1.get_pos_from_nltk_tagged_sents(s2)
o2 = pos_tagger(s2_list)
o2 = a1.get_pos_from_stanza_output(o2)
print("Finding accuracy of the genre romance:")
a1.accuracy(g2, o2)
print()

# Third Genre: 
s3 = nltk.corpus.brown.tagged_sents(categories="government", tagset="universal")
s3_list = []
for s in s3: 
    w_list = []
    for w in s:
        w_list.append(w[0])
    s3_list.append(w_list)
g3 = a1.get_pos_from_nltk_tagged_sents(s3)
o3 = pos_tagger(s3_list)
o3 = a1.get_pos_from_stanza_output(o3)
print("Finding accuracy of the genre government:")
a1.accuracy(g3, o3)
print()
