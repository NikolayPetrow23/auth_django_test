FROM python:3.9

WORKDIR /app

COPY .. .

RUN chmod a+x docker/*.sh
RUN pip install --upgrade pip
RUN pip install -r requirements.txt