### UD_English-EWT

!uuparser --outdir uuparser/logs/1/ --datadir UD_data --include "en_ewt" --dynet-seed 1 --dynet-mem 10000

!uuparser --predict --modeldir uuparser/logs/1/ --outdir uuparser/predict/1/ --datadir UD_data --include "en_ewt" 

!uuparser --outdir uuparser/logs/2/ --datadir UD_data --include "en_ewt" --dynet-seed 2 --dynet-mem 10000

!uuparser --predict --modeldir uuparser/logs/2/ --outdir uuparser/predict/2/ --datadir UD_data --include "en_ewt" 

!uuparser --outdir uuparser/logs/3/ --datadir UD_data --include "en_ewt" --dynet-seed 3 --dynet-mem 10000

!uuparser --predict --modeldir uuparser/logs/3/ --outdir uuparser/predict/3/ --datadir UD_data --include "en_ewt" 


### UD_English-ESL

!uuparser --outdir uuparser/logs/1/ --datadir UD_data --include "en_esl" --dynet-seed 1 --dynet-mem 10000

!uuparser --predict --modeldir uuparser/logs/1/ --outdir uuparser/predict/1/ --datadir UD_data --include "en_esl" 

!uuparser --outdir uuparser/logs/2/ --datadir UD_data --include "en_esl" --dynet-seed 2 --dynet-mem 10000

!uuparser --predict --modeldir uuparser/logs/2/ --outdir uuparser/predict/2/ --datadir UD_data --include "en_esl" 

!uuparser --outdir uuparser/logs/3/ --datadir UD_data --include "en_esl" --dynet-seed 3 --dynet-mem 10000

!uuparser --predict --modeldir uuparser/logs/3/ --outdir uuparser/predict/3/ --datadir UD_data --include "en_esl" 


### UD_English-Twitter

!uuparser --outdir uuparser/logs/1/ --datadir UD_data --include "en_twitter" --dynet-seed 1 --dynet-mem 10000

!uuparser --predict --modeldir uuparser/logs/1/ --outdir uuparser/predict/1/ --datadir UD_data --include "en_twitter" 

!uuparser --outdir uuparser/logs/2/ --datadir UD_data --include "en_twitter" --dynet-seed 2 --dynet-mem 10000

!uuparser --predict --modeldir uuparser/logs/2/ --outdir uuparser/predict/2/ --datadir UD_data --include "en_twitter" 

!uuparser --outdir uuparser/logs/3/ --datadir UD_data --include "en_twitter" --dynet-seed 3 --dynet-mem 10000

!uuparser --predict --modeldir uuparser/logs/3/ --outdir uuparser/predict/3/ --datadir UD_data --include "en_twitter" 

