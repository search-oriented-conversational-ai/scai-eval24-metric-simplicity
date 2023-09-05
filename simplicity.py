import click

features = ["fkre", "rt_average"]

@click.command()
@click.argument('inputs', nargs=-1, type=click.File())
def simplicity(inputs):
    import lftk
    import ndjson
    import spacy

    nlp = spacy.load("en_core_web_sm")
    scores = {}
    for file in inputs:
        for conversation in ndjson.reader(file):
            for turn in conversation["turns"]:
                turn_id = turn["id"]
                response = turn["response"]
                scores[turn_id] = lftk.Extractor(docs = nlp(response)).extract(features = features)
    print(ndjson.dumps([scores]))

if __name__ == '__main__':
    simplicity()

