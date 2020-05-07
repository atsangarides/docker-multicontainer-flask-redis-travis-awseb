FROM python:3.8-slim-buster

# create new folder called "app" and set as working dir
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# copy everything to working dir
COPY ./ ./

CMD python worker.py