# Imagen base Alpine
FROM python:alpine3.7

# Actualizacion de paquetes alpine
RUN apk update

# Metadata para imagen
LABEL mantainer="kr.rdz.20@gmail.com" \
      last_update="01-08-2018"

# Definición del directorio para proyecto
ENV root /project
RUN mkdir $root
WORKDIR $root

# Instalación de librerias
ADD ./requirement.txt $root
RUN pip install -r requirement.txt

# Definición de archivos de programa
ADD . $root

EXPOSE 5000

CMD ["/usr/local/bin/gunicorn", "-b", ":5000", "app:app"]