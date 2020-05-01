import csv
import codecs
count=0
file=r'recasted-hindi-nli-data\recasted-hindi-nli-data\bhaav\bhaav_recasted.tsv'#path to data
sa=[]
sb=[]
lb=[]
with open(file, encoding='utf-8') as f:
    reader = csv.reader(f,delimiter='\t')
    for row in reader:
       
       
        
        
        if len(row)==3:
            count+=1
            
            sa.append(row[0])
            sb.append(row[1])
            lb.append(row[2])


count1=0
count2=0
with codecs.open('sentences_train_Bh.txt', 'w',"utf-8") as output_file,codecs.open('labels_train_Bh.txt', 'w',"utf-8") as output_file2:
    for i in range(len(sa[0:60000])):
         
         if lb[i]=='entailed':
             output_file.write(sa[i]+'\t'+sb[i]+'\n')
             output_file2.write(str(0)+'\n')
             count1+=1
         else:
            if count2<=12000:
                output_file.write(sa[i]+'\t'+sb[i]+'\n')
                count2+=1
                output_file2.write(str(1)+'\n')
print(count1)
print(count2)
       
output_file.close()
output_file2.close()
count1=0
count2=0

with codecs.open('sentences_val_Bh.txt', 'w',"utf-8") as output_file,codecs.open('labels_val_Bh.txt', 'w',"utf-8") as output_file2:
    for i in range(len(sa[60000:70000])):
         
         if lb[i]=='entailed':
             count1+=1
             output_file.write(sa[i]+'\t'+sb[i]+'\n')
             output_file2.write(str(0)+'\n')
         else:
            if count2<=count1:
                count2+=1
                output_file.write(sa[i]+'\t'+sb[i]+'\n')
                output_file2.write(str(1)+'\n')
        
        
output_file.close()
output_file2.close()
        

count1=0
count2=0 
with codecs.open('sentences_test_Bh.txt', 'w',"utf-8") as output_file,codecs.open('labels_test_Bh.txt', 'w',"utf-8") as output_file2:
    for i in range(len(sa[70000:])):
        
         if lb[i]=='entailed':
             count1+=1
             output_file.write(sa[i]+'\t'+sb[i]+'\n')
             output_file2.write(str(0)+'\n')
         else:
            if count2<=count1:
                count2+=1
                output_file.write(sa[i]+'\t'+sb[i]+'\n')
                output_file2.write(str(1)+'\n')
        
         
         
output_file.close()
output_file2.close()
      
