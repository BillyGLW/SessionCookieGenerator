FROM python:3.8.2-alpine

WORKDIR /usr/src/appv1

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# deps
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
COPY ./requirements.txt /usr/src/appv1/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
COPY ./entrypoint.sh /usr/src/appv1/entrypoint.sh
COPY * /usr/src/app/
COPY . /usr/src/appv1/
RUN ls -la
RUN ls -la project
RUN pwd
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]