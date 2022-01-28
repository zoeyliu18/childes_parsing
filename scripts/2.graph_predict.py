#usr/bin/env python3

import io, os, argparse
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

def predict(file, directory, model, emb, run):

	mapping = {'bert': 'bert-cased', 'roberta': 'roberta-large', 'rembert': 'rembert'}

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
	
	file_name = file.split('/')[-1]

	with io.open('predict/graph' + str(run) + '/' + directory + '/' + mapping[emb] + '/' + file_name, 'w') as f:
		for sent in predictions:
			for tok in sent:
				f.write('\t'.join(str(w) for w in tok) + '\n')
			f.write('\n')

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type = str, help = 'path to ud_data/')

	args = parser.parse_args()

	if not os.path.exists('predict'):
		os.system('mkdir predict/')

	for run in [1, 2, 3]:
		if not os.path.exists('predict/graph' + str(run)):
			os.system('mkdir predict/graph' + str(run))

	for directory in os.listdir(args.input):
		if os.path.isdir(args.input + directory) and directory.startswith('UD'):
			for run in [1, 2, 3]:
				if not os.path.exists('predict/graph/' + directory):
					os.system('mkdir predict/graph/' + directory)

				if not os.path.exists('predict/graph/' + directory + '/bert-cased'):
					os.system('mkdir predict/graph/' + directory + '/bert-cased')
				if not os.path.exists('predict/graph/' + directory + '/roberta-large'):
					os.system('mkdir predict/graph/' + directory + '/roberta-large')
				if not os.path.exists('predict/graph/' + directory + '/rembert'):
					os.system('mkdir predict/graph/' + directory + '/rembert')

			test_file = ''
			for file in os.listdir(args.input + directory):
				if file.endswith('test.conllu') or file.endswith('test.fixed.conllu'):
					test_file = file

			for run in [1, 2, 3]:
				bert_model = parser = Parser.load('models/graph/' + str(run) + '/' + directory + '/bert-cased/model')
				roberta_model = parser = Parser.load('models/graph/' + str(run) + '/' + directory + '/roberta-large/model')
		#		rembert_model = parser = Parser.load('models/graph/' + str(run) + '/' + directory + '/rembert/model')

				predict(args.input + directory + '/' + test_file, directory, bert_model, 'bert', run)
				predict(args.input + directory + '/' + test_file, directory, roberta_model, 'roberta', run)
		#		predict(args.input + directory + '/' + test_file, directory, rembert_model, 'rembert'):
