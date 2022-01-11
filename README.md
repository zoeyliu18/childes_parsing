# child_syntax: Child and Parent speech annotated with adaptations of the Universal Dependencies framework

## Train graph-based parser based on out-of-domain UD-style data

### Data preparation

#### From [Universal Dependencies](https://universaldependencies.org/), download the following treebanks

(1) UD-EWT

(2) UD-GUM

(3) UD-GUM reddit (then build the reddit corpus following [instructions](https://github.com/amir-zeldes/gum/blob/master/README_reddit.md)

(4) UD-Atis

#### Download [Convbank data](https://gitlab.com/ucdavisnlp/dialog-parsing/-/tree/master/dep_parsed)

#### Download Tweeter data?

### Training parsers

#### Install [Diaparser](https://github.com/Unipisa/diaparser) AND `git clone` its repository

## Finetune a pretrained model

(1) Under the `diaparser` git repository, create a `fientune.txt` file; the fine contains one line of text that is the path of the pretrained model. See `misc/finetune.txt` for an example.

(2) replace `diaparser/diaparser/parsers/biaffine_dependency.py` with `misc/biaffine_dependency.py`

(3) run via commaind line:

`python -m diaparser.cmds.biaffine_dependency train --train /data/liuaal/childes_syntax/UD_English-GUMReddit/en_gumreddit-ud-train.conllu \

    --dev  /data/liuaal/childes_syntax/UD_English-GUMReddit/en_gumreddit-ud-dev.conllu \
    
    --test /data/liuaal/childes_syntax/UD_English-GUMReddit/en_gumreddit-ud-test.conllu \
    
    -b -d 0  \
    
    -p exp/reddit_finetune/model  \
    
    -f bert  \
    
    --bert bert-base-cased`
