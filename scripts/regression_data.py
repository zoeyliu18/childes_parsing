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
				info.append(tok)
			parses.append(info)

			sent = conll_read_sentence(f)

	return parses

### Evaluation ###

def evaluate(gold, pred):

	gold_parses = get_parse(gold)
	pred_parses = get_parse(pred)

	assert len(gold_parses) == len(pred_parses)

	all_info = []

	test_set_size = 0

	for i in range(len(gold_parses)):
		gold_sent = gold_parses[i]
		pred_sent = pred_parses[i]

		sent_len = len(gold_sent)
		test_set_size += sent_len
		total_dl = 0

		sent_macro_uas = 0
		sent_macro_las = 0

		age = ''

		for z in range(len(gold_sent)):
			age = gold_sent[z][-1].split()[1]
			gold_head = gold_sent[z][6]
			gold_deprel = gold_sent[z][7]
			gold_dependent = gold_sent[z][0]

			if gold_head != 'root':
				total_dl += abs(int(gold_head) - int(gold_dependent))

			pred_head = pred_sent[z][6]
			pred_deprel = pred_sent[z][7]

			if gold_head == pred_head:
				sent_macro_uas += 1
			if gold_head == pred_head and gold_deprel == pred_deprel:
				sent_macro_las += 1

		sent_macro_uas = sent_macro_uas / len(gold_sent)
		sent_macro_las = sent_macro_las / len(gold_sent)

		ave_dl = total_dl / (len(gold_sent) - 1)

		info = [age, sent_len, ave_dl, sent_macro_uas, sent_macro_las]
		all_info.append(info)

	return all_info, test_set_size


### Evaluation by dependency length###

def dl_evaluate(gold, pred):

	gold_parses = get_parse(gold)
	pred_parses = get_parse(pred)

	assert len(gold_parses) == len(pred_parses)

	all_info = []

	for i in range(len(gold_parses)):
		gold_sent = gold_parses[i]
		pred_sent = pred_parses[i]

		for z in range(len(gold_sent)):
			age = gold_sent[z][-1].split()[1]
			gold_head = gold_sent[z][6]
			gold_deprel = gold_sent[z][7]
			gold_dependent = gold_sent[z][0]
		
			pred_head = pred_sent[z][6]
			pred_deprel = pred_sent[z][7]
			uas_acc = ''
			las_acc = ''

			if gold_deprel != 'root':
				dl = int(gold_head) - int(gold_dependent)
				dl_direction = ''
				if dl < 0:
					dl_direction = 'initial'
				if dl > 0:
					dl_direction = 'final'

				dl = abs(dl)

				if gold_head == pred_head:
					uas_acc = 'yes'
				else:
					uas_acc = 'no'
				if gold_head == pred_head and gold_deprel == pred_deprel:
					las_acc = 'yes'
				else:
					las_acc = 'no'

				info = [age, dl, dl_direction, uas_acc, las_acc, gold_deprel, pred_deprel]
				print(info)
				all_info.append(info)

	return all_info

header = ['Child', 'Corpus', 'Role', 'Train_size', 'Test_size', 'Size_ratio', 'Age', 'Sent_len', 'DL', 'UAS_Accuracy', 'LAS_Accuracy']
f = open('results/childes_indomain_regression.txt', 'w')
f.write('\t'.join(w for w in header) + '\n')

dl_header = ['Child', 'Corpus', 'Role', 'Age', 'DL', 'DL_Direction', 'UAS_Accuracy', 'LAS_Accuracy', 'Gold_Deprel', 'Pred_Deprel']
		
dl_f = open('results/' + 'childes_indomain_regression_dl.txt', 'w')
dl_f.write('\t'.join(w for w in dl_header) + '\n')

for directory in os.listdir('processed_data/'):
	train_data = get_parse('processed_data/' + directory + '/train.conllu')
	train_size = 0
	for parse in train_data:
		train_size += len(parse)

	for gold_file in os.listdir('processed_data/' + directory):
		if gold_file.endswith('.child') or gold_file.endswith('parent'):
			file_name = gold_file.split('.')
			role = file_name[1]
			file_name = file_name[0].split('_')
			child = file_name[0]
			corpus = file_name[1]
			min_age = file_name[2]
			max_age = file_name[3]

#			macro_uas = []
#			macro_las = []
#			micro_uas = []
#			micro_las = []
			
			for seed in [1]: #, 2, 3]:
				pred_file = 'predict/machamp/' + directory + '_indomain/' + gold_file + '.machamp.twitter.' + str(seed) + '.cardiffnlp-twitter-roberta-base.indomain'
				
				evaluate_info, test_set_size = evaluate('processed_data/' + directory + '/' + gold_file, pred_file)

				for info in evaluate_info:
					new_tok = [child, corpus, role, train_size, test_set_size, train_size / test_set_size]
					for tok in info:
						new_tok.append(tok)
					f.write('\t'.join(str(w) for w in new_tok) + '\n')

				dl_evaluate_info = dl_evaluate('processed_data/' + directory + '/' + gold_file, pred_file)

				for info in dl_evaluate_info:
					new_tok = [child, corpus, role]
					for tok in info:
						new_tok.append(tok)
					dl_f.write('\t'.join(str(w) for w in new_tok) + '\n')
