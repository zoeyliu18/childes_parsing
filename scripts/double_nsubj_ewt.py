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

with open("en_ewt-ud-train.conllu") as f:
	sent = conll_read_sentence(f)
	while sent is not None:
		n = 0
		head_dep = []
		for tok in sent:
			head_dep.append(tok[6] + ' ' + tok[7])
		for tok in head_dep:
			if tok.endswith('nsubj') and head_dep.count(tok) > 1:
				n += 1
				for z in sent:
					if z[6] + ' ' + z[7] == tok:
						print(z, 'YES')
					else:
						print(z)
				print('\n')
				print('\n')
		sent = conll_read_sentence(f)


