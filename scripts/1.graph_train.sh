### UD_English-EWT

mkdir models
mkdir models/graph1
mkdir models/graph2
mkdir models/graph3

mkdir models/graph1/UD_English-EWT
mkdir models/graph1/UD_English-GUMReddit
mkdir models/graph1/UD_English-Atis
mkdir models/graph1/UD_English-Tweebank2

mkdir models/graph2/UD_English-EWT
mkdir models/graph2/UD_English-GUMReddit
mkdir models/graph2/UD_English-Atis
mkdir models/graph2/UD_English-Tweebank2

mkdir models/graph3/UD_English-EWT
mkdir models/graph3/UD_English-GUMReddit
mkdir models/graph3/UD_English-Atis
mkdir models/graph3/UD_English-Tweebank2

### Bert
python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-EWT/en_ewt-ud-train.conllu \
    --dev  ud_data/UD_English-EWT/en_ewt-ud-dev.conllu \
    --test ud_data/UD_English-EWT/en_ewt-ud-test.conllu \
    -b -d 0  \
    -p models/graph1/UD_English-EWT/bert-cased/model  \
    -f bert  \
    --batch-size 2000  \
    --bert bert-base-cased  \
    -s 1

python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-EWT/en_ewt-ud-train.conllu \
    --dev  ud_data/UD_English-EWT/en_ewt-ud-dev.conllu \
    --test ud_data/UD_English-EWT/en_ewt-ud-test.conllu \
    -b -d 0  \
    -p models/graph2/UD_English-EWT/bert-cased/model  \
    -f bert  \
    --batch-size 2000  \
    --bert bert-base-cased  \
    -s 2

python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-EWT/en_ewt-ud-train.conllu \
    --dev  ud_data/UD_English-EWT/en_ewt-ud-dev.conllu \
    --test ud_data/UD_English-EWT/en_ewt-ud-test.conllu \
    -b -d 0  \
    -p models/graph3/UD_English-EWT/bert-cased/model  \
    -f bert  \
    --batch-size 2000  \
    --bert bert-base-cased  \
    -s 3

### Roberta
python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-EWT/en_ewt-ud-train.conllu \
    --dev  ud_data/UD_English-EWT/en_ewt-ud-dev.conllu \
    --test ud_data/UD_English-EWT/en_ewt-ud-test.conllu \
    -b -d 0  \
    -p models/graph1/UD_English-EWT/roberta-large/model  \
    -f bert  \
    --batch-size 2000  \
    --bert roberta-large  \
    -s 1

python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-EWT/en_ewt-ud-train.conllu \
    --dev  ud_data/UD_English-EWT/en_ewt-ud-dev.conllu \
    --test ud_data/UD_English-EWT/en_ewt-ud-test.conllu \
    -b -d 0  \
    -p models/graph2/UD_English-EWT/roberta-large/model  \
    -f bert  \
    --batch-size 2000  \
    --bert roberta-large  \
    -s 2

python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-EWT/en_ewt-ud-train.conllu \
    --dev  ud_data/UD_English-EWT/en_ewt-ud-dev.conllu \
    --test ud_data/UD_English-EWT/en_ewt-ud-test.conllu \
    -b -d 0  \
    -p models/graph3/UD_English-EWT/roberta-large/model  \
    -f bert  \
    --batch-size 2000  \
    --bert roberta-large  \
    -s 3

### Rembert
python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-EWT/en_ewt-ud-train.conllu \
    --dev  ud_data/UD_English-EWT/en_ewt-ud-dev.conllu \
    --test ud_data/UD_English-EWT/en_ewt-ud-test.conllu \
    -b -d 0  \
    -p models/graph1/UD_English-EWT/rembert/model  \
    -f bert  \
    --batch-size 2000  \
    --bert rembert  \
    -s 1

python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-EWT/en_ewt-ud-train.conllu \
    --dev  ud_data/UD_English-EWT/en_ewt-ud-dev.conllu \
    --test ud_data/UD_English-EWT/en_ewt-ud-test.conllu \
    -b -d 0  \
    -p models/graph2/UD_English-EWT/rembert/model  \
    -f bert  \
    --batch-size 2000  \
    --bert rembert  \
    -s 2

python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-EWT/en_ewt-ud-train.conllu \
    --dev  ud_data/UD_English-EWT/en_ewt-ud-dev.conllu \
    --test ud_data/UD_English-EWT/en_ewt-ud-test.conllu \
    -b -d 0  \
    -p models/graph3/UD_English-EWT/rembert/model  \
    -f bert  \
    --batch-size 2000  \
    --bert rembert  \
    -s 3

### UD_English-GUMReddit

### Bert
python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-GUMReddit/en_gumreddit-ud-train.conllu \
    --dev  ud_data/UD_English-GUMReddit/en_gumreddit-ud-dev.conllu \
    --test ud_data/UD_English-GUMReddit/en_gumreddit-ud-test.conllu \
    -b -d 0  \
    -p models/graph1/UD_English-GUMReddit/bert-cased/model  \
    -f bert  \
    --batch-size 2000  \
    --bert bert-base-cased  \
    -s 1

python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-GUMReddit/en_gumreddit-ud-train.conllu \
    --dev  ud_data/UD_English-GUMReddit/en_gumreddit-ud-dev.conllu \
    --test ud_data/UD_English-GUMReddit/en_gumreddit-ud-test.conllu \
    -b -d 0  \
    -p models/graph2/UD_English-GUMReddit/bert-cased/model  \
    -f bert  \
    --batch-size 2000  \
    --bert bert-base-cased  \
    -s 2

python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-GUMReddit/en_gumreddit-ud-train.conllu \
    --dev  ud_data/UD_English-GUMReddit/en_gumreddit-ud-dev.conllu \
    --test ud_data/UD_English-GUMReddit/en_gumreddit-ud-test.conllu \
    -b -d 0  \
    -p models/graph3/UD_English-GUMReddit/bert-cased/model  \
    -f bert  \
    --batch-size 2000  \
    --bert bert-base-cased  \
    -s 3


### Roberta
python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-GUMReddit/en_gumreddit-ud-train.conllu \
    --dev  ud_data/UD_English-GUMReddit/en_gumreddit-ud-dev.conllu \
    --test ud_data/UD_English-GUMReddit/en_gumreddit-ud-test.conllu \
    -b -d 0  \
    -p models/graph1/UD_English-GUMReddit/roberta-large/model  \
    -f bert  \
    --batch-size 2000  \
    --bert roberta-large  \
    -s 1

python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-GUMReddit/en_gumreddit-ud-train.conllu \
    --dev  ud_data/UD_English-GUMReddit/en_gumreddit-ud-dev.conllu \
    --test ud_data/UD_English-GUMReddit/en_gumreddit-ud-test.conllu \
    -b -d 0  \
    -p models/graph2/UD_English-GUMReddit/roberta-large/model  \
    -f bert  \
    --batch-size 2000  \
    --bert roberta-large  \
    -s 2

python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-GUMReddit/en_gumreddit-ud-train.conllu \
    --dev  ud_data/UD_English-GUMReddit/en_gumreddit-ud-dev.conllu \
    --test ud_data/UD_English-GUMReddit/en_gumreddit-ud-test.conllu \
    -b -d 0  \
    -p models/graph3/UD_English-GUMReddit/roberta-large/model  \
    -f bert  \
    --batch-size 2000  \
    --bert roberta-large  \
    -s 3

### Rembert
python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-GUMReddit/en_gumreddit-ud-train.conllu \
    --dev  ud_data/UD_English-GUMReddit/en_gumreddit-ud-dev.conllu \
    --test ud_data/UD_English-GUMReddit/en_gumreddit-ud-test.conllu \
    -b -d 0  \
    -p models/graph1/UD_English-GUMReddit/rembert/model  \
    -f bert  \
    --batch-size 2000  \
    --bert rembert  \
    -s 1

python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-GUMReddit/en_gumreddit-ud-train.conllu \
    --dev  ud_data/UD_English-GUMReddit/en_gumreddit-ud-dev.conllu \
    --test ud_data/UD_English-GUMReddit/en_gumreddit-ud-test.conllu \
    -b -d 0  \
    -p models/graph2/UD_English-GUMReddit/rembert/model  \
    -f bert  \
    --batch-size 2000  \
    --bert rembert  \
    -s 2

python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-GUMReddit/en_gumreddit-ud-train.conllu \
    --dev  ud_data/UD_English-GUMReddit/en_gumreddit-ud-dev.conllu \
    --test ud_data/UD_English-GUMReddit/en_gumreddit-ud-test.conllu \
    -b -d 0  \
    -p models/graph3/UD_English-GUMReddit/rembert/model  \
    -f bert  \
    --batch-size 2000  \
    --bert rembert  \
    -s 3


### UD_English-Atis

### Bert
python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-Atis/en_atis-ud-train.conllu \
    --dev  ud_data/UD_English-Atis/en_atis-ud-dev.conllu \
    --test ud_data/UD_English-Atis/en_atis-ud-test.conllu \
    -b -d 0  \
    -p models/graph1/UD_English-Atis/bert-cased/model  \
    -f bert  \
    --batch-size 2000  \
    --bert bert-base-cased  \
    -s 1

python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-Atis/en_atis-ud-train.conllu \
    --dev  ud_data/UD_English-Atis/en_atis-ud-dev.conllu \
    --test ud_data/UD_English-Atis/en_atis-ud-test.conllu \
    -b -d 0  \
    -p models/graph2/UD_English-Atis/bert-cased/model  \
    -f bert  \
    --batch-size 2000  \
    --bert bert-base-cased  \
    -s 2

python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-Atis/en_atis-ud-train.conllu \
    --dev  ud_data/UD_English-Atis/en_atis-ud-dev.conllu \
    --test ud_data/UD_English-Atis/en_atis-ud-test.conllu \
    -b -d 0  \
    -p models/graph3/UD_English-Atis/bert-cased/model  \
    -f bert  \
    --batch-size 2000  \
    --bert bert-base-cased  \
    -s 3

### Roberta
python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-Atis/en_atis-ud-train.conllu \
    --dev  ud_data/UD_English-Atis/en_atis-ud-dev.conllu \
    --test ud_data/UD_English-Atis/en_atis-ud-test.conllu \
    -b -d 0  \
    -p models/graph1/UD_English-Atis/roberta-large/model  \
    -f bert  \
    --batch-size 2000  \
    --bert roberta-large  \
    -s 1

python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-Atis/en_atis-ud-train.conllu \
    --dev  ud_data/UD_English-Atis/en_atis-ud-dev.conllu \
    --test ud_data/UD_English-Atis/en_atis-ud-test.conllu \
    -b -d 0  \
    -p models/graph2/UD_English-Atis/roberta-large/model  \
    -f bert  \
    --batch-size 2000  \
    --bert roberta-large  \
    -s 2

python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-Atis/en_atis-ud-train.conllu \
    --dev  ud_data/UD_English-Atis/en_atis-ud-dev.conllu \
    --test ud_data/UD_English-Atis/en_atis-ud-test.conllu \
    -b -d 0  \
    -p models/graph3/UD_English-Atis/roberta-large/model  \
    -f bert  \
    --batch-size 2000  \
    --bert roberta-large  \
    -s 3

### Rembert
python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-Atis/en_atis-ud-train.conllu \
    --dev  ud_data/UD_English-Atis/en_atis-ud-dev.conllu \
    --test ud_data/UD_English-Atis/en_atis-ud-test.conllu \
    -b -d 0  \
    -p models/graph1/UD_English-Atis/rembert/model  \
    -f bert  \
    --batch-size 2000  \
    --bert rembert  \
    -s 1

python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-Atis/en_atis-ud-train.conllu \
    --dev  ud_data/UD_English-Atis/en_atis-ud-dev.conllu \
    --test ud_data/UD_English-Atis/en_atis-ud-test.conllu \
    -b -d 0  \
    -p models/graph2/UD_English-Atis/rembert/model  \
    -f bert  \
    --batch-size 2000  \
    --bert rembert  \
    -s 2

python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-Atis/en_atis-ud-train.conllu \
    --dev  ud_data/UD_English-Atis/en_atis-ud-dev.conllu \
    --test ud_data/UD_English-Atis/en_atis-ud-test.conllu \
    -b -d 0  \
    -p models/graph3/UD_English-Atis/rembert/model  \
    -f bert  \
    --batch-size 2000  \
    --bert rembert  \
    -s 3

### UD_English-Tweebank2

### Bert
python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-Tweebank2/en-ud-tweet-train.conllu \
    --dev  ud_data/UD_English-Tweebank2/en-ud-tweet-dev.conllu \
    --test ud_data/UD_English-Tweebank2/en-ud-tweet-test.conllu \
    -b -d 0  \
    -p models/graph1/UD_English-Tweebank2/bert-cased/model  \
    -f bert  \
    --batch-size 2000  \
    --bert bert-base-cased  \
    -s 1

python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-Tweebank2/en-ud-tweet-train.conllu \
    --dev  ud_data/UD_English-Tweebank2/en-ud-tweet-dev.conllu \
    --test ud_data/UD_English-Tweebank2/en-ud-tweet-test.conllu \
    -b -d 0  \
    -p models/graph2/UD_English-Tweebank2/bert-cased/model  \
    -f bert  \
    --batch-size 2000  \
    --bert bert-base-cased  \
    -s 2

python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-Tweebank2/en-ud-tweet-train.conllu \
    --dev  ud_data/UD_English-Tweebank2/en-ud-tweet-dev.conllu \
    --test ud_data/UD_English-Tweebank2/en-ud-tweet-test.conllu \
    -b -d 0  \
    -p models/graph3/UD_English-Tweebank2/bert-cased/model  \
    -f bert  \
    --batch-size 2000  \
    --bert bert-base-cased  \
    -s 3

### Roberta
python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-Tweebank2/en-ud-tweet-train.conllu \
    --dev  ud_data/UD_English-Tweebank2/en-ud-tweet-dev.conllu \
    --test ud_data/UD_English-Tweebank2/en-ud-tweet-test.conllu \
    -b -d 0  \
    -p models/graph1/UD_English-Tweebank2/roberta-large/model  \
    -f bert  \
    --batch-size 2000  \
    --bert roberta-large  \
    -s 1

python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-Tweebank2/en-ud-tweet-train.conllu \
    --dev  ud_data/UD_English-Tweebank2/en-ud-tweet-dev.conllu \
    --test ud_data/UD_English-Tweebank2/en-ud-tweet-test.conllu \
    -b -d 0  \
    -p models/graph2/UD_English-Tweebank2/roberta-large/model  \
    -f bert  \
    --batch-size 2000  \
    --bert roberta-large  \
    -s 2

python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-Tweebank2/en-ud-tweet-train.conllu \
    --dev  ud_data/UD_English-Tweebank2/en-ud-tweet-dev.conllu \
    --test ud_data/UD_English-Tweebank2/en-ud-tweet-test.conllu \
    -b -d 0  \
    -p models/graph3/UD_English-Tweebank2/roberta-large/model  \
    -f bert  \
    --batch-size 2000  \
    --bert roberta-large  \
    -s 3

### Rembert
python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-Tweebank2/en-ud-tweet-train.conllu \
    --dev  ud_data/UD_English-Tweebank2/en-ud-tweet-dev.conllu \
    --test ud_data/UD_English-Tweebank2/en-ud-tweet-test.conllu \
    -b -d 0  \
    -p models/graph1/UD_English-Tweebank2/rembert/model  \
    -f bert  \
    --batch-size 2000  \
    --bert rembert  \
    -s 1

python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-Tweebank2/en-ud-tweet-train.conllu \
    --dev  ud_data/UD_English-Tweebank2/en-ud-tweet-dev.conllu \
    --test ud_data/UD_English-Tweebank2/en-ud-tweet-test.conllu \
    -b -d 0  \
    -p models/graph2/UD_English-Tweebank2/rembert/model  \
    -f bert  \
    --batch-size 2000  \
    --bert rembert  \
    -s 2

python -m diaparser.cmds.biaffine_dependency train --train ud_data/UD_English-Tweebank2/en-ud-tweet-train.conllu \
    --dev  ud_data/UD_English-Tweebank2/en-ud-tweet-dev.conllu \
    --test ud_data/UD_English-Tweebank2/en-ud-tweet-test.conllu \
    -b -d 0  \
    -p models/graph3/UD_English-Tweebank2/rembert/model  \
    -f bert  \
    --batch-size 2000  \
    --bert rembert  \
    -s 3
