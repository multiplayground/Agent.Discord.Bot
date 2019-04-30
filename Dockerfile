FROM python:3.7

RUN mkdir /code
WORKDIR /code
ADD . /code
RUN pip install -r requirements.txt

CMD ["python","/code/python_test/bot.py"]
