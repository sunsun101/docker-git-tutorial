FROM python:3.9.7-buster
WORKDIR /home/src

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./src /home/src/
EXPOSE 8000
CMD uvicorn --host 0.0.0.0 api:app --forwarded-allow-ips '*' --reload 