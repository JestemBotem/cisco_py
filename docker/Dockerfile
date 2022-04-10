FROM python:3.10-alpine

WORKDIR /usr/src/app

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY src/requirements.txt /usr/src/app/requirements.txt
RUN pip3 install -r requirements.txt

# copy entrypoint.sh
COPY ../docker/entrypoint.sh /usr/src/app/entrypoint.sh

COPY src/ /usr/src/app

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
