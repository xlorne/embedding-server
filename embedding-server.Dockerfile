FROM python:3.12.9
WORKDIR /opt/server/
COPY . /opt/server/
RUN pip install -r requirements.txt