FROM python:3.7
ENV MLP_BOT=${MLP_BOT}
ENV MLP_BOTGIT=${MLP_GIT}
RUN mkdir /code
WORKDIR /code
ADD . /code
RUN pip install -r requirements.txt

CMD ["python","/code/python_test/bot.py"]