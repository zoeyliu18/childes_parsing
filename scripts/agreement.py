import io, os
from sklearn.metrics import cohen_kappa_score

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

annotations_macro = []

A_annotations = []
B_annotations = []

by_child_macro = []
by_child_micro = []

for child in os.listdir('data/'):
	if child != '.DS_Store':

		child_annotations_macro = []
		child_A_annotations = []
		child_B_annotations = []

		for file in os.listdir('data/' + child + '/'):
			if file != '.DS_Store':
				with open('data/' + child + '/' + file) as f:
					print(child, file)
					sent = conll_read_sentence(f)

					while sent is not None:
						if sent[0][4] != '_':
							a_tree = []
							b_tree = []
							for tok in sent:
								a_head = tok[4]
								a_deprel = tok[5]
								if a_deprel.endswith('='):
									a_deprel = a_deprel[ : -1]
								a_tree.append(a_head + '_' + a_deprel)
								A_annotations.append(a_head + '_' + a_deprel)
								child_A_annotations.append(a_head + '_' + a_deprel)

								b_head = tok[6]
								b_deprel = tok[7]
								b_tree.append(b_head + '_' + b_deprel)
								B_annotations.append(b_head + '_' + b_deprel)
								child_B_annotations.append(b_head + '_' + b_deprel)

							score = cohen_kappa_score(a_tree, b_tree)
							annotations_macro.append(score)
							child_annotations_macro.append(score)

						sent = conll_read_sentence(f)

		child_annotations_macro = sum(child_annotations_macro) / len(child_annotations_macro)
		by_child_macro.append(child_annotations_macro)
		by_child_micro.append(cohen_kappa_score(child_A_annotations, child_B_annotations))

macro_agreement = sum(annotations_macro) / len(annotations_macro)
micro_agreement = cohen_kappa_score(A_annotations, B_annotations)

print(macro_agreement)
print(micro_agreement)
print(sum(by_child_macro) / len(by_child_macro))
print(sum(by_child_micro) / len(by_child_micro))
