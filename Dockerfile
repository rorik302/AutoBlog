FROM tiangolo/uwsgi-nginx-flask:python3.8

WORKDIR /app

COPY project/requirements.txt .
RUN pip install -r requirements.txt

COPY project/ .
