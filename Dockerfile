FROM python:2

EXPOSE 4000
ADD requirements.txt /weixin/requirements.txt
WORKDIR /weixin
RUN pip install -r requirements.txt
