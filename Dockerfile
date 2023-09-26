FROM python:3.10

ENV VIRTUAL_ENV=/opt/venv

RUN mkdir /app
WORKDIR /app
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt /app/
RUN pip3 install -r requirements.txt
RUN python3 -m spacy download en_core_web_sm

COPY simplicity.py /app/
ENTRYPOINT [ "python3", "simplicity.py" ]
