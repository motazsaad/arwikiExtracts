import glob
import json
import logging
import os
from collections import defaultdict
from tabulate import tabulate
import operator



def load_json_wiki_corpus(corpus_dir):
    json_corpus = list()
    for subdir, dirs, files in os.walk(corpus_dir):
        for f in files:
            wiki_file = os.path.join(subdir, f)
            # print('reading', wiki_file)
            with open(wiki_file, encoding='utf-8') as wiki_reader:
                lines = wiki_reader.readlines()
                for line in lines:
                    json_doc = json.loads(line)
                    doc_id = json_doc.get('id', '')
                    title = json_doc.get('title', '')
                    text = json_doc.get('text', '')
                    if text:
	                    json_corpus.append(text)
    return json_corpus


def corpus_info(corpus, outfile, topn=100):
	wiki_writer = open(outfile, encoding='utf-8', mode='w')
	print('# of documents:', len(corpus))
	word_freq = {} 
	for doc in corpus:
		# print(doc)
		for word in doc.split():
			word_freq[word] = word_freq.get(word, 0) + 1 
		wiki_writer.write('{}\n'.format(doc))
	print('vocabulary size:', len(word_freq))
	word_count = 0 
	for v in word_freq.values():
		word_count += v 
	print('word count:', word_count)
	
	sorted_freq = sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)
	most_freq = [list(i) for i in sorted_freq[:topn]]  # list of lists
	print('most frequent word')
	print(tabulate(most_freq, headers=["Word", "Frequency"], tablefmt="pipe"))
	least_freq = [list(i) for i in sorted_freq[-1*topn:]]  # list of lists
	print('hapax words')
	print(tabulate(least_freq, headers=["Word", "Frequency"], tablefmt="pipe"))
	
	
	
arwiki_corpus = load_json_wiki_corpus('/home/motaz/gitrepos/arwikiExtracts/20190920/')
corpus_info(arwiki_corpus, 'arwiki_20190920.txt')


