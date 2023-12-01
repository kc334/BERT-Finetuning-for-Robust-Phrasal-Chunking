# BERT Finetuning for Robust Phrasal Chunking
## Reference
This is my homework one for advanced nlp class. Below is the description link to it

    https://anoopsarkar.github.io/advanced-nlp-class/hw1.html

## Approach
Leveraged the capabilities of a BERT-based Transformer model that is fine-tuned to predict the phrase chunking tags for each (sub-word) token and used it as the baseline.
Augmented the training data with additional noisy examples. This approach aimed to make the model more resilient to errors and inconsistencies in real-world data. As a result of this innovation, there was a notable improvement in model performance, achieving an accuracy increase of about 5% over the baseline.
## Dataset
Dataset used is from CoNLL 2000. Validation and testing dataset are infected with noise or typo.

## Bert based model file

The bert based model mentioned above can be downloaded from here:

https://drive.google.com/file/d/1Cob8vewgpvNhJ2KnZlYq2Tntkgc0l2yx/view

Put the file on the path `data/chunker.pt`

## Installation

Make sure you setup your virtual environment:

    python3.10 -m venv venv
    source venv/bin/activate
    pip install -U -r requirements.txt

## Train on the data files

    python3 zipout.py

For more options:

    python3 zipout.py -h

## Check your accuracy

To check your accuracy on the dev set:

    python3 check.py

For more options:

    python3 check.py -h

In particular use the log file to check your output evaluation:

    python3 check.py -l log



## Data files

The data files provided are:

* `data/train.txt.gz` -- CoNLL 2000 training data
* `data/input` -- input files `dev.txt` and `test.txt`
* `data/reference/dev.out` -- reference output for the `dev.txt` input file

