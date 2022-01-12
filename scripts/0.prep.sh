TREEBANKS="UD_English-EWT UD_English-GUMReddit UD_English-Atis "

# Download data:
wget https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11234/1-4611/ud-treebanks-v2.9.tgz
tar -zxvf ud-treebanks-v2.9.tgz
mkdir -p data
for TREEBANK in $TREEBANKS
do
    cp -r ud-treebanks-v2.9/$TREEBANK ud_data/
done
rm -rf ud-treebanks-v2.9*

# Get special treebanks (not fully available in official UD
git clone https://github.com/Oneplus/Tweebank.git
cp -r Tweebank/converted ud_data/UD_English-Tweebank2
rm -rf Tweebank

# Get ConvBank data

git clone https://gitlab.com/ucdavisnlp/dialog-parsing
cp -r dialog-parsing/dep_parsed ud_data/dep_parsed

#python3 scripts/misc/cleanconl.py ../data/*/*conllu
#cd ..
