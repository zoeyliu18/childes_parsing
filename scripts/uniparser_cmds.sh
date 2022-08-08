### UD_English-EWT

!python3 run_pytorch_kiperwasser.py --train ../UD_data/UD_English-EWT/en_ewt-ud-train.conllu --dev ../UD_data/UD_English-EWT/en_ewt-ud-dev.conllu --test ../UD_data/UD_English-EWT/en_ewt-ud-test.conllu --seed 1 --model logs/en_ewt.1 --decoder eisner

!python3 run_pytorch_kiperwasser.py --train ../UD_data/UD_English-EWT/en_ewt-ud-train.conllu --dev ../UD_data/UD_English-EWT/en_ewt-ud-dev.conllu --test ../UD_data/UD_English-EWT/en_ewt-ud-test.conllu --seed 2 --model logs/en_ewt.2 --decoder eisner

!python3 run_pytorch_kiperwasser.py --train ../UD_data/UD_English-EWT/en_ewt-ud-train.conllu --dev ../UD_data/UD_English-EWT/en_ewt-ud-dev.conllu --test ../UD_data/UD_English-EWT/en_ewt-ud-test.conllu --seed 3 --model logs/en_ewt.3 --decoder eisner

### UD_English-ESL

!python3 run_pytorch_kiperwasser.py --train ../UD_data/UD_English-ESL/en_esl-ud-train.conllu --dev ../UD_data/UD_English-ESL/en_esl-ud-dev.conllu --test ../UD_data/UD_English-ESL/en_esl-ud-test.conllu --seed 1 --model logs/en_esl.1 --decoder eisner

!python3 run_pytorch_kiperwasser.py --train ../UD_data/UD_English-ESL/en_esl-ud-train.conllu --dev ../UD_data/UD_English-ESL/en_esl-ud-dev.conllu --test ../UD_data/UD_English-ESL/en_esl-ud-test.conllu --seed 2 --model logs/en_esl.2 --decoder eisner

!python3 run_pytorch_kiperwasser.py --train ../UD_data/UD_English-ESL/en_esl-ud-train.conllu --dev ../UD_data/UD_English-ESL/en_esl-ud-dev.conllu --test ../UD_data/UD_English-ESL/en_esl-ud-test.conllu --seed 3 --model logs/en_esl.3 --decoder eisner

### UD_English-Twitter

!python3 run_pytorch_kiperwasser.py --train ../UD_data/UD_English-Twitter/en_twitter-ud-train.conllu --dev ../UD_data/UD_English-Twitter/en_twitter-ud-dev.conllu --test ../UD_data/UD_English-Twitter/en_twitter-ud-test.conllu --seed 1 --model logs/en_twitter.1 --decoder eisner

!python3 run_pytorch_kiperwasser.py --train ../UD_data/UD_English-Twitter/en_twitter-ud-train.conllu --dev ../UD_data/UD_English-Twitter/en_twitter-ud-dev.conllu --test ../UD_data/UD_English-Twitter/en_twitter-ud-test.conllu --seed 2 --model logs/en_twitter.2 --decoder eisner

!python3 run_pytorch_kiperwasser.py --train ../UD_data/UD_English-Twitter/en_twitter-ud-train.conllu --dev ../UD_data/UD_English-Twitter/en_twitter-ud-dev.conllu --test ../UD_data/UD_English-Twitter/en_twitter-ud-test.conllu --seed 3 --model logs/en_twitter.3 --decoder eisner