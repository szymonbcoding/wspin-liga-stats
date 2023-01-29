FROM python:3.9.15

ADD requirements.txt ./

ADD data ./data/

ADD .env ./

RUN pip3 install -r requirements.txt

ADD scrapper.py ./

CMD ["python3", "./scrapper.py"]