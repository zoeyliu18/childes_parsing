### Need to be run within the machamp folder

#usr/bin/env python3

import io, os, argparse, sys

if not os.path.exists('../predict'):
	os.system('mkdir ../predict')

if not os.path.exists('../predict/machamp'):
	os.system('mkdir ../predict/machamp')

mapping = {'bert': 'bert-base-cased', 'roberta': 'roberta-base', 'twitter': 'cardiffnlp-twitter-roberta-base'}

child = sys.argv[1]

if not os.path.exists('../predict/machamp/' + child):
	os.system('mkdir ../predict/machamp/' + child)

for file in os.listdir('../processed_data/' + child + '/'):
	for treebank in ['ewt', 'twitter', 'esl']:
		for seed in [1, 2, 3]:
			for emb in ['bert-base-cased', 'roberta-base', 'cardiffnlp-twitter-roberta-base']:
				if file + '.machamp.' + treebank + '.' + str(seed) + '.' + emb not in os.listdir('../predict/machamp/' + child + '/') or os.stat('../predict/machamp/' + child + '/' + file + '.machamp.' + treebank + '.' + str(seed) + '.' + emb).st_size == 0:
					print(file + '.machamp.' + treebank + '.' + str(seed) + '.' + emb)
				#	try:
					os.system("python3 predict.py logs/machamp." + treebank + '.' + str(seed) + '.' + emb + '/*/model.tar.gz ../processed_data/' + child + '/' + file + ' ../predict/machamp/' + child + '/' + file + '.machamp.' + treebank + '.' + str(seed) + '.' + emb + ' --device 0 --batch_size 16')
				#	except:
				#		print(file + '.machamp.' + treebank + '.' + str(seed) + '.' + emb)
