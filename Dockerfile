
FROM python:2.7
MAINTAINER EDUARDO X DUARTE <messengeroot@gmail.com>
ADD . /devops-exercise
WORKDIR /devops-exercise
RUN pip install -r requirement.txt
