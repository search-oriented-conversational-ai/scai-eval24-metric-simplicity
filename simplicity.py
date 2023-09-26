import click

@click.command()
@click.argument('inputs', nargs=-1, type=click.File())
def simplicity(inputs):
    import lftk
    import ndjson
    import spacy

    nlp = spacy.load("en_core_web_sm")
    labels = {}
    for file in inputs:
        for conversation in ndjson.reader(file):
            for turn in conversation["turns"]:
                turn_id = turn["id"]
                response = turn["response"]
                score = lftk.Extractor(docs = nlp(response)).extract(features = ["fkre"])["fkre"]
                if score <= 30:
                    labels[turn_id] = ["very-difficult"]
                elif score <= 60:
                    labels[turn_id] = ["difficult"]
                elif score <= 90:
                    labels[turn_id] = ["easy"]
                else:
                    labels[turn_id] = ["very-easy"]
    print(ndjson.dumps([labels]))

if __name__ == '__main__':
    simplicity()

