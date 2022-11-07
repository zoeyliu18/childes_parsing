library(ggplot2)
library(dplyr)
library(wesanderson)
library(lme4)

data <- read.csv('results/childes_machamp_eval.txt', header = T, sep = '\t', row.names = NULL)
#colnames(data) <- colnames(data)[2:ncol(data)]
data$Treebank[data$Treebank == 'ewt'] = 'EWT'
data$Treebank[data$Treebank == 'esl'] = 'ESL'
data$Treebank[data$Treebank == 'twitter'] = 'Tweebank'
data$Treebank <- factor(data$Treebank, levels = c('EWT', 'Tweebank', 'ESL'))

data$Embedding[data$Embedding == 'bert-base-cased'] = 'bert'
data$Embedding[data$Embedding == 'roberta-base'] = 'roberta'
data$Embedding[data$Embedding == 'cardiffnlp-twitter-roberta-base'] = 'twitter'
data$Embedding <- factor(data$Embedding, levels = c('bert', 'roberta', 'twitter'))

adam_ewt_machamp = subset(data, Child == 'Adam' & Treebank == 'ewt')

adam_ewt_machamp %>% 
  ggplot(aes(Age, as.numeric(Micro_LAS), group = Embedding, color = Embedding)) +
  geom_line(aes(linetype = Embedding), alpha = 1) +
  #  scale_linetype_manual(values=c("dotted", 'solid', 'dotted', 'solid')) +
  geom_point(aes(color = Embedding, shape = Embedding), size = 1.5) +
  #  scale_shape_manual(values = c(3, 16, 3, 16)) +
#  scale_color_manual(values = c("darkred", "darkgreen", "steelblue",  "mediumpurple4")) +
  scale_y_continuous(breaks=seq(50, 90, 10)) +
  facet_wrap( ~ Role) + #, scales = "free_y") +
  theme_classic() + 
  theme(text = element_text(size=12, family="Times")) + 
  theme(legend.position="top") +
  xlab("child age (months)") + 
  ylab("LAS") + 
  guides(color = guide_legend(nrow = 2))


adam_machamp = subset(data, Child == 'Adam')

subset(adam_machamp, Role == 'parent') %>% 
  ggplot(aes(Age, as.numeric(Micro_LAS), group = Embedding, color = Embedding)) +
  geom_line(aes(linetype = Embedding), alpha = 1) +
  #  scale_linetype_manual(values=c("dotted", 'solid', 'dotted', 'solid')) +
  geom_point(aes(color = Embedding, shape = Embedding), size = 1.5) +
  #  scale_shape_manual(values = c(3, 16, 3, 16)) +
  #  scale_color_manual(values = c("darkred", "darkgreen", "steelblue",  "mediumpurple4")) +
  scale_y_continuous(breaks=seq(50, 90, 10)) +
  facet_wrap( ~ Treebank) + #, scales = "free_y") +
  theme_classic() + 
  theme(text = element_text(size=12, family="Times")) + 
  theme(legend.position="top") +
  xlab("child age (months)") + 
  ylab("LAS") + 
  guides(color = guide_legend(nrow = 2))


average_across_children <- aggregate(Micro_LAS~Role+Treebank+Embedding+Parser+Age, data=data, FUN='mean')

subset(average_across_children, Role == 'parent') %>% 
  ggplot(aes(Age, as.numeric(Micro_LAS), group = Embedding, color = Embedding)) +
  geom_line(aes(linetype = Embedding), alpha = 1) +
  #  scale_linetype_manual(values=c("dotted", 'solid', 'dotted', 'solid')) +
  geom_point(aes(color = Embedding, shape = Embedding), size = 1.5) +
  #  scale_shape_manual(values = c(3, 16, 3, 16)) +
  #  scale_color_manual(values = c("darkred", "darkgreen", "steelblue",  "mediumpurple4")) +
#  scale_y_continuous(breaks=seq(50, 90, 10)) +
  facet_wrap( ~ Treebank) + #, scales = "free_y") +
  theme_classic() + 
  theme(text = element_text(size=18, family="Times")) + 
  theme(legend.position="top") +
  xlab("child age (months)") + 
  ylab("LAS") + 
  guides(color = guide_legend(nrow = 2))


subset(average_across_children, Role == 'child') %>% 
  ggplot(aes(Age, as.numeric(Micro_LAS), group = Embedding, color = Embedding)) +
  geom_line(aes(linetype = Embedding), alpha = 1) +
  #  scale_linetype_manual(values=c("dotted", 'solid', 'dotted', 'solid')) +
  geom_point(aes(color = Embedding, shape = Embedding), size = 1.5) +
  #  scale_shape_manual(values = c(3, 16, 3, 16)) +
  #  scale_color_manual(values = c("darkred", "darkgreen", "steelblue",  "mediumpurple4")) +
  #  scale_y_continuous(breaks=seq(50, 90, 10)) +
  facet_wrap( ~ Treebank) + #, scales = "free_y") +
  theme_classic() + 
  theme(text = element_text(size=12, family="Times")) + 
  theme(legend.position="top") +
  xlab("child age (months)") + 
  ylab("LAS") + 
  guides(color = guide_legend(nrow = 2))


subset(average_across_children, Treebank == 'Tweebank') %>% 
  ggplot(aes(Age, as.numeric(Micro_LAS), group = Embedding, color = Embedding)) +
  geom_line(aes(linetype = Embedding), alpha = 1) +
  #  scale_linetype_manual(values=c("dotted", 'solid', 'dotted', 'solid')) +
  geom_point(aes(color = Embedding, shape = Embedding), size = 1.5) +
  #  scale_shape_manual(values = c(3, 16, 3, 16)) +
  #  scale_color_manual(values = c("darkred", "darkgreen", "steelblue",  "mediumpurple4")) +
    scale_y_continuous(breaks=seq(50, 90, 5)) +
  facet_wrap( ~ Role) +
  theme_classic() + 
  theme(text = element_text(size=25, family="Times")) + 
  theme(legend.position="top") +
  xlab("child age (months)") + 
  ylab("LAS") + 
  guides(color = guide_legend(nrow = 2))


######## Diaparser

diaparser_data <- read.csv('results/childes_diaparser_eval.txt', header = T, sep = '\t', row.names = NULL)
#colnames(diaparser_data) <- colnames(diaparser_data)[2:ncol(diaparser_data)]
diaparser_data$Treebank[diaparser_data$Treebank == 'ewt'] = 'EWT'
diaparser_data$Treebank[diaparser_data$Treebank == 'esl'] = 'ESL'
diaparser_data$Treebank[diaparser_data$Treebank == 'twitter'] = 'Tweebank'
diaparser_data$Treebank <- factor(diaparser_data$Treebank, levels = c('EWT', 'Tweebank', 'ESL'))

diaparser_data$Embedding[diaparser_data$Embedding == 'bert-base-cased'] = 'bert'
diaparser_data$Embedding[diaparser_data$Embedding == 'roberta-base'] = 'roberta'
diaparser_data$Embedding[diaparser_data$Embedding == 'cardiffnlp-twitter-roberta-base'] = 'twitter'
diaparser_data$Embedding <- factor(diaparser_data$Embedding, levels = c('bert', 'roberta', 'twitter'))

diaparser_average_across_children <- aggregate(Micro_LAS~Role+Treebank+Embedding+Parser+Age, data=diaparser_data, FUN='mean')


subset(diaparser_average_across_children, Treebank == 'Tweebank') %>% 
  ggplot(aes(Age, as.numeric(Micro_LAS), group = Embedding, color = Embedding)) +
  geom_line(aes(linetype = Embedding), alpha = 1) +
  #  scale_linetype_manual(values=c("dotted", 'solid', 'dotted', 'solid')) +
  geom_point(aes(color = Embedding, shape = Embedding), size = 1.5) +
  #  scale_shape_manual(values = c(3, 16, 3, 16)) +
  #  scale_color_manual(values = c("darkred", "darkgreen", "steelblue",  "mediumpurple4")) +
    scale_y_continuous(breaks=seq(50, 90, 5)) +
  facet_wrap( ~ Role) + #, scales = "free_y") +
  theme_classic() + 
  theme(text = element_text(size=25, family="Times")) + 
  theme(legend.position="top") +
  xlab("child age (months)") + 
  ylab("LAS") + 
  guides(color = guide_legend(nrow = 2))


######## UUParser

uuparser_data <- read.csv('results/childes_uuparser_eval.txt', header = T, sep = '\t', row.names = NULL)
uuparser_data$Treebank[uuparser_data$Treebank == 'ewt'] = 'EWT'
uuparser_data$Treebank[uuparser_data$Treebank == 'esl'] = 'ESL'
uuparser_data$Treebank[uuparser_data$Treebank == 'twitter'] = 'Tweebank'
uuparser_data$Treebank <- factor(uuparser_data$Treebank, levels = c('EWT', 'Tweebank', 'ESL'))


uuparser_average_across_children <- aggregate(Micro_LAS~Role+Treebank+Age, data=uuparser_data, FUN='mean')


uuparser_average_across_children %>% 
  ggplot(aes(Age, as.numeric(Micro_LAS), group = Role, color = Role)) +
  geom_line(aes(linetype = Role), alpha = 1) +
  #  scale_linetype_manual(values=c("dotted", 'solid', 'dotted', 'solid')) +
  geom_point(aes(color = Role, shape = Role), size = 1.5) +
  #  scale_shape_manual(values = c(3, 16, 3, 16)) +
  #  scale_color_manual(values = c("darkred", "darkgreen", "steelblue",  "mediumpurple4")) +
  #  scale_y_continuous(breaks=seq(50, 90, 10)) +
  facet_wrap( ~ Treebank) + #, scales = "free_y") +
  theme_classic() + 
  theme(text = element_text(size=12, family="Times")) + 
  theme(legend.position="top") +
  xlab("child age (months)") + 
  ylab("LAS") + 
  guides(color = guide_legend(nrow = 2))

subset(uuparser_average_across_children, Treebank == 'Tweebank') %>% 
  ggplot(aes(Age, as.numeric(Micro_LAS), group = 1, color = Role)) +
  geom_line(aes(linetype = Role), alpha = 1) +
  #  scale_linetype_manual(values=c("dotted", 'solid', 'dotted', 'solid')) +
  geom_point(aes(color = Role, shape = Role), size = 1.5) +
  #  scale_shape_manual(values = c(3, 16)) +
    scale_color_manual(values = c("darkgreen",  "mediumpurple4")) +
  #  scale_y_continuous(breaks=seq(50, 90, 10)) +
  facet_wrap( ~ Role) + #, scales = "free_y") +
  theme_classic() + 
  theme(text = element_text(size=25, family="Times")) + 
  theme(legend.position="top") +
  xlab("child age (months)") + 
  ylab("LAS") + 
  guides(color = guide_legend(nrow = 2))

############## In-domain evaluation #############

### By Age ###
indomain_eval <- read.csv('results/childes_indomain_eval_full.txt', header = T, sep = '\t', row.names = NULL)
#colnames(adam_indomain) <- colnames(adam_indomain)[2:ncol(adam_indomain)]

indomain_eval %>% 
  ggplot(aes(Age, as.numeric(Micro_LAS), group = Child, color = Child)) +
  geom_line(aes(linetype = Child), alpha = 1) +
  #  scale_linetype_manual(values=c("dotted", 'solid', 'dotted', 'solid')) +
  geom_point(aes(color = Child, shape = Child), size = 1.5) +
  #  scale_shape_manual(values = c(3, 16, 3, 16)) +
  #  scale_color_manual(values = c("darkred", "darkgreen", "steelblue",  "mediumpurple4")) +
 # scale_y_continuous(breaks=seq(50, 90, 10)) +
  facet_wrap( ~ Role) + #, scales = "free_y") +
  theme_classic() + 
  theme(text = element_text(size=12, family="Times")) + 
  theme(legend.position="top") +
  theme(text = element_text(size=25, family="Times")) +
  xlab("child age (months)") + 
  ylab("LAS")
#+ 
#  guides(color = guide_legend(nrow = 2))


### By Utterance Length ###
ul_indomain_eval <- read.csv('results/childes_indomain_eval_ul.txt', header = T, sep = '\t', row.names = NULL)
#colnames(adam_indomain) <- colnames(adam_indomain)[2:ncol(adam_indomain)]

subset(ul_indomain_eval, Child =='Sarah') %>% 
  ggplot(aes(Sent_len, as.numeric(Micro_LAS), group = Child, color = Child)) +
  geom_line(aes(linetype = Child), alpha = 1) +
  #  scale_linetype_manual(values=c("dotted", 'solid', 'dotted', 'solid')) +
  geom_point(aes(color = Child, shape = Child), size = 1.5) +
  #  scale_shape_manual(values = c(3, 16, 3, 16)) +
  #  scale_color_manual(values = c("darkred", "darkgreen", "steelblue",  "mediumpurple4")) +
  # scale_y_continuous(breaks=seq(50, 90, 10)) +
  facet_wrap( ~ Role) + #, scales = "free_y") +
  theme_classic() + 
  theme(text = element_text(size=12, family="Times")) + 
  theme(legend.position="top") +
  theme(text = element_text(size=25, family="Times")) +
  xlab("utterance length") + 
  ylab("LAS")
#+ 
#  guides(color = guide_legend(nrow = 2))

ggplot(ul_indomain_eval, aes(Sent_len, Micro_LAS, group = Child, color = Child)) + 
  geom_point(aes(color = Child, shape = Child), alpha=.02) +
#  scale_color_manual(values = wes_palette('Zissou1', n = 2)) + #c("darkblue", "blue")) +
  labs(x = "Utterance length") +
  labs(y = 'Micro LAS') +
  geom_smooth(mapping = aes(Sent_len, Micro_LAS), method = 'gam') +
  theme_classic() + 
  facet_wrap(~ Role) +
  theme(legend.position="top") 

############## Regression analysis: Overall #######

regression <- read.csv('results/childes_indomain_regression.txt', header = T, sep = '\t')
regression$UAS_Accuracy <- as.numeric(regression$UAS_Accuracy)
regression$LAS_Accuracy <- as.numeric(regression$LAS_Accuracy)
regression$Age_int <- as.integer(regression$Age)
regression$Age_int <- scale(regression$Age_int)
regression$Size_ratio <- scale(regression$Size_ratio)


model <- lm(LAS_Accuracy ~ Age_int, data = subset(regression, Role == 'child')) ## Age_int 0.001672   0.000113   14.79   <2e-16 ***

model <- lm(LAS_Accuracy ~ Size_ratio *  Age_int * Sent_len * DL, data = subset(regression, Role =='child')) ## Age_int  2.449e-02  1.178e-02   2.078   0.0377 *

model <- lmer(LAS_Accuracy ~ Size_ratio *  Age_int * Sent_len * DL + (Size_ratio | Child), data = subset(regression, Role =='child'&Age_int<=42))

model <- lmer(UAS_Accuracy ~ Size_ratio + Age_int + Sent_len * DL + (Size_ratio + Age_int + Sent_len * DL | Child), data = subset(regression, Role == 'child'))



############## Regression analysis: Effect of dependency length on parsing performance #############

dl_regression <- read.csv('results/childes_indomain_regression_dl.txt', header = T, sep = '\t', row.names = NULL)
dl_regression$UAS_Accuracy <- as.factor(dl_regression$UAS_Accuracy)
dl_regression$LAS_Accuracy <- as.factor(dl_regression$LAS_Accuracy)

dl_model <- lmer(UAS_Accuracy ~ Age + DL + (1 | Child), data = subset(dl_regression, Role == 'child'), family = 'binomial')


###########################


ewt
machamp
cardiffnlp-twitter-roberta-base
parent
18_24
cop 17.07 {'nsubj': 90.91}
nmod:poss 10.8 {'nmod': 98.8}
aux 7.69 {'nsubj': 96.64}
root 6.59 {'parataxis': 8.82, 'compound': 11.76, 'advmod': 8.82, 'discourse': 16.67, 'vocative': 5.88, 'obl': 6.86, 'nsubj': 9.8}
advmod 6.46 {'aux': 67.0, 'case': 5.0, 'compound': 5.0, 'cop': 5.0}
vocative 5.49 {'obj': 14.12, 'nsubj': 28.24, 'root': 30.59, 'discourse': 5.88}
parataxis 5.3 {'ccomp': 13.41, 'xcomp': 6.1, 'root': 28.05, 'aux': 6.1, 'acl': 6.1, 'advcl': 6.1}
obj 5.24 {'discourse': 9.88, 'parataxis': 60.49, 'compound': 6.17}



ewt
machamp
cardiffnlp-twitter-roberta-base
parent
54_60
advmod 15.46 {'aux': 66.99, 'cop': 9.06, 'root': 5.5}
cop 11.36 {'nsubj': 94.27}
nmod:poss 9.3 {'nmod': 98.92}
root 6.65 {'aux': 12.78, 'advmod': 10.53, 'discourse': 12.03, 'ccomp': 5.26, 'nsubj': 12.03, 'compound': 9.02, 'parataxis': 9.77}
aux 6.1 {'nsubj': 91.8}


twitter
machamp
cardiffnlp-twitter-roberta-base
parent
18_24
nmod:poss 13.97 {'nmod': 97.6}
root 10.46 {'parataxis': 5.6, 'acl': 6.4, 'discourse': 13.6, 'nsubj': 36.8, 'vocative': 5.6}
nsubj 7.62 {'vocative': 12.09, 'root': 40.66, 'obj': 8.79, 'det': 8.79, 'discourse': 10.99, 'nmod': 5.49}
parataxis 7.53 {'advmod': 5.56, 'xcomp': 10.0, 'ccomp': 12.22, 'root': 17.78, 'obj': 6.67, 'advcl': 7.78, 'acl': 7.78, 'nsubj': 7.78}
conj 6.61 {'root': 6.33, 'discourse': 45.57, 'advmod': 6.33, 'nummod': 10.13, 'list': 10.13}
compound:prt 5.61 {'compound': 86.57, 'advmod': 8.96}


twitter
machamp
cardiffnlp-twitter-roberta-base
parent
54_60
nmod:poss 11.01 {'nmod': 98.39}
root 10.77 {'discourse': 10.99, 'cop': 7.69, 'aux': 7.14, 'parataxis': 9.89, 'advmod': 10.99, 'nsubj': 21.43}
compound:prt 5.56 {'advmod': 21.28, 'compound': 76.6}
parataxis 5.15 {'aux': 13.79, 'ccomp': 13.79, 'cop': 20.69, 'root': 20.69, 'conj': 5.75}


esl
machamp
cardiffnlp-twitter-roberta-base
parent
18_24
nmod:poss 14.26 {'nmod': 98.2}
parataxis 9.48 {'conj': 6.31, 'ccomp': 15.32, 'root': 18.92, 'xcomp': 6.31, 'advcl': 8.11, 'discourse': 7.21, 'nsubj': 9.01, 'acl': 7.21}
root 9.31 {'advmod': 10.09, 'compound': 12.84, 'discourse': 12.84, 'nsubj': 24.77, 'parataxis': 6.42, 'obl': 7.34}
vocative 6.66 {'obj': 7.69, 'nsubj': 26.92, 'root': 23.08, 'appos': 8.97, 'discourse': 8.97, 'flat': 5.13}
compound:prt 5.72 {'compound': 85.07, 'advmod': 10.45}
nsubj 5.21 {'expl': 6.56, 'obl': 8.2, 'root': 22.95, 'obj': 14.75, 'det': 11.48}
conj 5.04 {'amod': 5.08, 'root': 8.47, 'parataxis': 13.56, 'discourse': 27.12, 'cc': 5.08, 'compound': 8.47, 'advmod': 5.08}




ewt
machamp
cardiffnlp-twitter-roberta-base
parent
24_30
cop 15.9 {'nsubj': 92.71}
nmod:poss 12.04 {'nmod': 97.06}
advmod 9.91 {'aux': 64.94, 'cop': 8.44}
aux 8.79 {'nsubj': 94.51}
root 6.31 {'nsubj': 16.33, 'ccomp': 5.1, 'advmod': 8.67, 'aux': 7.14, 'obl': 5.1, 'compound': 11.22, 'discourse': 12.76}
parataxis 5.99 {'root': 24.73, 'conj': 6.45, 'advcl': 5.38, 'obj': 5.38, 'acl': 6.99, 'aux': 8.6, 'ccomp': 13.44, 'cop': 7.53}


twitter
machamp
cardiffnlp-twitter-roberta-base
parent
24_30
nmod:poss 15.35 {'nmod': 95.99}
root 11.49 {'cop': 7.5, 'advmod': 6.79, 'nsubj': 28.57, 'aux': 5.36, 'parataxis': 6.79, 'discourse': 9.29, 'compound': 6.79}
parataxis 7.39 {'root': 12.78, 'aux': 9.44, 'ccomp': 14.44, 'advcl': 7.78, 'obj': 5.56, 'acl': 5.56, 'nsubj': 5.0, 'cop': 8.89, 'xcomp': 5.0}
nsubj 6.49 {'root': 44.3, 'obj': 17.09, 'det': 6.33, 'discourse': 5.7}
advmod 5.58 {'compound': 31.62, 'root': 16.18, 'obl': 5.88, 'det': 12.5, 'mark': 7.35, 'case': 10.29}
compound:prt 5.46 {'compound': 83.46, 'advmod': 12.03}


esl
machamp
cardiffnlp-twitter-roberta-base
parent
24_30
nmod:poss 15.51 {'nmod': 96.52}
root 11.19 {'advmod': 10.74, 'nsubj': 30.0, 'aux': 5.56, 'parataxis': 5.56, 'discourse': 7.78, 'obl': 5.56}
parataxis 9.62 {'root': 19.4, 'aux': 7.33, 'conj': 8.62, 'ccomp': 18.53, 'acl': 8.62, 'advcl': 7.76, 'cop': 6.47}
compound:prt 5.51 {'compound': 87.22, 'advmod': 10.53}
vocative 5.27 {'obj': 13.39, 'root': 21.26, 'obl': 10.24, 'appos': 6.3, 'advmod': 8.66, 'nsubj': 13.39, 'discourse': 7.87}
nsubj 5.27 {'root': 33.86, 'det': 9.45, 'obj': 10.24, 'nmod': 7.87, 'expl': 7.09, 'compound': 7.09}


############

ewt
machamp
cardiffnlp-twitter-roberta-base
parent
54_60
advmod 15.46 {'aux': 66.99, 'cop': 9.06, 'root': 5.5}
cop 11.36 {'nsubj': 94.27}
nmod:poss 9.3 {'nmod': 98.92}
root 6.65 {'aux': 12.78, 'advmod': 10.53, 'discourse': 12.03, 'ccomp': 5.26, 'nsubj': 12.03, 'compound': 9.02, 'parataxis': 9.77}
aux 6.1 {'nsubj': 91.8}


twitter
machamp
cardiffnlp-twitter-roberta-base
parent
54_60
nmod:poss 11.01 {'nmod': 98.39}
root 10.77 {'discourse': 10.99, 'cop': 7.69, 'aux': 7.14, 'parataxis': 9.89, 'advmod': 10.99, 'nsubj': 21.43}
compound:prt 5.56 {'advmod': 21.28, 'compound': 76.6}
parataxis 5.15 {'aux': 13.79, 'ccomp': 13.79, 'cop': 20.69, 'root': 20.69, 'conj': 5.75}



esl
machamp
cardiffnlp-twitter-roberta-base
parent
54_60
nmod:poss 11.4 {'nmod': 98.92}
root 10.78 {'discourse': 7.95, 'cop': 7.39, 'advmod': 14.2, 'nsubj': 21.02, 'aux': 6.25, 'compound': 5.11, 'parataxis': 5.11, 'obl': 6.82}
parataxis 6.62 {'cop': 15.74, 'ccomp': 9.26, 'discourse': 9.26, 'aux': 14.81, 'root': 22.22}
vocative 5.94 {'appos': 6.19, 'obl': 14.43, 'nsubj': 13.4, 'root': 12.37, 'obj': 13.4, 'advmod': 7.22, 'discourse': 13.4}
compound:prt 5.76 {'compound': 85.11, 'advmod': 14.89}






ewt
machamp
cardiffnlp-twitter-roberta-base
parent
60_66
advmod 17.42 {'root': 6.45, 'aux': 77.42, 'cop': 5.38}
cop 11.99 {'nsubj': 98.44}
aux 11.42 {'nsubj': 95.08}
nmod:poss 7.87 {'nmod': 100.0}
compound:prt 6.37 {'compound': 73.53, 'advmod': 23.53}
root 5.24 {'advmod': 14.29, 'compound': 10.71, 'discourse': 7.14, 'obl': 7.14, 'nsubj': 14.29, 'aux': 10.71, 'parataxis': 21.43}






twitter
machamp
cardiffnlp-twitter-roberta-base
parent
60_66
nmod:poss 10.71 {'nmod': 100.0}
compound:prt 8.67 {'compound': 85.29, 'advmod': 11.76}
root 8.42 {'advmod': 18.18, 'nsubj': 21.21, 'goeswith': 6.06, 'discourse': 12.12, 'obl': 9.09, 'xcomp': 6.06}
conj 8.42 {'root': 15.15, 'goeswith': 9.09, 'discourse': 27.27, 'nmod': 6.06, 'xcomp': 9.09, 'nsubj': 9.09, 'ccomp': 6.06, 'advmod': 6.06}
mark 5.61 {'case': 13.64, 'advmod': 86.36}





esl
machamp
cardiffnlp-twitter-roberta-base
parent
60_66
nmod:poss 10.85 {'nmod': 100.0}
root 9.82 {'advmod': 15.79, 'nsubj': 23.68, 'compound': 7.89, 'discourse': 5.26, 'aux': 10.53, 'obl': 10.53, 'conj': 5.26, 'xcomp': 5.26}
compound:prt 8.79 {'compound': 88.24, 'advmod': 8.82}
mark 6.46 {'advmod': 76.0, 'case': 16.0, 'obj': 8.0}
conj 6.2 {'compound': 8.33, 'root': 16.67, 'discourse': 29.17, 'parataxis': 8.33, 'advmod': 8.33}
parataxis 6.2 {'conj': 12.5, 'root': 16.67, 'aux': 12.5, 'ccomp': 12.5, 'discourse': 12.5, 'obj': 12.5}
nsubj 5.17 {'root': 25.0, 'obj': 25.0, 'nmod': 5.0, 'expl': 20.0, 'det': 5.0, 'obl': 5.0, 'parataxis': 5.0, 'compound': 5.0, 'nummod': 5.0}
discourse 5.17 {'root': 35.0, 'advmod': 35.0, 'obj': 5.0, 'det': 10.0, 'nsubj': 5.0, 'ccomp': 5.0, 'case': 5.0}


###############################


ewt
machamp
cardiffnlp-twitter-roberta-base
child
18_24
conj 19.39 {'root': 26.24, 'parataxis': 14.42, 'discourse': 16.78, 'compound': 13.24, 'goeswith': 6.15}
root 17.84 {'compound': 47.3, 'discourse': 7.71, 'amod': 10.54, 'advmod': 5.14}
cop 6.88 {'nsubj': 92.67}
vocative 6.79 {'root': 39.19, 'compound': 6.76, 'obj': 20.95, 'nsubj': 14.86, 'discourse': 7.43}
parataxis 6.56 {'advmod': 5.59, 'root': 24.48, 'obj': 9.79, 'conj': 16.78, 'compound': 5.59, 'appos': 5.59, 'acl': 8.39}
nmod:poss 6.01 {'nmod': 78.63, 'compound': 12.98}
nsubj 5.78 {'compound': 27.78, 'obj': 5.56, 'det': 6.35, 'root': 25.4, 'discourse': 7.14}




ewt
machamp
cardiffnlp-twitter-roberta-base
child
24_30
root 16.47 {'compound': 35.4, 'parataxis': 5.81, 'advmod': 6.59, 'nsubj': 7.36, 'amod': 5.43, 'discourse': 12.14, 'flat': 5.04}
conj 13.47 {'root': 20.85, 'discourse': 36.02, 'parataxis': 12.64, 'compound': 13.27}
nmod:poss 8.81 {'nmod': 78.99, 'compound': 11.59, 'root': 6.76}
cop 8.15 {'nsubj': 92.69}
nsubj 6.83 {'compound': 28.97, 'discourse': 5.61, 'nmod': 5.3, 'obj': 5.3, 'det': 8.1, 'root': 32.09}
vocative 5.96 {'root': 38.21, 'nsubj': 9.29, 'obj': 20.0, 'compound': 10.71, 'discourse': 8.21}




twitter
machamp
cardiffnlp-twitter-roberta-base
child
18_24
conj 23.28 {'root': 27.16, 'parataxis': 5.6, 'discourse': 25.43, 'vocative': 7.33, 'compound': 8.41, 'flat': 5.17}
root 20.02 {'nsubj': 8.27, 'compound': 35.34, 'discourse': 17.54, 'amod': 7.52, 'vocative': 5.01}
parataxis 7.68 {'obj': 6.54, 'root': 31.37, 'xcomp': 5.23, 'conj': 5.88, 'appos': 9.15}
nmod:poss 6.57 {'nmod': 77.86, 'compound': 9.92, 'amod': 5.34}
nsubj 5.87 {'root': 24.79, 'vocative': 23.93, 'det': 10.26, 'compound': 14.53, 'discourse': 7.69}




twitter
machamp
cardiffnlp-twitter-roberta-base
child
24_30
root 17.75 {'compound': 18.93, 'det': 5.07, 'advmod': 6.93, 'nsubj': 15.87, 'discourse': 23.07}
conj 16.85 {'root': 20.79, 'discourse': 39.61, 'goeswith': 5.48, 'list': 6.04}
nmod:poss 9.8 {'nmod': 77.78, 'compound': 14.73}
nsubj 7.93 {'det': 12.24, 'root': 40.9, 'vocative': 20.9, 'discourse': 6.27, 'compound': 8.06}
parataxis 5.4 {'root': 29.82, 'obj': 10.53, 'conj': 5.26, 'xcomp': 9.65, 'discourse': 5.26}




esl
machamp
cardiffnlp-twitter-roberta-base
child
18_24
root 19.74 {'compound': 37.53, 'amod': 9.38, 'discourse': 5.9, 'advmod': 9.38, 'nsubj': 7.51}
conj 19.68 {'root': 27.69, 'parataxis': 16.4, 'compound': 15.86, 'appos': 9.14, 'discourse': 7.53}
parataxis 9.21 {'obj': 9.77, 'root': 22.99, 'conj': 27.01, 'appos': 6.32, 'acl': 6.9}
nmod:poss 6.93 {'nmod': 80.15, 'compound': 9.92, 'amod': 5.34}
vocative 6.93 {'root': 35.88, 'obj': 11.45, 'nmod': 10.69, 'nsubj': 16.03, 'appos': 5.34}
nsubj 5.4 {'det': 14.71, 'obj': 6.86, 'root': 21.57, 'vocative': 5.88, 'nmod': 5.88, 'compound': 17.65, 'discourse': 6.86}




esl
machamp
cardiffnlp-twitter-roberta-base
child
24_30
root 17.81 {'compound': 23.6, 'parataxis': 7.33, 'advmod': 10.67, 'nsubj': 15.47, 'discourse': 9.73}
conj 14.13 {'root': 22.02, 'advmod': 6.72, 'appos': 7.39, 'discourse': 15.13, 'compound': 13.61, 'parataxis': 15.63}
nmod:poss 9.83 {'nmod': 78.26, 'compound': 14.49}
discourse 9.03 {'root': 25.79, 'advmod': 21.84, 'compound': 8.68, 'parataxis': 6.05, 'det': 23.68}
nsubj 7.03 {'det': 11.49, 'root': 35.14, 'obl': 5.41, 'nmod': 5.07, 'parataxis': 5.07, 'compound': 15.88}
vocative 6.53 {'nmod': 7.64, 'appos': 6.18, 'obj': 15.27, 'compound': 8.0, 'nsubj': 9.82, 'root': 31.27, 'obl': 8.0}
parataxis 5.7 {'ccomp': 6.25, 'root': 25.42, 'acl': 5.83, 'obj': 10.83, 'conj': 13.75, 'advmod': 5.0}



ewt
machamp
cardiffnlp-twitter-roberta-base
child
48_54
advmod 10.6 {'aux': 59.49, 'root': 9.65, 'compound': 6.11, 'mark': 9.0}
root 9.72 {'parataxis': 10.53, 'aux': 8.07, 'nsubj': 8.07, 'advmod': 5.96, 'compound': 17.19, 'conj': 5.61, 'discourse': 8.07}
nmod:poss 9.31 {'nmod': 98.17}
cop 8.08 {'nsubj': 89.03}
conj 7.02 {'discourse': 23.3, 'root': 17.48, 'parataxis': 8.74, 'compound': 13.11, 'flat': 5.83, 'appos': 6.8}
aux 6.41 {'nsubj': 92.02}




twitter
machamp
cardiffnlp-twitter-roberta-base
child
48_54
conj 11.73 {'discourse': 16.94, 'goeswith': 26.58, 'vocative': 5.65, 'root': 18.94}
root 11.14 {'parataxis': 5.59, 'nsubj': 14.34, 'cop': 5.24, 'advmod': 6.29, 'compound': 7.69, 'discourse': 12.94, 'vocative': 5.59}
nmod:poss 10.63 {'nmod': 96.7}
parataxis 6.23 {'root': 18.12, 'obj': 6.88, 'ccomp': 11.88, 'cop': 5.62, 'xcomp': 10.0, 'advcl': 5.0, 'discourse': 7.5, 'conj': 5.0}
advmod 6.23 {'root': 11.88, 'case': 10.0, 'det': 6.25, 'compound': 45.62, 'discourse': 6.88}




esl
machamp
cardiffnlp-twitter-roberta-base
child
48_54
root 11.57 {'conj': 6.23, 'aux': 5.57, 'nsubj': 13.11, 'advmod': 7.87, 'obj': 6.89, 'compound': 12.13, 'parataxis': 5.57, 'discourse': 8.52, 'nummod': 6.23}
nmod:poss 10.36 {'nmod': 97.44}
conj 8.99 {'discourse': 10.13, 'root': 21.1, 'parataxis': 12.66, 'compound': 20.25}
discourse 7.28 {'advmod': 34.9, 'det': 5.73, 'root': 24.48, 'obj': 5.21}
parataxis 6.45 {'root': 19.41, 'obj': 10.0, 'ccomp': 15.29, 'advcl': 6.47, 'conj': 9.41, 'xcomp': 7.06, 'compound': 7.06}
vocative 5.69 {'root': 13.33, 'obj': 10.67, 'appos': 5.33, 'obl': 26.67, 'nsubj': 17.33, 'nmod': 8.67, 'discourse': 7.33}


ewt
machamp
cardiffnlp-twitter-roberta-base
child
54_60
advmod 10.56 {'root': 8.03, 'aux': 67.47}
root 9.62 {'nsubj': 11.45, 'aux': 9.25, 'parataxis': 15.42, 'compound': 10.13, 'discourse': 8.81, 'advmod': 6.17}
cop 8.9 {'nsubj': 84.76, 'root': 7.14}
nmod:poss 8.56 {'nmod': 96.04}
conj 5.47 {'root': 7.75, 'discourse': 39.53, 'cc': 5.43, 'amod': 6.2, 'parataxis': 10.85, 'obj': 6.2}




ewt
machamp
cardiffnlp-twitter-roberta-base
child
60_66
advmod 14.79 {'aux': 64.34, 'mark': 6.29, 'root': 8.39}
cop 10.13 {'nsubj': 93.88, 'root': 5.1}
root 8.58 {'compound': 6.02, 'discourse': 8.43, 'advmod': 13.25, 'ccomp': 7.23, 'aux': 16.87, 'nsubj': 7.23, 'parataxis': 6.02, 'cop': 6.02}
nmod:poss 7.34 {'nmod': 98.59}
aux 6.93 {'nsubj': 97.01}
conj 5.89 {'root': 12.28, 'amod': 5.26, 'compound': 28.07, 'obj': 5.26, 'discourse': 15.79, 'parataxis': 7.02, 'nsubj': 5.26, 'advmod': 7.02, 'nmod': 5.26}
compound:prt 5.89 {'advmod': 29.82, 'compound': 61.4, 'mark': 5.26}




twitter
machamp
cardiffnlp-twitter-roberta-base
child
54_60
root 12.77 {'acl': 5.18, 'nsubj': 12.35, 'ccomp': 7.17, 'aux': 6.77, 'discourse': 13.15, 'parataxis': 6.37, 'cop': 5.98, 'advmod': 6.37}
nmod:poss 10.27 {'nmod': 96.04}
conj 7.88 {'root': 13.55, 'discourse': 34.84, 'amod': 9.03, 'parataxis': 5.81, 'goeswith': 10.32}
parataxis 6.05 {'root': 27.73, 'ccomp': 14.29, 'acl': 8.4, 'aux': 6.72, 'xcomp': 5.88}
reparandum:repetition 5.95 {'aux': 5.98, 'root': 23.93, 'det': 6.84, 'nsubj': 20.51, 'cc': 16.24}




twitter
machamp
cardiffnlp-twitter-roberta-base
child
60_66
conj 12.78 {'root': 8.82, 'goeswith': 38.24, 'nummod': 6.86, 'discourse': 14.71}
root 11.53 {'nsubj': 10.87, 'acl': 8.7, 'obj': 8.7, 'advmod': 15.22, 'nummod': 8.7, 'discourse': 10.87, 'cop': 7.61}
nmod:poss 8.9 {'nmod': 98.59}
compound:prt 7.14 {'compound': 85.96, 'advmod': 10.53}
advmod 5.51 {'discourse': 6.82, 'det': 9.09, 'compound': 29.55, 'root': 20.45, 'case': 6.82, 'xcomp': 6.82}
parataxis 5.39 {'obj': 6.98, 'ccomp': 20.93, 'cop': 6.98, 'nummod': 6.98, 'advcl': 9.3, 'aux': 9.3, 'xcomp': 9.3, 'root': 6.98}




esl
machamp
cardiffnlp-twitter-roberta-base
child
54_60
root 12.15 {'nsubj': 15.42, 'parataxis': 10.67, 'discourse': 11.86, 'aux': 5.53, 'compound': 5.14, 'ccomp': 6.72, 'advmod': 9.09, 'obl': 5.14}
nmod:poss 9.7 {'nmod': 96.53}
discourse 8.31 {'advmod': 32.37, 'root': 23.7, 'obj': 8.67, 'compound': 6.94}
conj 6.72 {'root': 15.71, 'cc': 6.43, 'discourse': 16.43, 'amod': 10.0, 'advmod': 7.86, 'obj': 5.0, 'parataxis': 6.43, 'compound': 12.86}
parataxis 6.05 {'obj': 8.73, 'root': 31.75, 'ccomp': 13.49, 'acl': 7.14, 'xcomp': 6.35, 'conj': 5.56}
vocative 5.71 {'obj': 10.08, 'nsubj': 16.81, 'root': 14.29, 'iobj': 5.88, 'obl': 13.45, 'discourse': 20.17, 'appos': 5.88}
reparandum:repetition 5.62 {'aux': 5.98, 'root': 21.37, 'det': 6.84, 'nsubj': 17.09, 'cc': 16.24}




esl
machamp
cardiffnlp-twitter-roberta-base
child
60_66
root 10.6 {'nummod': 8.43, 'compound': 7.23, 'acl': 6.02, 'obj': 8.43, 'advmod': 15.66, 'nsubj': 8.43, 'discourse': 8.43, 'cop': 7.23}
conj 9.71 {'root': 21.05, 'compound': 32.89, 'goeswith': 6.58, 'obj': 5.26, 'nmod': 5.26, 'advmod': 6.58, 'discourse': 5.26}
nmod:poss 9.07 {'nmod': 98.59}
compound:prt 7.28 {'compound': 85.96, 'advmod': 12.28}
discourse 6.39 {'root': 24.0, 'det': 22.0, 'advmod': 28.0, 'compound': 8.0}
parataxis 5.87 {'obl': 6.52, 'nsubj': 6.52, 'ccomp': 17.39, 'cop': 6.52, 'nummod': 6.52, 'xcomp': 8.7, 'aux': 6.52, 'advmod': 8.7, 'root': 15.22, 'conj': 6.52}
vocative 5.62 {'iobj': 11.36, 'discourse': 22.73, 'nsubj': 34.09, 'obl': 18.18}



