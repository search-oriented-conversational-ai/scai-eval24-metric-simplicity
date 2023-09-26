# scai-eval-simplicity
Calculates Flesch-Kincaid readability levels for SCAI Eval.

Labels each turn based on the readability score of the response, loosely based on the [table in Wikipedia](https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests#Flesch_reading_ease):
```python
if score <= 30:
    labels[turn_id] = ["very-difficult"]
elif score <= 60:
    labels[turn_id] = ["difficult"]
elif score <= 90:
    labels[turn_id] = ["easy"]
else:
    labels[turn_id] = ["very-easy"]
```

Calculation is based on [LFTK](https://github.com/brucewlee/lftk).

## Local
Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python -m spacy download en_core_web_sm
```

Run
```bash
python3 simplicity.py example.ndjson
```

## Docker
```bash
docker build -t webis/scai-eval24-metric-simplicity:1.0.0 .
docker run --rm -it -v $PWD:/data webis/scai-eval24-metric-simplicity:1.0.0 /data/example.ndjson
docker publish webis/scai-eval24-metric-simplicity:1.0.0
```

## TIRA
```bash
python3 /app/simplicity.py $inputDataset/* > $outputDir/run.ndjson
```
