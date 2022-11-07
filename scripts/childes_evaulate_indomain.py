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


### Evaluation by age ###

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
			gold_head = gold_sent[z][6]
			gold_deprel = gold_sent[z][7]

			pred_head = pred_sent[z][6]
			pred_deprel = pred_sent[z][7]

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
			
			gold_head = gold_sent[z][6]
			gold_deprel = gold_sent[z][7]
		
			pred_head = pred_sent[z][6]
			pred_deprel = pred_sent[z][7]

			if gold_head == pred_head:
				micro_uas += 1
			if gold_head == pred_head and gold_deprel == pred_deprel:
				micro_las += 1

	micro_uas = round(100 * micro_uas / total, 2)
	micro_las = round(100 * micro_las / total, 2)

	return [macro_uas, macro_las, micro_uas, micro_las]


### Evaluation by utterance length ###

def ul_evaluate(gold, pred):

	gold_parses = get_parse(gold)
	pred_parses = get_parse(pred)

	assert len(gold_parses) == len(pred_parses)

	### Gettin unique sentence lengths

	unique_sent_len_list = []
	for i in range(len(gold_parses)):
		gold_sent = gold_parses[i]
		sent_len = len(gold_sent)
		if sent_len not in unique_sent_len_list:
			unique_sent_len_list.append(sent_len)

	all_info = []

	### Macro: calculate for each sentence, then divide by number of sentences ###

	for unique_sent_len in unique_sent_len_list:
		macro_uas = 0
		macro_las = 0
		c = 0
		for i in range(len(gold_parses)):
			gold_sent = gold_parses[i]
			sent_len = len(gold_sent)
			if sent_len == unique_sent_len:
				c += 1
				pred_sent = pred_parses[i]
				sent_macro_uas = 0
				sent_macro_las = 0

				for z in range(len(gold_sent)):
					gold_head = gold_sent[z][6]
					gold_deprel = gold_sent[z][7]

					pred_head = pred_sent[z][6]
					pred_deprel = pred_sent[z][7]

					if gold_head == pred_head:
						sent_macro_uas += 1
					if gold_head == pred_head and gold_deprel == pred_deprel:
						sent_macro_las += 1

				sent_macro_uas = sent_macro_uas / len(gold_sent)
				sent_macro_las = sent_macro_las / len(gold_sent)

				macro_uas += sent_macro_uas
				macro_las += sent_macro_las

		macro_uas = round(100 * macro_uas / c, 2)
		macro_las = round(100 * macro_las / c, 2)

	### Micro: combining all sentences together ###

		micro_uas = 0
		micro_las = 0
		total = 0

		for i in range(len(gold_parses)):
			gold_sent = gold_parses[i]
			sent_len = len(gold_sent)
			if sent_len == unique_sent_len:
				pred_sent = pred_parses[i]
				sent_macro_uas = 0
				sent_macro_las = 0

				total += sent_len

				for z in range(len(gold_sent)):
			
					gold_head = gold_sent[z][6]
					gold_deprel = gold_sent[z][7]
		
					pred_head = pred_sent[z][6]
					pred_deprel = pred_sent[z][7]

					if gold_head == pred_head:
						micro_uas += 1
					if gold_head == pred_head and gold_deprel == pred_deprel:
						micro_las += 1

		micro_uas = round(100 * micro_uas / total, 2)
		micro_las = round(100 * micro_las / total, 2)

		all_info.append([unique_sent_len, macro_uas, macro_las, micro_uas, micro_las])

	return all_info


header = ['Child', 'Corpus', 'Age', 'Role', 'Macro_UAS', 'Macro_LAS', 'Micro_UAS', 'Micro_LAS']
		
f = open('results/' + 'childes_indomain_eval.txt', 'w')
f.write('\t'.join(w for w in header) + '\n')

ul_header = ['Child', 'Corpus', 'Role', 'Sent_len', 'Micro_LAS']
		
ul_f = open('results/' + 'childes_indomain_eval_ul.txt', 'w')
ul_f.write('\t'.join(w for w in ul_header) + '\n')

for directory in os.listdir('processed_data/'):
	data_seed1 = []
	data_seed2 = []
	data_seed3 = []	
	ul_evaluate_dict = {}
	for gold_file in os.listdir('processed_data/' + directory):
		if gold_file.endswith('.child') or gold_file.endswith('parent'):
			file_name = gold_file.split('.')
			role = file_name[1]
			file_name = file_name[0].split('_')
			child = file_name[0]
			corpus = file_name[1]
			min_age = file_name[2]
			max_age = file_name[3]

			macro_uas = []
			macro_las = []
			micro_uas = []
			micro_las = []

			for seed in [1, 2, 3]:
			#	try:
				if 2 > 1:
					pred_file = 'predict/machamp/' + directory + '_indomain/' + gold_file + '.machamp.twitter.' + str(seed) + '.cardiffnlp-twitter-roberta-base.indomain'
				
					evaluate_results = evaluate('processed_data/' + directory + '/' + gold_file, pred_file)

					macro_uas.append(evaluate_results[0])
					macro_las.append(evaluate_results[1])
					micro_uas.append(evaluate_results[2])
					micro_las.append(evaluate_results[3])
#				except:
#					macro_uas.append(0)
#					macro_las.append(0)
#					micro_uas.append(0)
#					micro_las.append(0)
#					print('predict/machamp/' + directory + '_indomain/' + gold_file + '.machamp.twitter.' + str(seed) + '.cardiffnlp-twitter-roberta-base.indomain'
		
			
					ul_evaluate_results = ul_evaluate('processed_data/' + directory + '/' + gold_file, pred_file)
					for tok in ul_evaluate_results:
						new_info = [child, corpus, role, tok[0]]
						new_info = '\t'.join(str(w) for w in new_info)
						print(new_info)
						if new_info not in ul_evaluate_dict:
							ul_evaluate_dict[new_info] = [tok[-1]]
						else:
							ul_evaluate_dict[new_info].append(tok[-1])
						print(ul_evaluate_dict[new_info])
						new_tok = ''

			f.write('\t'.join(str(w) for w in [child, corpus, min_age + '_' + max_age, role, round(statistics.mean(macro_uas), 2), round(statistics.mean(macro_las), 2), round(statistics.mean(micro_uas), 2), round(statistics.mean(micro_las), 2)]) + '\n')


	new_ul_evaluate_dict = {}
	for k, v in ul_evaluate_dict.items():
	#	assert len(v) == 3
		new_v = sum(v) / len(v)

		ul_f.write(k + '\t' + str(new_v) + '\n')
