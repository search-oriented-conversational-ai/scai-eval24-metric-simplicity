# scai-eval-simplicity
Calculates standard text simplicity metrics for SCAI Eval.

Based on [LFTK](https://github.com/brucewlee/lftk).

## Docker
TODO

## Local
```
# Setup
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python -m spacy download en_core_web_sm

# Run
python3 simplicity.py example.jsonl
```
