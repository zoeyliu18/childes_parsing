### Need to be run within the machamp folder

#usr/bin/env python3

import io, os, argparse, sys

mapping = {'twitter': 'cardiffnlp-twitter-roberta-base'}

#child = sys.argv[1]

for child in os.listdir('../processed_data/'):
	if child + '_indomain' not in os.listdir('../predict/machamp/'):
		os.system('mkdir ../predict/machamp/' + child + '_indomain/')
	for file in os.listdir('../processed_data/' + child + '/'):
		for seed in [1, 2, 3]:
			if file + '.machamp.twitter.' + str(seed) + '.indomain' not in os.listdir('../predict/machamp/' + child + '_indomain/') or os.stat('../predict/machamp/' + child + '_indomain/' + file + '.machamp.twitter.' + str(seed) + '.cardiffnlp-twitter-roberta-base.indomain').st_size == 0:
				print(file + '.machamp.twitter.' + str(seed) + '.cardiffnlp-twitter-roberta-base.indomain')
				#	try:
				os.system("python3 predict.py logs/" + child + ".machamp.twitter." + str(seed) + '.cardiffnlp-twitter-roberta-base/*/model.tar.gz ../processed_data/' + child + '/' + file + ' ../predict/machamp/' + child + '_indomain/' + file + '.machamp.twitter.' + str(seed) + '.cardiffnlp-twitter-roberta-base.indomain --device 0 --batch_size 16')
				#	except:
				#		print(file + '.machamp.' + treebank + '.' + str(seed) + '.' + emb)
