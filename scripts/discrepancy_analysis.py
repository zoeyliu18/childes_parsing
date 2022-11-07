import io, os

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


for treebank in ['ewt', 'twitter', 'esl']:	
	for parser in ['machamp']: #, 'diaparser']:
		for emb in ['cardiffnlp-twitter-roberta-base']:
#		for emb in ['bert-base-cased', 'roberta-base', 'cardiffnlp-twitter-roberta-base']:
			for seed in [1]: #, 2, 3]:
			#	for age_range in ['18_24', '24_30']:			
				for age_range in ['48_54']: #['18_24', '24_30']: #, '30_36', '36_42', '42_48', '48_54', '54_60', '60_66']:
					for role in ['child']:
				#	for role in ['child', 'parent']:
						total_different = 0
						discrepancies = {}
						details = {}
						for directory in os.listdir('processed_data/'):
							for gold_file in os.listdir('processed_data/' + directory):
								if role in gold_file and age_range in gold_file:
									file_name = gold_file.split('.')
									role = file_name[1]
									file_name = file_name[0].split('_')
									pred_file = 'predict/' + parser + '/' + directory + '/' + gold_file + '.' + parser + '.' + treebank + '.' + str(seed) + '.' + emb
						
									gold_parses = get_parse('processed_data/' + directory + '/' + gold_file)
									pred_parses = get_parse(pred_file)

									for i in range(len(gold_parses)):
										gold_sent = gold_parses[i]
										pred_sent = pred_parses[i]

										for z in range(len(gold_sent)):
											gold_head = gold_sent[z][0]
											gold_deprel = gold_sent[z][1]

											pred_head = pred_sent[z][0]
											pred_deprel = pred_sent[z][1]

											if gold_deprel != pred_deprel:
												total_different += 1
												if gold_deprel not in discrepancies:
													discrepancies[gold_deprel] = 1
												else:
													discrepancies[gold_deprel] += 1

												if gold_deprel not in details:
													details[gold_deprel] = {}
													details[gold_deprel][pred_deprel] = 1
												else:
													if pred_deprel not in details[gold_deprel]:
														details[gold_deprel][pred_deprel] = 1
													else:
														details[gold_deprel][pred_deprel] += 1
				

						discrepancies_proportion = {}
						for k, v in discrepancies.items():
							discrepancies_proportion[k] = round(v * 100 / total_different, 2)

						discrepancies_proportion = {k: v for k, v in sorted(discrepancies_proportion.items(), key=lambda item: item[1], reverse = True)}
						
						details_proportion = {}
						for k, v in details.items():
							deprel_proportion = {}
							total = 0
							for z, w in v.items():
								total += w
							for z, w in v.items():
								if round(w * 100 / total, 2) >= 5:
									deprel_proportion[z] = round(w * 100 / total, 2)
							details_proportion[k] = deprel_proportion


						print(treebank)
						print(parser)
						print(emb)
						print(role)
						print(age_range)
						for k, v in discrepancies_proportion.items():
							if v >= 5:
								print(k, v, details_proportion[k])

						print('\n')
						print('\n')


