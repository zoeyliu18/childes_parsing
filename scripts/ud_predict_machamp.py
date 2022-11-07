### Need to be run within the machamp folder

#usr/bin/env python3

import io, os, argparse

mapping = {'bert': 'bert-base-cased', 'roberta': 'roberta-base', 'twitter': 'cardiffnlp-twitter-roberta-base'}

if not os.path.exists('predict'):
	os.system('mkdir predict')

for directory in os.listdir('../UD_data/'):
	if os.path.isdir('../UD_data/' + directory) and directory.startswith('UD'):
		if not os.path.exists('predict/' + directory):
			os.system('mkdir predict/' + directory)

		test_file = ''
		for file in os.listdir('../UD_data/' + directory):
			if file.endswith('test.conllu') or file.endswith('test.fixed.conllu'):
				test_file = file

		file_name = test_file.split('.')[0]

		treebank = ''
		if 'ewt' in test_file:
			treebank = 'ewt'
		if 'twitter' in test_file:
			treebank = 'twitter'
		if 'esl' in test_file:
			treebank = 'esl'

		for seed in [1, 2, 3]:
			for emb in ['bert-base-cased', 'roberta-base', 'cardiffnlp-twitter-roberta-base']:
				if file_name + '.machamp.' + treebank + '.' + str(seed) + '.' + emb not in os.listdir('predict/' + directory) or os.stat('predict/' + directory + '/' + file_name + '.machamp.' + treebank + '.' + str(seed) + '.' + emb).st_size == 0:
					print(file_name + '.machamp.' + treebank + '.' + str(seed) + '.' + emb)
					try:
						os.system("python3 predict.py logs/machamp." + treebank + '.' + str(seed) + '.' + emb + '/*/model.tar.gz ../UD_data/' + directory + '/' + test_file + ' predict/' + directory + '/' + file_name + '.machamp.' + treebank + '.' + str(seed) + '.' + emb + ' --device 0 --batch_size 16')
					except:
						print(file_name + '.machamp.' + treebank + '.' + str(seed) + '.' + emb)

