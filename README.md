# SCAI Eval 2024 Metric: Simplicity
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


## Dockerized
```bash
docker build -t registry.webis.de/code-research/tira/tira-user-scai-info/scai-eval24-metric-simplicity:1.0.0 .
docker run --rm -it -v $PWD:/data registry.webis.de/code-research/tira/tira-user-scai-info/scai-eval24-metric-simplicity:1.0.0 /data/example.ndjson
```

Run on SCAI Eval 2024 data (will be downloaded automatically)
```bash
tira-run \
  --input-dataset scai-eval-2024-metric-submission/scai-eval24-2023-09-26-20230926-training \
  --image registry.webis.de/code-research/tira/tira-user-scai-info/scai-eval24-metric-simplicity:1.0.0 \
  --evaluate true \
  --command 'python3 /app/simplicity.py $inputDataset/* > $outputDir/run.json'

# view labels
less tira-output/run.json
```

In step 2 of the "Create New Docker Software" dialog in TIRA, click on "PUSH NEW DOCKER IMAGE" to get instructions to upload your own image. Use the same command as above in TIRA. For this metric, it is:
```bash
python3 /app/simplicity.py $inputDataset/* > $outputDir/run.json
```


