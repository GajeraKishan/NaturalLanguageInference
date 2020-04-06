import csv
import codecs
count=0
file=r'recasted-hindi-nli-data\recasted-hindi-nli-data\bhaav\bhaav_recasted.tsv'
sa=[]
sb=[]
lb=[]
with open(file, encoding='utf-8') as f:
    reader = csv.reader(f,delimiter='\t')
    for row in reader:
        print(row[0])
        print(row[1])
        
        
        if len(row)==3:
            count+=1
            sa.append(row[0])
            sb.append(row[1])
            lb.append(row[2])


with codecs.open('sentences_train.txt', 'w',"utf-8") as output_file,codecs.open('labels_train.txt', 'w',"utf-8") as output_file2:
    for i in range(len(sa[0:60000])):
         output_file.write(sa[i]+'\t'+sb[i]+'\n')
         if lb[i]=='entailed':
             output_file2.write(str(0)+'\n')
         else:
            output_file2.write(str(1)+'\n')
        
output_file.close()
output_file2.close()

with codecs.open('sentences_val.txt', 'w',"utf-8") as output_file,codecs.open('labels_val.txt', 'w',"utf-8") as output_file2:
    for i in range(len(sa[60000:70000])):
         output_file.write(sa[i]+'\t'+sb[i]+'\n')
         if lb[i]=='entailed':
             output_file2.write(str(0)+'\n')
         else:
            output_file2.write(str(1)+'\n')
        
        
output_file.close()
output_file2.close()
        
        
with codecs.open('sentences_test.txt', 'w',"utf-8") as output_file,codecs.open('labels_test.txt', 'w',"utf-8") as output_file2:
    for i in range(len(sa[70000:])):
         output_file.write(sa[i]+'\t'+sb[i]+'\n')
         if lb[i]=='entailed':
             output_file2.write(str(0)+'\n')
         else:
            output_file2.write(str(1)+'\n')
        
         
         
output_file.close()
output_file2.close()
        