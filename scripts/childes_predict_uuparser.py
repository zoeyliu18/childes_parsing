import io, os, sys

if not os.path.exists('../predict'):
	os.system('mkdir ../predict')

if not os.path.exists('../predict/uuparser'):
	os.system('mkdir ../predict/uuparser')

child = sys.argv[1]

if not os.path.exists('../predict/uuparser/' + child):
	os.system('mkdir ../predict/uuparser/' + child)

if not os.path.exists('../temp'):
	os.system('mkdir ../temp')

for file in os.listdir('../data/' + child + '/'):
	file_name = file.split('.')[0]
	short_handle = '_'.join(w for w in file_name.split('_')[ : 2])
	if not os.path.exists('../temp/' + short_handle):
		os.system('mkdir ../temp/' + short_handle)

	os.system('cp ../data/' + child + '/' + file + ' ../temp/' + short_handle + '/' + short_handle + '-ud-test.conllu')

	for treebank in ['en_ewt', 'en_twitter', 'en_esl']
		for seed in [1, 2, 3]:
			os.system('uuparser --predict --modeldir uuparser/logs/' + str(seed) + '/ --outdir' + '../predict/uuparser/' + child + '/ --datadir ../temp --include ' + '"' + short_handle + '"')
			new_file_name = file_name + '.uuparser.' + str(seed)
			os.system('mv ../predict/uuparser/' + child + '/' + short_handle + '.conllu ../predict/uuparser/' + child + '/' + new_file_name)

### UD_English-EWT

!uuparser --outdir uuparser/logs/1/ --datadir UD_data --include "en_ewt" --dynet-seed 1 --dynet-mem 10000

!uuparser --predict --modeldir uuparser/logs/1/ --outdir uuparser/predict/1/ --datadir UD_data --include "en_ewt" 