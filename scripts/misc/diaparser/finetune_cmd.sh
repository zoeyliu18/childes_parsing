python -m diaparser.cmds.biaffine_dependency train --train /data/liuaal/childes_syntax/UD_English-Atis/en_atis-ud-train.conllu \
    --dev  /data/liuaal/childes_syntax/UD_English-Atis/en_atis-ud-dev.conllu \
    --test /data/liuaal/childes_syntax/UD_English-Atis/en_atis-ud-test.conllu \
    -b -d 0  \
    -p exp/en_atis.bert-cased_finetune/model  \
    -f bert  \
    --bert bert-base-cased


