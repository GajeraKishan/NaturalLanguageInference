# -*- coding: utf-8 -*-
import torch
roberta = torch.hub.load('pytorch/fairseq', 'roberta.large.mnli')
roberta.eval()  

import codecs


filepath_data='sentences_val.txt'
filepath_labels='labels_val.txt'
sentences=[]
labels=[]
with codecs.open(filepath_data,'r',encoding='utf-8') as fp:
   lines = fp.readlines()
   for line in lines:
       line=line.strip('\n')
       sentences.append(line.split('\t'))
fp.close()
 
 
 
with codecs.open(filepath_labels,'r',encoding='utf-8') as fp:
   lines = fp.readlines()
   for line in lines:
       line=line.strip('\n')
         
       labels.append(int(line))#0=entailed,1=not-entailed.
fp.close()

count=0
for i in range(0,len(sentences)):
   
    tokens = roberta.encode(sentences[i][0],sentences[i][1])
    pred=(roberta.predict('mnli', tokens).argmax()).item() #entailment=2,#neutral=1,#contradiction=0
    
    if (pred==2 and labels[i]==0) or ((pred==0 or pred==1) and labels[i]==1):
        count+=1
    

print("Accuracy",count/10000)
