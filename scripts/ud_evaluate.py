#usr/bin/env python3

import io, os, argparse, statistics

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


### Get heads and dependency relations from a file ###

def get_parse(file):

	parses = []

	with io.open(file, encoding = 'utf-8') as f:
		sent = conll_read_sentence(f)

		while sent is not None:
			info = []
			for tok in sent:
				info.append([tok[6], tok[7]])
			parses.append(info)

			sent = conll_read_sentence(f)

	return parses


### Evaluation ###

def evaluate(gold, pred):

	gold_parses = get_parse(gold)
	pred_parses = get_parse(pred)

	assert len(gold_parses) == len(pred_parses)

	### Macro: calculate for each sentence, then divide by number of sentences ###

	macro_uas = 0
	macro_las = 0

	for i in range(len(gold_parses)):
		gold_sent = gold_parses[i]
		pred_sent = pred_parses[i]
		sent_macro_uas = 0
		sent_macro_las = 0

		for z in range(len(gold_sent)):
			gold_head = gold_sent[z][0]
			gold_deprel = gold_sent[z][1]
			pred_head = pred_sent[z][0]
			pred_deprel = pred_sent[z][1]

			if gold_head == pred_head:
				sent_macro_uas += 1
			if gold_head == pred_head and gold_deprel == pred_deprel:
				sent_macro_las += 1

		sent_macro_uas = sent_macro_uas / len(gold_sent)
		sent_macro_las = sent_macro_las / len(gold_sent)

		macro_uas += sent_macro_uas
		macro_las += sent_macro_las

	macro_uas = round(100 * macro_uas / len(gold_parses), 2)
	macro_las = round(100 * macro_las / len(gold_parses), 2)

	### Micro: combining all sentences together ###

	micro_uas = 0
	micro_las = 0
	total = 0

	for i in range(len(gold_parses)):
		gold_sent = gold_parses[i]
		pred_sent = pred_parses[i]
		sent_macro_uas = 0
		sent_macro_las = 0

		total += len(gold_sent)

		for z in range(len(gold_sent)):
			
			gold_head = gold_sent[z][0]
			gold_deprel = gold_sent[z][1]
			pred_head = pred_sent[z][0]
			pred_deprel = pred_sent[z][1]

			if gold_head == pred_head:
				micro_uas += 1
			if gold_head == pred_head and gold_deprel == pred_deprel:
				micro_las += 1

	micro_uas = round(100 * micro_uas / total, 2)
	micro_las = round(100 * micro_las / total, 2)

	return [macro_uas, macro_las, micro_uas, micro_las]


treebank_map = {'UD_English-EWT': 'en_ewt', 'UD_English-ESL': 'en_esl', 'UD_English-Twitter': 'en_twitter'}


if not os.path.exists('results'):
	os.system('mkdir results/')

header = ['Treebank', 'Parser', 'Embedding', 'Macro_UAS', 'Macro_LAS', 'Micro_UAS', 'Micro_LAS']
		
f = open('results/' + 'ud_eval.txt', 'w')
f.write('\t'.join(w for w in header) + '\n')

for directory in os.listdir('UD_data/'):
	print(directory)
	if os.path.isdir('UD_data/' + directory) and directory.startswith('UD'):
		gold_file = ''
		file_name = ''

		for file in os.listdir('UD_data/' + directory):
			if file.endswith('test.conllu') or file.endswith('test.fixed.conllu'):
				gold_file = 'UD_data/' + directory + '/' + file
				file_name = file.split('.')[0]

		treebank = ''
		if 'EWT' in directory:
			treebank = 'ewt'
		if 'Twitter' in directory:
			treebank = 'twitter'
		if 'ESL' in directory:
			treebank = 'esl'

		for parser in ['diaparser', 'machamp']:
			for emb in ['bert-base-cased', 'roberta-base', 'cardiffnlp-twitter-roberta-base']:
				macro_uas = []
				macro_las = []
				micro_uas = []
				micro_las = []

				for seed in [1, 2, 3]:
					try:
						pred_file = parser + '/predict/' + directory + '/' + file_name + '.' + parser + '.' + treebank + '.' + str(seed) + '.' + emb
						evaluate_results = evaluate(gold_file, pred_file)
						macro_uas.append(evaluate_results[0])
						macro_las.append(evaluate_results[1])
						micro_uas.append(evaluate_results[2])
						micro_las.append(evaluate_results[3])
					except:
						macro_uas.append(0)
						macro_las.append(0)
						micro_uas.append(0)
						micro_las.append(0)
						print(parser + '/predict/' + directory + '/' + file_name + '.' + parser + '.' + treebank + '.' + str(seed) + '.' + emb)
				f.write('\t'.join(str(w) for w in [directory, parser, emb, round(statistics.mean(macro_uas), 2), round(statistics.mean(macro_las), 2), round(statistics.mean(micro_uas), 2), round(statistics.mean(micro_las), 2)]) + '\n')
				print(round(statistics.mean(macro_las), 2))
		uuparser_macro_uas = []
		uuparser_macro_las = []
		uuparser_micro_uas = []
		uuparser_micro_las = []

		for seed in [1, 2, 3]:
			try:
				uuparser_pred_file = 'uuparser/predict/' + str(seed) + '/' + treebank_map[directory] + '/' + treebank_map[directory] + '.conllu' 
				uuparser_evaluate = evaluate(gold_file, uuparser_pred_file)
				uuparser_macro_uas.append(uuparser_evaluate[0])
				uuparser_macro_las.append(uuparser_evaluate[1])
				uuparser_micro_uas.append(uuparser_evaluate[2])
				uuparser_micro_las.append(uuparser_evaluate[3])
			except:
				uuparser_macro_uas.append(0)
				uuparser_macro_las.append(0)
				uuparser_micro_uas.append(0)
				uuparser_micro_las.append(0)
				print('uuparser/predict/' + str(seed) + '/' + treebank_map[directory] + '/' + treebank_map[directory] + '.conllu')

		f.write('\t'.join(str(w) for w in [directory, 'uuparser', 'NONE', round(statistics.mean(uuparser_macro_uas), 2), round(statistics.mean(uuparser_macro_las), 2), round(statistics.mean(uuparser_micro_uas), 2), round(statistics.mean(uuparser_micro_las), 2)]) + '\n')


		