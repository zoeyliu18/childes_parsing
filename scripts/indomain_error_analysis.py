import io, os

data = []
with open('results/childes_indomain_regression_dl.txt') as f:
	for line in f:
		toks = line.strip().split('\t')
		data.append(toks)

data = data[1 : ]

age_range_list = [[18, 24], [24, 30], [30, 36], [36, 42], [42, 48], [48, 54], [54, 60], [60, 66]]

for age_range in age_range_list:
	discrepancies = {}
	for i in range(len(data)):
		tok = data[i]
		age = float(tok[3])
		if age >= age_range[0] and age < age_range[1] and tok[-2] != tok[-1]:
			gold_deprel = tok[-2]
			pred_deprel = tok[-1]
		#	if gold_deprel not in discrepancies:
		#		discrepancies[gold_deprel] = []
		#		discrepancies[gold_deprel].append(pred_deprel)
		#	else:
		#		discrepancies[gold_deprel].append(pred_deprel)

			if pred_deprel not in discrepancies:
				discrepancies[pred_deprel] = []
				discrepancies[pred_deprel].append(gold_deprel)
			else:
				discrepancies[pred_deprel].append(gold_deprel)

	new_discrepancies = {}
	for k, v in discrepancies.items():
		new_v = {}
		for deprel in set(v):
			new_v[deprel] = v.count(deprel)
		new_discrepancies[k] = new_v

#	discrepancies = {k: v for k, v in sorted(discrepancies_proportion.items(), key=lambda item: item[1], reverse = True)}
	
	print(age_range)
	print('\n')
	discrepancies_proportion = {}
	discrepancies_proportion_list = []
	for k, v in new_discrepancies.items():
		k_total = 0
		for w, z in v.items():
			k_total += z
		discrepancies_proportion[k] = k_total
		discrepancies_proportion_list.append(k_total)
	discrepancies_proportion_list.sort()
	for proportion in discrepancies_proportion_list[-3 : ]:
		for a, b in discrepancies_proportion.items():
			if b == proportion:
				print(a, b)
				for g, h in new_discrepancies[a].items():
					print(g, h)
				print('\n')
		#		if b == proportion:
		#			print(a, b)
		#			for g, h in v.items():
		#				print(g, h)
			#		print('\n')

	print('\n')