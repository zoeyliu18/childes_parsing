### Need to be run within the diaparser folder

#usr/bin/env python3

import io, os, sys
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

#extra = ['disccourse', 'nmod:npmod', 'compound:redup', 'acl:relcls', 'xcompe', 'mod', ',arl', 'cccomp', 'roott', 'dicourse', 'rooot', 'riit', 'reparandum:resstart', 'voca', 'xcom', 'advmo', 'nsuubj', 'xxomp', 'nmod:pposs', 'comj', 'nsub', 'roots', 'compund', 'repparandum:restart', 'åroot', 'ocnj', 'obl:nmod', 'copy', 'compount:prt']
extra = ['xomp', 'repetition:reparandum']

### cycle

def deprel(sent):
	words = []
	for tok in sent:
		deps.append(tok[7])

	return deps


for child in os.listdir('data/'):
	if child != '.DS_Store':
		for file in os.listdir('data/' + child + '/'):
			if file != '.DS_Store':
				with open('data/' + child + '/' + file) as f:
					print(child, file)
					sent = conll_read_sentence(f)
					while sent is not None:
						for tok in sent:
							if tok[1].lower() in ['there', 'dere']:
								try:
									cop = 0
									for a in sent:
										if a[6] == tok[0] and a[1].lower() in ['is', 'was', 'are', 'were', "'s", "'re", "'m"] and int(a[0]) > int(tok[0]):
											cop += 1
									if cop == 0:
										for z in sent:
											if z[6] == tok[0] and z[7] == 'nsubj' and int(z[0]) > int(tok[0]):
												for w in sent:
													print(w)
												print(cop)
								except:
									pass
						sent = conll_read_sentence(f)
						



