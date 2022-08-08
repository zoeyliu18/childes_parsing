### Need to be run within the diaparser folder

#usr/bin/env python3

import io, os, sys
from diaparser.parsers import Parser

### Read *.conllu file ###

def conll_read_sentence(file_handle):

	sent = []

	for line in file_handle:
		line = line.strip('\n')
	
		if line.startswith('#') is False :
			toks = line.split("\t")			
		
			if len(toks) == 1:
				return sent 
			else:
				if toks[0].isdigit() == True:
					sent.append(toks)

	return None


### Get all sentences from a file ###

def get_data(file):

	data = []

	with io.open(file, encoding = 'utf-8') as f:
		sent = conll_read_sentence(f)

		while sent is not None:
			words = []
			for tok in sent:
				words.append(tok[1])

			data.append(words)

			sent = conll_read_sentence(f)

	return data


### Predict parses of sentences from a file with a trained model ###

def predict(file, directory, model, emb, seed):

	mapping = {'bert': 'bert-base-cased', 'roberta': 'roberta-base', 'twitter': 'cardiffnlp-twitter-roberta-base'}

	predictions = []

	data = get_data(file)

	for sent in data:
		pred = model.predict([sent], prob = True)
		pred_values = pred.sentences[0].values

	# values format	
	# [('1', '2', '3', '4', '5'), ('She', 'enjoys', 'playing', 'tennis', '.'), ('_', '_', '_', '_', '_'), ('_', '_', '_', '_', '_'), ('_', '_', '_', '_', '_'), ('_', '_', '_', '_', '_'), [2, 3, 0, 3, 3], ['nsubj', 'aux', 'root', 'obj', 'obj'], ('_', '_', '_', '_', '_'), ('_', '_', '_', '_', '_')]

		info = []
		for i in range(len(pred_values[0])):
			word_info = []
			for z in range(len(pred_values)):
				word_info.append(pred_values[z][i])
			info.append(word_info)

		predictions.append(info)
	
	file_name = file.split('/')[-1].split('.')[0]
	treebank = ''
	if 'ewt' in file_name:
		treebank = 'ewt'
	if 'reddit' in file_name:
		treebank = 'reddit'

	if file_name + '.diaparser.' + treebank + '.' + str(seed) + '.' + mapping[emb] not in os.listdir(directory + '/') or os.stat(directory + '/' + file_name + '.diaparser.' + treebank + '.' + str(seed) + '.' + mapping[emb]).st_size == 0:
		with io.open(directory + '/' + file_name + '.diaparser.' + treebank + '.' + str(seed) + '.' + mapping[emb], 'w') as f:
			for sent in predictions:
				for tok in sent:
					f.write('\t'.join(str(w) for w in tok) + '\n')
				f.write('\n')


if not os.path.exists('../predict'):
	os.system('mkdir ../predict')

if not os.path.exists('../predict/diaparser'):
	os.system('mkdir ../predict/diaparser')

child = sys.argv[1]

if not os.path.exists('../predict/diaparser/' + child):
	os.system('mkdir ../predict/diaparser/' + child)

for file in os.listdir('../data/' + child + '/'):
	file_name = file.split('.')[0]

	for treebank in ['ewt', 'twitter', 'esl']:
		for seed in [1, 2, 3]:
			bert_model = Parser.load('logs/diaparser.' + treebank + '.' + str(seed) + '.bert-base-cased')
			roberta_model = Parser.load('logs/diaparser.' + treebank + '.' + str(seed) + '.roberta-base')
			twitter_model = Parser.load('logs/diaparser.' + treebank + '.' + str(seed) + '.cardiffnlp-twitter-roberta-base')

			predict('../data/' + directory + '/' + file, '../predict/diaparser/' + directory, bert_model, 'bert', seed)
			predict('../data/' + directory + '/' + file, '../predict/diaparser/' + directory, roberta_model, 'roberta', seed)
			predict('../data/' + directory + '/' + file, '../predict/diaparser/' + directory, twitter_model, 'twitter', seed)

