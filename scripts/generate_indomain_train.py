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


for child in ['Abe_Kuczaj', 'Adam_Brown', 'Emma_Weist', 'Laura_Braunwald', 'Lily_Providence', 'Naima_Providence', 'Roman_Weist', 'Sarah_Brown', 'Thomas_Thomas', 'Violet_Providence']:
  train = []
  for directory in os.listdir('processed_data/'):
    if directory != child:
      for file in os.listdir('processed_data/' + directory + '/'):
        if file.endswith('child') or file.endswith('parent'):
          with open('processed_data/' + directory + '/' + file) as f:
            sent = conll_read_sentence(f)
            while sent is not None:
              train.append(sent)
              sent = conll_read_sentence(f)
  
  with open('processed_data/' + child + '/train.conllu', 'w') as f:
    for sent in train:
      for tok in sent:
        f.write('\t'.join(w for w in tok) + '\n')
      f.write('\n')


					