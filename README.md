# child_syntax: Child and Parent speech annotated with adaptations of the Universal Dependencies framework

## Train graph-based parser based on out-of-domain UD-style data

### Data preparation

```scripts/0.prep.sh```

(1) From [Universal Dependencies](https://universaldependencies.org/), download the following treebanks

<pre>(a) UD-EWT <br>
(b) UD-GUM reddit (then build the reddit corpus following [instructions](https://github.com/amir-zeldes/gum/blob/master/README_reddit.md) <br>
(c) UD-Atis
</pre>

(2) Download [English Tweeter data](https://github.com/Oneplus/Tweebank) (use the converted version in the experiments)

(3) Download [Convbank data](https://gitlab.com/ucdavisnlp/dialog-parsing/-/tree/master/dep_parsed)

### Training parsers

```scripts/1.graph_train.sh```

(1) Install [Diaparser](https://github.com/Unipisa/diaparser) AND `git clone` its repository

(2) Start training; see `misc/train_cmd.sh` for an example of training a parser with UD-Atis 

```sh
$ python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-Atis/en_atis-ud-train.conllu \
    --dev  ud_data/UD_English-Atis/en_atis-ud-dev.conllu \
    --test ud_data/UD_English-Atis/en_atis-ud-test.conllu \
    -b -d 0  \
    -p models/graph/UD_English-Atis.bert-cased/model  \
    -f bert  \
    --batch-size 2000  \
    --bert bert-base-cased
```

### TO DO: add training commands for training all out-of-domain parsers

### TO DO: add trained models for out-of-domain parsers

### Acquire parser predictions

```scripts/2.graph_predict.py```

To run:

```python3 scripts/2.graph_predct.py --input ud_data/```

### Evaluation ###

```scripts/3.graph_evaluate.py```

To run:

```python3 scripts/3.graph_evaluate.py --input ud_data/```

Micro LAS/UAS + Macro LAS/UAS

## Finetune a pretrained model

(1) Under the `diaparser` git repository, create a `fientune.txt` file; the fine contains one line of text that is the path of the pretrained model. See `misc/finetune.txt` for an example.

(2) replace `diaparser/diaparser/parsers/biaffine_dependency.py` with `misc/biaffine_dependency.py`

(3) Start finetuning; see `misc/finetune_cmd.sh` for an example of finetuning a parser trained on UD-EWT with UD-Atis

```sh
$ python -m diaparser.cmds.biaffine_dependency train --train /data/liuaal/childes_syntax/UD_English-Atis/en_atis-ud-train.conllu \
    --dev  /data/liuaal/childes_syntax/UD_English-Atis/en_atis-ud-dev.conllu \
    --test /data/liuaal/childes_syntax/UD_English-Atis/en_atis-ud-test.conllu \
    -b -d 0  \
    -p exp/en_atis.bert-cased_finetune/model  \
    -f bert  \
    --bert bert-base-cased
```
