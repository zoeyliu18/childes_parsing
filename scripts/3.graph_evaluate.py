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


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type = str, help = 'path to ud_data/')

	args = parser.parse_args()

	if not os.path.exists('evaluate'):
		os.system('mkdir evaluate/')

	if not os.path.exists('evaluate/graph'):
		os.system('mkdir evaluate/graph')

	for directory in os.listdir(args.input):
		print(directory)
		if os.path.isdir(args.input + directory) and directory.startswith('UD'):
			if not os.path.exists('evaluate/graph/' + directory):
				os.system('mkdir evaluate/graph/' + directory)

			gold_file = ''
			filename = ''

			for file in os.listdir(args.input + directory):
				if file.endswith('test.conllu') or file.endswith('test.fixed.conllu'):
					filename = file
					gold_file = args.input + directory + '/' + file

			bert_pred_file = 'predict/graph/' + directory + '/bert-cased/' + filename
			roberta_pred_file = 'predict/graph/' + directory + '/roberta-large/' + filename
		#	rembert_pred_file = 'predict/graph/' + directory + '/rembert/' + filename

			bert_evaluate = evaluate(gold_file, bert_pred_file)
			roberta_evaluate = evaluate(gold_file, roberta_pred_file)
		#	rembert_evaluate = evaluate(gold_file, rembert_pred_file)
			print(bert_evaluate)
			print(roberta_evaluate)
			header = ['Treebank', 'Parser', 'Embedding', 'Macro_UAS', 'Macro_LAS', 'Micro_UAS', 'Micro_LAS']
		
		#	with open('evaluate/graph/' + directory + '/' + 'eval.txt', 'w') as f:
		#		f.write('\t'.join(w for w in header) + '\n')
		#		f.write('\t'.join(str(w for w in [directory, 'diaparser', 'bert', bert_evaluate[0], bert_evaluate[1], bert_evaluate[2], bert_evaluate[3]])) + '\n')
		#		f.write('\t'.join(str(w for w in [directory, 'diaparser', 'roberta-large', roberta_evaluate[0], roberta_evaluate[1], roberta_evaluate[2], roberta_evaluate[3]])) + '\n')
		#		f.write('\t'.join(str(w for w in [directory, 'diaparser', 'rembert', rembert_evaluate[0], rembert_evaluate[1], rembert_evaluate[2], rembert_evaluate[3]])) + '\n')


			f = open('evaluate/graph/' + directory + '/' + 'eval.txt', 'w')
			f.write('\t'.join(w for w in header) + '\n')
			f.write('\t'.join(str(w for w in [directory, 'diaparser', 'bert', bert_evaluate[0], bert_evaluate[1], bert_evaluate[2], bert_evaluate[3]])) + '\n')
			f.write('\t'.join(str(w for w in [directory, 'diaparser', 'roberta-large', roberta_evaluate[0], roberta_evaluate[1], roberta_evaluate[2], roberta_evaluate[3]])) + '\n')
		#	f.write('\t'.join(str(w for w in [directory, 'diaparser', 'rembert', rembert_evaluate[0], rembert_evaluate[1], rembert_evaluate[2], rembert_evaluate[3]])) + '\n')



