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

print("\\begin{table*}[h!]")
print("\\footnotesize")
print("\\centering")
print("\\begin{tabular}{c|c|c|c|c|c|c|c|c}")
print("\\textbf{Child} & \\textbf{18-24} & \\textbf{24-30} & \\textbf{30-36} & \\textbf{36-42} & \\textbf{42-48} & \\textbf{48-54} & \\textbf{54-60} & \\textbf{60-66}  \\\\\\hline")

child_total_n_words = 0
child_total_n_sents = 0

parent_total_n_words = 0
parent_total_n_sents = 0

for child in os.listdir('data/'):
	if child != '.DS_Store':
		child_n_words_list = []
		child_n_sents_list = []
		child_mlu_list = []

		parent_n_words_list = []
		parent_n_sents_list = []
		parent_mlu_list = []

		age_range = ['18_24', '24_30', '30_36', '36_42', '42_48', '48_54', '54_60', '60_66']
		for age in age_range:
			for role in ['child', 'parent']:
				file = child + '_' + age + '.' + role
				try:
					n_words = 0
					n_sents = 0

					child_name = child.split('_')[0]
					corpus = child.split('_')[1]

					with open('data/' + child + '/' + file) as f:
					#	print(child, file)
						sent = conll_read_sentence(f)

						while sent is not None:
							n_words += len(sent)
							n_sents += 1

							sent = conll_read_sentence(f)

					mlu = round(n_words / n_sents,2 )					

					if role == 'child':
						child_total_n_words += n_words
						child_total_n_sents += n_sents
						n_words = str(n_words)
						if len(n_words) > 3:
							temp = n_words
							n_words = temp[0] + ',' + temp[1 : ]
						n_sents = str(n_sents)
						if len(n_sents) > 3:
							temp = n_sents
							n_sents = temp[0] + ',' + temp[1 : ]

						child_n_words_list.append('words: ' + str(n_words))
						child_n_sents_list.append('sents: ' + str(n_sents))
						child_mlu_list.append('MLU: ' + str(mlu))
						

					else:
						parent_total_n_words += n_words
						parent_total_n_sents += n_sents
						n_words = str(n_words)
						if len(n_words) > 3:
							temp = n_words
							n_words = temp[0] + ',' + temp[1 : ]
						n_sents = str(n_sents)
						if len(n_sents) > 3:
							temp = n_sents
							n_sents = temp[0] + ',' + temp[1 : ]

						parent_n_words_list.append('words: ' + str(n_words))
						parent_n_sents_list.append('sents: ' + str(n_sents))
						parent_mlu_list.append('MLU: ' + str(mlu))
			
				except:
					if role == 'child' and age != '60_66':
						child_n_words_list.append(' ')
						child_n_sents_list.append(' ')
						child_mlu_list.append(' ')

					if role == 'parent' and age != '60_66':
						parent_n_words_list.append(' ')
						parent_n_sents_list.append(' ')
						parent_mlu_list.append(' ')

		child_n_words_stats = ' & '.join(w for w in child_n_words_list)
		child_n_sents_stats = ' & '.join(w for w in child_n_sents_list)
		child_mlu_stats = ' & '.join(w for w in child_mlu_list)


		parent_n_words_stats = ' & '.join(w for w in parent_n_words_list)
		parent_n_sents_stats = ' & '.join(w for w in parent_n_sents_list)
		parent_mlu_stats = ' & '.join(w for w in parent_mlu_list)

		print(child_name + ' & ' + child_n_words_stats + ' \\\\')
		print(' & ' + child_n_sents_stats + ' \\\\')
		print(' & ' + child_mlu_stats + ' \\\\')
		print('Parent & ' + parent_n_words_stats + ' \\\\')
		print(' & ' + parent_n_sents_stats + ' \\\\')
		print(' & ' + parent_mlu_stats + ' \\\\\\hline')

print('\\end{tabular}')
print('\\caption{Descriptive statistics for utterances of each child and their parent(s)}')
print('\\label{tab:descriptive_stats}')
print('\\end{table*}')

print(child_total_n_words)
print(child_total_n_sents)
print(parent_total_n_words)
print(parent_total_n_sents)


'''
\begin{table*}[h!]
\footnotesize
	\centering
	\begin{tabular}{c|c|c|c|c|c|c|c|c|c|c}
	\textbf{Child} & \textbf{Corpus} & \textbf{Role} & \textbf{18-24} & \textbf{24-30} & \textbf{30-36} & \textbf{36-42} & \textbf{42-48} & \textbf{48-54} & \textbf{54-60} & \textbf{60-66}  \\\hline
	
Abe &  Child & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark \\
& & Parent & & & & & & & & \\
\hline
Adam &  Child   & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark \\
&  Parent & & & & & & & & \\
Sarah &  Child & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark \\
&  Parent & & & & & & & & \\
\hline
Thomas  & Child & & \checkmark &\checkmark & \checkmark & \checkmark & \checkmark & \checkmark &  \\
&  Parent & & & & & & & & \\
\hline
Emma & Child & & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark &  & \\
& Parent & & & & & & & & \\
Roman &  Child & & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \\
& Parent & & & & & & & & \\
\hline
Laura & Braunwald~\cite{braunwald1971mother} & Child & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark &  \\
& Parent & & & & & & & & \\
\hline
Naima & Child & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & & & \\
& Parent & & & & & & & & \\
Lily &  Child & \checkmark & \checkmark & \checkmark &\checkmark  &\checkmark  & \checkmark  & & \\
& Parent & & & & & & & & \\
Violet &  Child  & \checkmark & \checkmark & \checkmark &\checkmark  &\checkmark  &  & & \\
& Parent & & & & & & & & \\
\hline

	\end{tabular}
	\caption{Descriptive statistics for selected VIP children from CHILDES; \checkmark indicates that there are 2000 words for child and parent utterances, respectively, at the corresponding age of the child. \textbf{CALCULATE MLU}}
	\label{tab:descriptive_stats}
\end{table*}
'''