# Natural Language Inference on Hindi MNLI Data Set
==================================
In this project we build a tool that performs Natural Language Inference on Hindi Data. We used pretrained Language Transformers that have been trained on English Data. We the fine tune these transformers on two Hindi NLI Datasets and assess its performance. The Language tranformers that we use are RoBERTa, RobERTa-mnli, and XLMR.
 
## 1. Preprocessing the data
run Hindi_data_prep.py on the Hindi NLI dataset to process the data files and split it into train, test and validation files.

## 2. Run fine tuned model 
For Roberta
Convert data into bpe format by running the multiprocessing_bpe_encoder.py file with this command.
```
python multiprocessing_bpe_encoder.py --encoder-json encoder.json --vocab-bpe vocab.bpe --inputs "sentences_train.txt" --outputs "train.input0.bpe" --workers 1 --keep-empty

python multiprocessing_bpe_encoder.py --encoder-json encoder.json --vocab-bpe vocab.bpe --inputs "sentences_val.txt" --outputs "dev.input0.bpe" --workers 1 --keep-empty
```
for XLM-R
Convert data into sentencepiece format by running the spm_encoder.py file with this command.
```
python spm_encoder.py --inputs "sentences_train.txt" --outputs "train.input0.spm" --workers 1 --keep-empty

python spm_encoder.py --inputs "/content/drive/My Drive/XLMR_XNLI/sentences_val_xnli.txt" --outputs "dev.input0.spm" --workers 1 --keep-empty
```
Preprocess the train and validation bpe files by running this command.
data and add it to the fairseq dict.txt
```
fairseq-preprocess --only-source --trainpref "train.input0.bpe" --validpref "dev.input0.bpe" --destdir "train-bin/input0" --workers 60 --srcdict dict.txt
```
Preprocess the train and validation label files by running this command.
```
fairseq-preprocess --only-source --trainpref "labels_train.txt" --validpref "labels_val.txt" --destdir "train-bin/label" --workers 60
```
Fine-tune hypermarameters of the pretrained roberta-mnli model by running the following command.
```
python train.py train-bin/ \
    --restore-file model.pt \
    --max-positions 512 \
    --max-sentences 2 \
    --max-tokens 4400 \
    --task sentence_prediction \
    --reset-optimizer --reset-dataloader --reset-meters \
    --required-batch-size-multiple 1 \
    --init-token 0 --separator-token 2 \
    --arch roberta_large \
    --criterion sentence_prediction \
    --num-classes 2 \
    --dropout 0.1 --attention-dropout 0.1 \
    --weight-decay 0.1 --optimizer adam --adam-betas "(0.9, 0.98)" --adam-eps 1e-04 \
    --clip-norm 0.0 \
    --lr-scheduler polynomial_decay --lr 0.00001 --total-num-update 10000 --warmup-updates 50 \
    --fp16 --fp16-init-scale 4 --threshold-loss-scale 1 --fp16-scale-window 128 \
    --max-epoch 5 \
    --best-checkpoint-metric accuracy --maximize-best-checkpoint-metric \
    --truncate-sequence \
    --find-unused-parameters \
    --update-freq 16
```




