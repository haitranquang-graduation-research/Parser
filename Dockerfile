FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirement.txt requirement.txt
RUN pip3 install -r requirement.txt

COPY . .

EXPOSE 5000

CMD [ "python3", "app/parser/app.py"]

