FROM python:3
MAINTAINER Eduardo Camarillo camarillor.eduardo@gmail.com

ADD app/app.py /apps/abraxas/

RUN pip install Flask

EXPOSE 5000/tcp

CMD [ "python", "/apps/abraxas/app.py" ]
