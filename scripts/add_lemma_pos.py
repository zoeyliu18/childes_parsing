import io, os, argparse
import stanza

en_nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,lemma', tokenize_pretokenized=True)

### Read *.conllu file ###

def conll_read_sentence(file_handle):

	sent = []

	for line in file_handle:
		line = line.strip('\n')
		if line.startswith('#') is False :
			toks = line.split("\t")		
			if len(toks) != 10:
				return sent 
			else:
				if toks[0].isdigit() == True:
					sent.append(toks)

	return None


### Getting POS and Lemma features from Stanza ###

def get_features(sentence):
	tokens = []
	head_list = []
	deprel_list = []
	for tok in sentence:
		tokens.append(tok[1])
		head_list.append(tok[6])
		deprel_list.append(tok[7])

	utterance = ' '.join(w for w in tokens)

	parse_info = en_nlp(utterance)

	parse_results = []

	for sent in parse_info.sentences:
		for i in range(len(sent.words)):
			word = sent.words[i]
			w_id = word.id
			w_text = word.text
			w_lemma = word.lemma
			w_upos = word.upos
			w_xpos = word.xpos
			w_feats = word.feats
			w_head = ''
			w_head = head_list[i]
			w_deprel = deprel_list[i]
			parse_results.append([w_id, w_text, w_lemma, w_upos, w_xpos, w_feats, w_head, w_deprel, sentence[0][-2], sentence[0][-1]])

	return parse_results

def sentence_count(file_handle):
	n_sentences = 0
	with open(file_handle) as f:
		for line in f:
			if line.startswith('# text = '):
				n_sentences += 1
	return n_sentences


for child in os.listdir('data/'):
	if child != '.DS_Store':
		if not os.path.exists('processed_data/' + child):
			os.system('mkdir processed_data/' + child)

		for file in os.listdir('data/' + child + '/'):
			if file != '.DS_Store':
				new_sent_count = 0
				ref_sent_count = sentence_count('data/' + child + '/' + file)
				if file in os.listdir('processed_data/' + child + '/'):
					new_sent_count = sentence_count('processed_data/' + child + '/' + file)

				if new_sent_count != ref_sent_count:
			#	if file == 'Thomas_Thomas_24_30.parent':
					try:
						all_sentences = []
						file_texts = []
						file_features = []
						with open('data/' + child + '/' + file) as f:
							sent = conll_read_sentence(f)
							while sent is not None:
								all_sentences.append(sent)
								sent = conll_read_sentence(f)

						for sent in all_sentences:
							features = get_features(sent)
							file_features.append(features)

						with open('data/' + child + '/' + file) as f:
							for line in f:
								if line.startswith('# text = '):
									file_texts.append(line.strip())

						assert len(file_texts) == len(file_features)

						with open('processed_data/' + child + '/' + file, 'w') as new_f:
							for i in range(len(file_texts)):
								text = file_texts[i]
								features = file_features[i]
								new_f.write(text + '\n')
								for feature in features:
									new_f.write('\t'.join(str(w) for w in feature) + '\n')
								new_f.write('\n')


					except:
						print(file, 'CHECK')













