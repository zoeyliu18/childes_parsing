#usr/bin/env python3

import io, os, argparse, random

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


### Get all parses from combined data (either train + dev, or just train) ###

def get_data(file):

	data = []

	with io.open(file, encoding = 'utf-8') as f:
		sent = conll_read_sentence(f)

		while sent is not None:

			### Select all unique sentences ###
			if sent not in data:
				data.append(sent)

			sent = conll_read_sentence(f)

	return data


### Build data sets of given sizes ###

def build_dataset(directory, data, train_size, train_n, dev_size, dev_n):

	if not os.path.exists('data/' + directory):
		os.system('mkdir data/' + directory)

	if not os.path.exists('data/' + directory + '/' + str(train_size)):
		os.system('mkdir data/' + directory + '/' + str(train_size))

	for i in range(train_n):
		train_idx = i + 1
		train_idx_data = []
		train_idx_size = 0

		while train_idx_size != train_size:

			### Sample sentences without replacement, allowing wiggle room ###
			sent = random.sample(data, k = 1)[0]
			if sent not in train_idx_data:
				train_idx_size += len(sent)
				train_idx_data.append(sent)

			if train_idx_size >= train_size - 10 and train_idx_size <= train_size + 10:
				break
		
			if train_idx_size > train_size + 10:
				train_idx_data = train_idx_data[ : -1]
				break

		if not os.path.exists('data/' + directory + '/' + str(train_size) + '/' + str(train_idx)):
			os.system('mkdir data/' + directory + '/' + str(train_size) + '/' + str(train_idx))

			with io.open('data/' + directory + '/' + str(train_size) + '/' + str(train_idx) + '/train.conllu', 'w') as f:
				for sent in train_idx_data:
					for tok in sent:
						f.write('\t'.join(w for w in tok) + '\n')
					f.write('\n')

		if not os.path.exists('data/' + directory + '/' + str(train_size) + '/' + str(train_idx) + '/' + str(dev_size)):
			os.system('mkdir data/' + directory + '/' + str(train_size) + '/' + str(train_idx) + '/' + str(dev_size))

		selected_dev_data = []

		for z in range(int(dev_n)):
			dev_idx = z + 1
			dev_idx_data = []
			dev_idx_size = 0

			### No overlap between each train set and its corresponding dev sets ###
			rest_data = []
			for sent in data:
				if sent not in train_idx_data and sent not in selected_dev_data:
					rest_data.append(sent)

			if len(rest_data) < dev_size - 10:
				break

			while dev_idx_size != dev_size:

				### Sample sentences without replacement, allowing wiggle room ###
				sent = random.sample(rest_data, k = 1)[0]
				if sent not in dev_idx_data:
					dev_idx_size += len(sent)
					dev_idx_data.append(sent)

				if dev_idx_size >= dev_size - 10 and dev_idx_size <= dev_size + 10:
					break
		
				if dev_idx_size > dev_size + 10:
					dev_idx_data = dev_idx_data[ : -1]
					break

			for sent in dev_idx_data:
				selected_dev_data.append(sent)

			if not os.path.exists('data/' + directory + '/' + str(train_size) + '/' + str(train_idx) + '/' + str(dev_size) + '/' + str(dev_idx)):
				os.system('mkdir data/' + directory + '/' + str(train_size) + '/' + str(train_idx) + '/' + str(dev_size) + '/' + str(dev_idx))

				with io.open('data/' + directory + '/' + str(train_size) + '/' + str(train_idx) + '/' + str(dev_size) + '/' + str(dev_idx) + '/dev.conllu', 'w') as f:
					for sent in dev_idx_data:
						for tok in sent:
							f.write('\t'.join(w for w in tok) + '\n')
						f.write('\n')


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type = str, help = 'path to UD directory')
	parser.add_argument('--output', type = str, help = 'output path')
	parser.add_argument('--train_size', type = str, help = 'training set size, based on N of words')
	parser.add_argument('--train_n', type = str, help = 'number of training sets to be constructed')
	parser.add_argument('--dev_size', type = str, help = 'dev set size, based on N of words')
	parser.add_argument('--dev_n', type = str, help = 'number of dev sets to be constructed')

	args = parser.parse_args()

	if not os.path.exists('data'):
		os.system('mkdir data/')

	for directory in os.listdir(args.input):
		if os.path.isdir(args.input + directory) and directory.startswith('UD'):
			train_file = ''
			dev_file = ''
			test_file = ''

			if directory == 'UD_Hindi_English-HIENCS': #!= 'Tweebank':
				for file in os.listdir(args.input + directory):
					if file.endswith('train.conllu'):
						train_file = file
					if file.endswith('dev.conllu'):
						dev_file = file
					if file.endswith('test.conllu'):
						test_file = file

				if train_file != '' and test_file != '':
					train_data = get_data(args.input + directory + '/' + train_file)
					data = train_data

					### If treebank has a dev set, combine training and dev set for data sets construction ###

					if dev_file != '':					
						dev_data = get_data(args.input + directory + '/' + dev_file)
						data = data + dev_data

					total = len(data)
					train_size = int(args.train_size)
					dev_size = int(args.dev_size)

					if total < train_size + dev_size - 20:
						print(directory + ': ' + str(total) + ' ' + str(train_size + dev_size))

					else:
						### Start with contructing training sets that have no overlap between each other ###
						train_n = int(total / train_size)
						dev_n = int((total - train_size) / dev_size)

						build_dataset(directory, data, train_size, train_n, dev_size, dev_n)

				if directory == 'Tweebank':
					train_data = get_data(args.input + directory + '/en-ud-tweet-train.fixed.conllu')
					dev_data = get_data(args.input + directory + '/en-ud-tweet-dev.fixed.conllu')
					data = train_data + dev_data

					total = len(data)
					train_size = int(args.train_size)
					dev_size = int(args.dev_size)

					if total < train_size + dev_size - 20:
						print(directory + ': ' + str(total) + ' ' + str(train_size + dev_size))

					else:
						### Start with contructing training sets that have no overlap between each other ###
						train_n = int(total / train_size)
						dev_n = int((total - train_size) / dev_size)

						build_dataset(directory, data, train_size, train_n, dev_size, dev_n)