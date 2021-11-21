FROM python:3
LABEL maintainer="RCaldas <docker@rcaldas.com>"

COPY requirements.txt /images/
WORKDIR /images
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY images.py /images/
ENTRYPOINT python /images/images.py
