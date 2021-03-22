FROM python:3.8.2-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# deps
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
COPY * /usr/src/app/

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]