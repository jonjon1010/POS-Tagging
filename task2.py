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

# Task 2: 

# Sentence 1: 
sent1 = "Bob saw the saw on the table and decided to take it"
gold1 = ["NOUN","VERB","DET","NOUN","IN","DET","NOUN","CONJ","VERB","TO","VERB","PRP"]
gold1_list = []
gold1_list.append(gold1)
output1 = pos_tagger(sent1)
output1 = a1.get_pos_from_stanza_output(output1)
print(gold1_list)
print(output1)
print("Finding accuracy of sentence 1:")
a1.accuracy(gold1_list, output1)
print()

# Sentence 2:
sent2 = "Billy chickened out from eating the really spicy chicken wings"
gold2 = ["NOUN","VERB","PART","FROM","VERB","DET","ADV","ADJ","NOUN", "NOUN"]
gold2_list = []
gold2_list.append(gold2)
output2 = pos_tagger(sent2)
output2 = a1.get_pos_from_stanza_output(output2)
print(gold2_list)
print(output2)
print("Finding accuracy of sentence 2:")
a1.accuracy(gold2_list, output2)
print()

# Sentence 3:
sent3 = "John has a pet dog that he would alway pet before going to sleep"
gold3 = ["NOUN","VERB","DET","NOUN","NOUN","DET","PRON","VERB","ADV","VERB","ADV","VERB","DET","NOUN"]
gold3_list = []
gold3_list.append(gold3)
output3 = pos_tagger(sent3)
output3 = a1.get_pos_from_stanza_output(output3)
print(gold3_list)
print(output3)
print("Finding accuracy of sentence 3:")
a1.accuracy(gold3_list, output3)
print()

# Sentence 4: 
sent4 = "Sam's movie in the box office hit a big hit" 
gold4 = ["NOUN","NOUN","IN","DET","NOUN","NOUN","VERB","DET","ADJ","NOUN"]
gold4_list = []
gold4_list.append(gold4)
output4 = pos_tagger(sent4)
output4 = a1.get_pos_from_stanza_output(output4)
print(gold4_list)
print(output4)
print("Finding accuracy of sentence 4:")
a1.accuracy(gold4_list, output4)
print()

# Sentence 5: 
sent5 = "Nate ate chicken noodle soup with spoon"
gold5 = ["NOUN","VERB","NOUN","NOUN","NOUN","IN","NOUN"]
gold5_list = []
gold5_list.append(gold5)
output5 = pos_tagger(sent5)
output5 = a1.get_pos_from_stanza_output(output5)
print(gold5_list)
print(output5)
print("Finding accuracy of sentence 5:")
a1.accuracy(gold5_list, output5)
print()