##To run fine tuned-roberta mnli model 

Convert data into bpe format by running the multiprocessing_bpe_encoder.py file with this command.
```
python multiprocessing_bpe_encoder.py --encoder-json encoder.json --vocab-bpe vocab.bpe --inputs "sentences_train.txt" --outputs "train.input0.bpe" --workers 1 --keep-empty

python multiprocessing_bpe_encoder.py --encoder-json encoder.json --vocab-bpe vocab.bpe --inputs "sentences_val.txt" --outputs "dev.input0.bpe" --workers 1 --keep-empty
```
##preprocess the train and validation bpe files by running this command.
data and add it to the fairseq dict.txt
```
fairseq-preprocess --only-source --trainpref "train.input0.bpe" --validpref "dev.input0.bpe" --destdir "train-bin/input0" --workers 60 --srcdict dict.txt
```
preprocess the train and validation label files by running this command.
```
fairseq-preprocess --only-source --trainpref "labels_train.txt" --validpref "labels_val.txt" --destdir "train-bin/label" --workers 60
```
fine-tune hypermarameters of the pretrained roberta-mnli model by running the following command.
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




