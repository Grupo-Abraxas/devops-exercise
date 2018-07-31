FROM python:alpine3.7

RUN apk update

ENV root /project
RUN mkdir $root

WORKDIR $root

ADD ./requirement.txt $root

RUN pip install -r requirement.txt

ADD . $root

EXPOSE 5000

CMD ["/usr/local/bin/gunicorn", "-b", ":5000", "app:app"]