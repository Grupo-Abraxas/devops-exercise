FROM python:3.7

RUN apt-get update && apt-get install

ENV root /project
RUN mkdir $root

WORKDIR $root

ADD ./requirement.txt $root

RUN pip install -r requirement.txt

ADD . $root

EXPOSE 5000

CMD ["/usr/local/bin/gunicorn", "-w", "2", "-b", ":5000", "app:app"]