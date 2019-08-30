FROM python:3.7

ARG MLP_BOT
ARG MLP_GIT
ENV MLP_BOT=$MLP_BOT
ENV MLP_GIT=$MLP_GIT
RUN mkdir /code
WORKDIR /code
ADD . /code
RUN pip install -r requirements.txt

CMD ["python","/code/python_test/bot.py"]