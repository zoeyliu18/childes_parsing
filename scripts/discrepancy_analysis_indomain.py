import io, os, statistics

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


for treebank in ['twitter']:	
	for parser in ['machamp']: #, 'diaparser']:
		for emb in ['cardiffnlp-twitter-roberta-base']:
#		for emb in ['bert-base-cased', 'roberta-base', 'cardiffnlp-twitter-roberta-base']:
			for seed in [1]: #, 2, 3]:
				reparandum_ratio = []
				reparandum_restart_ratio = []
				reparandum_repetition_ratio = []
				reparandum_different_ratio = []
				reparandum_restart_different_ratio = []
				reparandum_repetition_different_ratio = []
		
				for age_range in ['18_24', '24_30', '30_36', '36_42', '42_48', '48_54', '54_60', '60_66']:
					for role in ['child']:
				#	for role in ['child', 'parent']:
						everything = 0
						total_different = 0
						discrepancies = {}
						details = {}

						reparandum = 0
						reparandum_repetition = 0
						reparandum_restart = 0
						reparandum_different = 0
						reparandum_repetition_different = 0
						reparandum_restart_different = 0

						n = 0
						total_sent = 0

						for directory in ['Abe_Kuczaj', 'Adam_Brown', 'Sarah_Brown']:
							for gold_file in os.listdir('processed_data/' + directory):
								if role in gold_file and age_range in gold_file:
									file_name = gold_file.split('.')
									role = file_name[1]
									file_name = file_name[0].split('_')
									pred_file = 'predict/' + parser + '/' + directory + '_indomain/' + gold_file + '.' + parser + '.' + treebank + '.' + str(seed) + '.' + emb + '.indomain'
									gold_parses = get_parse('processed_data/' + directory + '/' + gold_file)
									pred_parses = get_parse(pred_file)


									for i in range(len(gold_parses)):
										gold_sent = gold_parses[i]
										pred_sent = pred_parses[i]

										total_sent += 1
										if gold_sent != pred_sent:
											if len(gold_sent) <= 4:
												n += 1

										for z in range(len(gold_sent)):
											everything += 1
											gold_head = gold_sent[z][6]
											gold_deprel = gold_sent[z][7]

											pred_head = pred_sent[z][6]
											pred_deprel = pred_sent[z][7]

											if gold_deprel == 'reparandum':
												reparandum += 1
											if gold_deprel == 'reparandum:repetition':
												reparandum_repetition += 1
											if gold_deprel == 'reparandum:restart':
												reparandum_restart += 1

											if gold_deprel != pred_deprel:
												total_different += 1
												if gold_deprel == 'reparandum':
													reparandum_different += 1
												if gold_deprel == 'reparandum:repetition':
													reparandum_repetition_different += 1
												if gold_deprel == 'reparandum:restart':
													reparandum_restart_different += 1

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

										#		if gold_deprel == 'root':
										#			print(' '.join(w[1] for w in gold_sent))
										#			for w in range(len(gold_sent)):
										#				print(gold_sent[w], pred_sent[w])
										#			print('\n')
				

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


					#	print(treebank)
					#	print(parser)
					#	print(emb)
						try:
							print(role)
							print(age_range)
							for k, v in discrepancies_proportion.items():
								if 'reparandum' in k:
									print(k, v, details_proportion[k])
							#	if v >= 5:
							#		print(k, v, details_proportion[k])

							print('\n')
							print('reparandum')
							print(reparandum, everything)
							print(round(reparandum * 100 / everything, 2))
							reparandum_ratio.append(round(reparandum * 100 / everything, 2))
							print(reparandum_different, reparandum)
							print(round(reparandum_different * 100 / reparandum, 2))
							reparandum_different_ratio.append(round(reparandum_different * 100 / reparandum, 2))
							print('\n')
							print('reparandum_repetition')
							print(reparandum_repetition, everything)						
							print(round(reparandum_repetition * 100 / everything, 2))
							reparandum_repetition_ratio.append(round(reparandum_repetition * 100 / everything, 2))
							print(reparandum_repetition_different, reparandum_repetition)
							print(round(reparandum_repetition_different * 100 / reparandum_repetition, 2))
							reparandum_repetition_different_ratio.append(round(reparandum_repetition_different * 100 / reparandum_repetition, 2))
							print('\n')
							print('reparandum_restart')
							print(reparandum_restart, everything)
							print(round(reparandum_restart * 100 / everything, 2))
							reparandum_restart_ratio.append(round(reparandum_restart * 100 / everything, 2))
							print(reparandum_restart_different, reparandum_restart)
							print(round(reparandum_restart_different * 100 / reparandum_restart, 2))
							reparandum_restart_different_ratio.append(round(reparandum_restart_different * 100 / reparandum_restart, 2))
							print('\n')
							print('\n')
							print(n * 100 / total_sent)
							print('\n')
							print('\n')

						except:
							pass


				print(statistics.mean(reparandum_ratio))
				print(statistics.mean(reparandum_different_ratio))
				print('\n')
				print(statistics.mean(reparandum_repetition_ratio))
				print(statistics.mean(reparandum_repetition_different_ratio))
				print('\n')
				print(statistics.mean(reparandum_restart_ratio))
				print(statistics.mean(reparandum_restart_different_ratio))


