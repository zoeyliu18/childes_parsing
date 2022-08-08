### UD_English-EWT

### Bert

!python -m diaparser.cmds.biaffine_dependency train  \
    --train ../UD_data/UD_English-EWT/en_ewt-ud-train.conllu \
    --dev  ../UD_data/UD_English-EWT/en_ewt-ud-dev.conllu \
    --test ../UD_data/UD_English-EWT/en_ewt-ud-test.conllu \
    -b -d 0  \
    -p logs/diaparser.ewt.1.bert-base-cased  \
    -f bert  \
    --bert bert-base-cased  \
    -s 1

!python -m diaparser.cmds.biaffine_dependency train  \
    --train ../UD_data/UD_English-EWT/en_ewt-ud-train.conllu \
    --dev  ../UD_data/UD_English-EWT/en_ewt-ud-dev.conllu \
    --test ../UD_data/UD_English-EWT/en_ewt-ud-test.conllu \
    -b -d 0  \
    -p logs/diaparser.ewt.2.bert-base-cased  \
    -f bert  \
    --bert bert-base-cased  \
    -s 2

!python -m diaparser.cmds.biaffine_dependency train  \
    --train ../UD_data/UD_English-EWT/en_ewt-ud-train.conllu \
    --dev  ../UD_data/UD_English-EWT/en_ewt-ud-dev.conllu \
    --test ../UD_data/UD_English-EWT/en_ewt-ud-test.conllu \
    -b -d 0  \
    -p logs/diaparser.ewt.3.bert-base-cased  \
    -f bert  \
    --bert bert-base-cased  \
    -s 3

### Roberta

!python -m diaparser.cmds.biaffine_dependency train  \
    --train ../UD_data/UD_English-EWT/en_ewt-ud-train.conllu \
    --dev  ../UD_data/UD_English-EWT/en_ewt-ud-dev.conllu \
    --test ../UD_data/UD_English-EWT/en_ewt-ud-test.conllu \
    -b -d 0  \
    -p logs/diaparser.ewt.1.roberta-base  \
    -f bert  \
    --bert roberta-base  \
    -s 1

!python -m diaparser.cmds.biaffine_dependency train  \
    --train ../UD_data/UD_English-EWT/en_ewt-ud-train.conllu \
    --dev  ../UD_data/UD_English-EWT/en_ewt-ud-dev.conllu \
    --test ../UD_data/UD_English-EWT/en_ewt-ud-test.conllu \
    -b -d 0  \
    -p logs/diaparser.ewt.2.roberta-base  \
    -f bert  \
    --bert roberta-base  \
    -s 2

!python -m diaparser.cmds.biaffine_dependency train  \
    --train ../UD_data/UD_English-EWT/en_ewt-ud-train.conllu \
    --dev  ../UD_data/UD_English-EWT/en_ewt-ud-dev.conllu \
    --test ../UD_data/UD_English-EWT/en_ewt-ud-test.conllu \
    -b -d 0  \
    -p logs/diaparser.ewt.3.roberta-base  \
    -f bert  \
    --bert roberta-base  \
    -s 3

# Twitter-roberta

!python -m diaparser.cmds.biaffine_dependency train  \
    --train ../UD_data/UD_English-EWT/en_ewt-ud-train.conllu \
    --dev  ../UD_data/UD_English-EWT/en_ewt-ud-dev.conllu \
    --test ../UD_data/UD_English-EWT/en_ewt-ud-test.conllu \
    -b -d 0  \
    -p logs/diaparser.ewt.1.cardiffnlp-twitter-roberta-base  \
    -f bert  \
    --bert cardiffnlp/twitter-roberta-base  \
    -s 1

!python -m diaparser.cmds.biaffine_dependency train  \
    --train ../UD_data/UD_English-EWT/en_ewt-ud-train.conllu \
    --dev  ../UD_data/UD_English-EWT/en_ewt-ud-dev.conllu \
    --test ../UD_data/UD_English-EWT/en_ewt-ud-test.conllu \
    -b -d 0  \
    -p logs/diaparser.ewt.2.cardiffnlp-twitter-roberta-base  \
    -f bert  \
    --bert cardiffnlp/twitter-roberta-base  \
    -s 2

!python -m diaparser.cmds.biaffine_dependency train  \
    --train ../UD_data/UD_English-EWT/en_ewt-ud-train.conllu \
    --dev  ../UD_data/UD_English-EWT/en_ewt-ud-dev.conllu \
    --test ../UD_data/UD_English-EWT/en_ewt-ud-test.conllu \
    -b -d 0  \
    -p logs/diaparser.ewt.3.cardiffnlp-twitter-roberta-base  \
    -f bert  \
    --bert cardiffnlp/twitter-roberta-base  \
    -s 3



### UD_English-ESL

### Bert

!python -m diaparser.cmds.biaffine_dependency train  \
    --train ../UD_data/UD_English-ESL/en_esl-ud-train.conllu \
    --dev  ../UD_data/UD_English-ESL/en_esl-ud-dev.conllu \
    --test ../UD_data/UD_English-ESL/en_esl-ud-test.conllu \
    -b -d 0  \
    -p logs/diaparser.esl.1.bert-base-cased  \
    -f bert  \
    --bert bert-base-cased  \
    -s 1

!python -m diaparser.cmds.biaffine_dependency train  \
    --train ../UD_data/UD_English-ESL/en_esl-ud-train.conllu \
    --dev  ../UD_data/UD_English-ESL/en_esl-ud-dev.conllu \
    --test ../UD_data/UD_English-ESL/en_esl-ud-test.conllu \
    -b -d 0  \
    -p logs/diaparser.esl.2.bert-base-cased  \
    -f bert  \
    --bert bert-base-cased  \
    -s 2

!python -m diaparser.cmds.biaffine_dependency train  \
    --train ../UD_data/UD_English-ESL/en_esl-ud-train.conllu \
    --dev  ../UD_data/UD_English-ESL/en_esl-ud-dev.conllu \
    --test ../UD_data/UD_English-ESL/en_esl-ud-test.conllu \
    -b -d 0  \
    -p logs/diaparser.esl.3.bert-base-cased  \
    -f bert  \
    --bert bert-base-cased  \
    -s 3

### Roberta

!python -m diaparser.cmds.biaffine_dependency train  \
    --train ../UD_data/UD_English-ESL/en_esl-ud-train.conllu \
    --dev  ../UD_data/UD_English-ESL/en_esl-ud-dev.conllu \
    --test ../UD_data/UD_English-ESL/en_esl-ud-test.conllu \
    -b -d 0  \
    -p logs/diaparser.esl.1.roberta-base  \
    -f bert  \
    --bert roberta-base  \
    -s 1

!python -m diaparser.cmds.biaffine_dependency train  \
    --train ../UD_data/UD_English-ESL/en_esl-ud-train.conllu \
    --dev  ../UD_data/UD_English-ESL/en_esl-ud-dev.conllu \
    --test ../UD_data/UD_English-ESL/en_esl-ud-test.conllu \
    -b -d 0  \
    -p logs/diaparser.esl.2.roberta-base  \
    -f bert  \
    --bert roberta-base  \
    -s 2

!python -m diaparser.cmds.biaffine_dependency train  \
    --train ../UD_data/UD_English-ESL/en_esl-ud-train.conllu \
    --dev  ../UD_data/UD_English-ESL/en_esl-ud-dev.conllu \
    --test ../UD_data/UD_English-ESL/en_esl-ud-test.conllu \
    -b -d 0  \
    -p logs/diaparser.esl.3.roberta-base  \
    -f bert  \
    --bert roberta-base  \
    -s 3

# Twitter-roberta

!python -m diaparser.cmds.biaffine_dependency train  \
    --train ../UD_data/UD_English-ESL/en_esl-ud-train.conllu \
    --dev  ../UD_data/UD_English-ESL/en_esl-ud-dev.conllu \
    --test ../UD_data/UD_English-ESL/en_esl-ud-test.conllu \
    -b -d 0  \
    -p logs/diaparser.esl.1.cardiffnlp-twitter-roberta-base  \
    -f bert  \
    --bert cardiffnlp/twitter-roberta-base  \
    -s 1

!python -m diaparser.cmds.biaffine_dependency train  \
    --train ../UD_data/UD_English-ESL/en_esl-ud-train.conllu \
    --dev  ../UD_data/UD_English-ESL/en_esl-ud-dev.conllu \
    --test ../UD_data/UD_English-ESL/en_esl-ud-test.conllu \
    -b -d 0  \
    -p logs/diaparser.esl.2.cardiffnlp-twitter-roberta-base  \
    -f bert  \
    --bert cardiffnlp/twitter-roberta-base  \
    -s 2

!python -m diaparser.cmds.biaffine_dependency train  \
    --train ../UD_data/UD_English-ESL/en_esl-ud-train.conllu \
    --dev  ../UD_data/UD_English-ESL/en_esl-ud-dev.conllu \
    --test ../UD_data/UD_English-ESL/en_esl-ud-test.conllu \
    -b -d 0  \
    -p logs/diaparser.esl.3.cardiffnlp-twitter-roberta-base  \
    -f bert  \
    --bert cardiffnlp/twitter-roberta-base  \
    -s 3



### UD_English-Twitter

### Bert

!python -m diaparser.cmds.biaffine_dependency train  \
    --train ../UD_data/UD_English-Twitter/en_twitter-ud-train.conllu \
    --dev  ../UD_data/UD_English-Twitter/en_twitter-ud-dev.conllu \
    --test ../UD_data/UD_English-Twitter/en_twitter-ud-test.conllu \
    -b -d 0  \
    -p logs/diaparser.twitter.1.bert-base-cased  \
    -f bert  \
    --bert bert-base-cased  \
    -s 1

!python -m diaparser.cmds.biaffine_dependency train  \
    --train ../UD_data/UD_English-Twitter/en_twitter-ud-train.conllu \
    --dev  ../UD_data/UD_English-Twitter/en_twitter-ud-dev.conllu \
    --test ../UD_data/UD_English-Twitter/en_twitter-ud-test.conllu \
    -b -d 0  \
    -p logs/diaparser.twitter.2.bert-base-cased  \
    -f bert  \
    --bert bert-base-cased  \
    -s 2

!python -m diaparser.cmds.biaffine_dependency train  \
    --train ../UD_data/UD_English-Twitter/en_twitter-ud-train.conllu \
    --dev  ../UD_data/UD_English-Twitter/en_twitter-ud-dev.conllu \
    --test ../UD_data/UD_English-Twitter/en_twitter-ud-test.conllu \
    -b -d 0  \
    -p logs/diaparser.twitter.3.bert-base-cased  \
    -f bert  \
    --bert bert-base-cased  \
    -s 3

### Roberta

!python -m diaparser.cmds.biaffine_dependency train  \
    --train ../UD_data/UD_English-Twitter/en_twitter-ud-train.conllu \
    --dev  ../UD_data/UD_English-Twitter/en_twitter-ud-dev.conllu \
    --test ../UD_data/UD_English-Twitter/en_twitter-ud-test.conllu \
    -b -d 0  \
    -p logs/diaparser.twitter.1.roberta-base  \
    -f bert  \
    --bert roberta-base  \
    -s 1

!python -m diaparser.cmds.biaffine_dependency train  \
    --train ../UD_data/UD_English-Twitter/en_twitter-ud-train.conllu \
    --dev  ../UD_data/UD_English-Twitter/en_twitter-ud-dev.conllu \
    --test ../UD_data/UD_English-Twitter/en_twitter-ud-test.conllu \
    -b -d 0  \
    -p logs/diaparser.twitter.2.roberta-base  \
    -f bert  \
    --bert roberta-base  \
    -s 2

!python -m diaparser.cmds.biaffine_dependency train  \
    --train ../UD_data/UD_English-Twitter/en_twitter-ud-train.conllu \
    --dev  ../UD_data/UD_English-Twitter/en_twitter-ud-dev.conllu \
    --test ../UD_data/UD_English-Twitter/en_twitter-ud-test.conllu \
    -b -d 0  \
    -p logs/diaparser.twitter.3.roberta-base  \
    -f bert  \
    --bert roberta-base  \
    -s 3

# Twitter-roberta

!python -m diaparser.cmds.biaffine_dependency train  \
    --train ../UD_data/UD_English-Twitter/en_twitter-ud-train.conllu \
    --dev  ../UD_data/UD_English-Twitter/en_twitter-ud-dev.conllu \
    --test ../UD_data/UD_English-Twitter/en_twitter-ud-test.conllu \
    -b -d 0  \
    -p logs/diaparser.twitter.1.cardiffnlp-twitter-roberta-base  \
    -f bert  \
    --bert cardiffnlp/twitter-roberta-base  \
    -s 1

!python -m diaparser.cmds.biaffine_dependency train  \
    --train ../UD_data/UD_English-Twitter/en_twitter-ud-train.conllu \
    --dev  ../UD_data/UD_English-Twitter/en_twitter-ud-dev.conllu \
    --test ../UD_data/UD_English-Twitter/en_twitter-ud-test.conllu \
    -b -d 0  \
    -p logs/diaparser.twitter.2.cardiffnlp-twitter-roberta-base  \
    -f bert  \
    --bert cardiffnlp/twitter-roberta-base  \
    -s 2

!python -m diaparser.cmds.biaffine_dependency train  \
    --train ../UD_data/UD_English-Twitter/en_twitter-ud-train.conllu \
    --dev  ../UD_data/UD_English-Twitter/en_twitter-ud-dev.conllu \
    --test ../UD_data/UD_English-Twitter/en_twitter-ud-test.conllu \
    -b -d 0  \
    -p logs/diaparser.twitter.3.cardiffnlp-twitter-roberta-base  \
    -f bert  \
    --bert cardiffnlp/twitter-roberta-base  \
    -s 3

