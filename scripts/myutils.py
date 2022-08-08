import os
import conll18_ud_eval
import sys
from allennlp.common import Params
import urllib.request as urllib
import json

seeds = ['1', '2', '3']
trains = ['ewt']

num_epochs = {'machamp': 20, 'uuparser': 20, 'udify': 20, 'uniparse': 15, 'diaparser': 0, 'stanza': 0}

lms = ["bert-base-cased", "roberta-large",  "cardiffnlp/twitter-roberta-base", "studio-ousia/luke-large", "microsoft/deberta-v3-base",  "microsoft/deberta-v3-large", 'distilbert-base-uncased', "roberta-base",  'bert-base-uncased',  'studio-ousia/luke-base']

treebank_map = {'ewt': ['UD_English-EWT', 'en_ewt-ud-train.conllu', 'en_ewt-ud-dev.conllu', 'en_ewt-ud-test.conllu']}

def getEmbedSize(name):
    with urllib.urlopen("https://huggingface.co/" + name + "/raw/main/config.json") as url:
        data = json.loads(url.read().decode())
        for key in ['hidden_size', 'dim']:
            if key in data:
                return data[key]
    return 0

def makeParams(lm):
    paramsPath = 'configs/params.' + lm.replace('/', '-') + '.json'
    if not os.path.isfile(paramsPath):
        size =getEmbedSize(lm)
        outFile = open(paramsPath, 'w')
        outFile.write('local transformer_model = "' + lm + '";\n')
        outFile.write('local transformer_dim = ' + str(size) + ';\n')
        outFile.write(''.join(open('configs/params.json').readlines()[2:]))
        outFile.close()
    return paramsPath


class conllFile:
    def __init__(self, data):
        self.data = data
        self.idx = -1
    def readline(self):
        self.idx +=1
        if self.idx != len(self.data):
            return self.data[self.idx]

def toConllFile(path):
    data = []
    curSent = []
    for line in open(path):
        curSent.append(line)
        if len(line) < 3:
            data.append(conll18_ud_eval.load_conllu(conllFile(curSent)))
            curSent = []
    return data

def getUdifyModel(name):
    modelDir = 'udify/logs/'
    nameDir = modelDir + name + '/'
    if os.path.isdir(nameDir):
        for modelDir in reversed(os.listdir(nameDir)):
            modelPath = nameDir + modelDir + '/model.tar.gz'
            if os.path.isfile(modelPath):
                return modelPath
    return ''

def getMachampModel(name):
    modelDir = 'mtp/logs/'
    nameDir = modelDir + name + '/'
    if os.path.isdir(nameDir):
        for modelDir in reversed(os.listdir(nameDir)):
            modelPath = nameDir + modelDir + '/model.tar.gz'
            if os.path.isfile(modelPath):
                return modelPath
            modelPath2 = nameDir + modelDir + '/20/model-20.tar.gz'
            if os.path.isfile(modelPath2):
                return modelPath2
    return ''

def getTrainDevTest(path):
    train = ''
    dev = ''
    test = ''
    for conlFile in os.listdir(path):
        if conlFile.endswith('conllu'):
            if 'train' in conlFile:
                train = path + '/' + conlFile
            if 'dev' in conlFile:
                dev = path + '/' + conlFile
            if 'test' in conlFile:
                test = path + '/' + conlFile
    return train, dev, test

def genDataconfig(treebank):
    outPath = 'configs/' + treebank + '.json'
    if os.path.isfile(outPath):
        return outPath
    treebank_info = treebank_map[treebank]
    trainPath = '../UD_data/' + treebank_info[0] + '/' + treebank_info[1]
    valPath = '../UD_data/' + treebank_info[0] + '/' + treebank_info[2]
    base = Params.from_file('configs/ewt.json')
    new = {treebank:base.as_dict()['UD_EWT']}
    new[treebank]['train_data_path'] = '../' + trainPath
#    del new[treebank]['validation_data_path']
#    for task in ['feats', 'lemma', 'upos']:
#        del new[treebank]['tasks'][task]
    newParams = Params(new)
    newParams.to_file(outPath)
    return outPath

def genDataconfigUdify(treebank, trainSize, setupId):
    outPath = 'udify/config/' + treebank + '.json'
    if os.path.isfile(outPath):
        return outPath
    trainPath = 'data/sequential/' + treebank + '/' +trainSize + '/' + setupId + '/train.conllu'
    base = Params.from_file('udify/config/ud/en/udify_bert_finetune_en_ewt.json')
    base['trainer']['num_epochs'] = 20
    base['trainer']['num_serialized_models_to_keep']  = 20
    base['train_data_path'] = trainPath
    base['validation_data_path'] = trainPath
    del base['test_data_path'] 
    del base['model']['decoders']['upos'] 
    del base['model']['decoders']['feats'] 
    del base['model']['decoders']['lemmas'] 
    base.to_file(outPath)
    return outPath.replace('udify', '')
    


french = {'UD_French-Rhapsodie', 'UD_French-GSD', 'UD_French-ParTUT', 'UD_French-Sequoia'}
norwegian = {'UD_Norwegian-Nynorsk', 'UD_Norwegian-NynorskLIA', 'UD_Norwegian-Bokmaal'}
slovenian = {'UD_Slovenian-SSJ', 'UD_Slovenian-SST', 'UD_Croatian-SET', 'UD_Serbian-SET'}
komi = {'UD_Komi_Zyrian-IKDP', 'UD_Finnish-TDT', 'UD_North_Sami-Giella', 'UD_Russian-Taiga'}
najia = {'UD_Naija-NSC', 'UD_English-EWT', 'UD_English-GUM', 'UD_English-LinES', 'UD_English-ParTUT', 'UD_English-LinES'}
hindi = {'UD_Hindi_English-HIENCS', 'UD_Hindi-HDTB', 'UD_English-EWT', 'UD_English-GUM', 'UD_English-LinES', 'UD_English-ParTUT', 'UD_English-LinES'}
italian = {'UD_Italian-PoSTWITA', 'UD_Italian-ISDT', 'UD_Italian-ParTUT', 'UD_Italian-VIT'}

social = {'UD_English-Tweebank2', 'UD_Hindi_English-HIENCS', 'UD_Italian-PoSTWITA'}
spoken = {'UD_French-Rhapsodie', 'UD_Norwegian-NynorskLIA', 'UD_Slovenian-SSJ', 'UD_Komi_Zyrian-IKDP', 'UD_Naija-NSC'}
ood = {"UD_Croatian-SET", "UD_English-EWT", "UD_English-GUM", "UD_English-LinES", "UD_English-ParTUT", "UD_Finnish-TDT", "UD_French-GSD", "UD_French-ParTUT", "UD_French-Sequoia", "UD_Hindi-HDTB", "UD_Italian-ISDT", "UD_Italian-ParTUT", "UD_Italian-VIT", "UD_North_Sami-Giella", "UD_Norwegian-Bokmaal", "UD_Norwegian-Nynorsk", "UD_Russian-Taiga", "UD_Serbian-SET", "UD_Slovenian-SST"}

