

import csv
import codecs
import json
import numpy as np
fpaths=r"XNLI-1.0\XNLI-1.0\xnli.dev.jsonl"
sa, sb, lb = [], [], []
fpaths = np.atleast_1d(fpaths)
for fpath in fpaths:
    with open(fpath) as fi:
        for line in fi:
            
            sample = json.loads(line)
            if sample['language']=='hi':
                sa.append(sample['sentence1'])
                sb.append(sample['sentence2'])
                lb.append(sample['gold_label'])


count=0

print
with codecs.open('sentences_val_xnli.txt', 'w',"utf-8") as output_file,codecs.open('labels_val_xnli.txt', 'w',"utf-8") as output_file2:
    for i in range(len(sa)):

             
             output_file.write(sa[i]+'\t'+sb[i]+'\n')
             if lb[i]=='entailment':
                 count+=1
                 output_file2.write(str(2)+'\n')
             elif lb[i]=='neutral':
                count+=1
                output_file2.write(str(1)+'\n')
             elif lb[i]=='contradiction':
               
                output_file2.write(str(0)+'\n')

print(count)
output_file.close()
output_file2.close()




fpaths=r"XNLI-1.0\XNLI-1.0\xnli.test.jsonl"
sa, sb, lb = [], [], []
fpaths = np.atleast_1d(fpaths)
for fpath in fpaths:
    with open(fpath) as fi:
        for line in fi:
            
            sample = json.loads(line)
            if sample['language']=='hi':
                sa.append(sample['sentence1'])
                sb.append(sample['sentence2'])
                lb.append(sample['gold_label'])


count=0


with codecs.open('sentences_test_xnli.txt', 'w',"utf-8") as output_file,codecs.open('labels_test_xnli.txt', 'w',"utf-8") as output_file2:
    for i in range(len(sa)):

             
             output_file.write(sa[i]+'\t'+sb[i]+'\n')
             if lb[i]=='entailment':
                 count+=1
                 output_file2.write(str(2)+'\n')
             elif lb[i]=='neutral':
                count+=1
                output_file2.write(str(1)+'\n')
             elif lb[i]=='contradiction':
               
                output_file2.write(str(0)+'\n')


output_file.close()
output_file2.close()
