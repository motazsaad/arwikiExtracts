import glob
import json
import logging
import os
from collections import defaultdict
from tabulate import tabulate
import operator


def corpus_info(corpus_file, topn=100):
	corpus = open(corpus_file, encoding='utf-8').read()
	word_freq = {} 
	for word in corpus.split():
		word_freq[word] = word_freq.get(word, 0) + 1 

	print('vocabulary size:', len(word_freq))
	word_count = 0 
	for v in word_freq.values():
		word_count += v 
	print('word count:', word_count)
	
	sorted_freq = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)
	most_freq = [list(i) for i in sorted_freq[:topn]]  # list of lists
	print('### Most frequent words')
	print(tabulate(most_freq, headers=["Word", "Frequency"], tablefmt="github", showindex=True))
	least_freq = [list(i) for i in sorted_freq[-1*topn:]]  # list of lists
	print('### Hapax words')
	print(tabulate(least_freq, headers=["Word", "Frequency"], tablefmt="github", showindex=True))
	
	
	
corpus_info('arwiki_20190920.txt')


