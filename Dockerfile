# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster


COPY ./requirement.txt /app/requirement.txt

WORKDIR /app
# Install pip requirements
RUN pip3 install -r requirement.txt

COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]
