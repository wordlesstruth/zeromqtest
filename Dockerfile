FROM python:3-slim as base

WORKDIR /config/

COPY resources/requirements.txt .

RUN pip install -r requirements.txt

FROM base as service

WORKDIR /usr/src/app/

COPY src/*.py /usr/src/app/
CMD [ "python", "publisher.py" ]
