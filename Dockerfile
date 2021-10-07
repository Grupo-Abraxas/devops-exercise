FROM python:slim
LABEL maintainer="oalvarez-in"
COPY . /service
WORKDIR /service
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
