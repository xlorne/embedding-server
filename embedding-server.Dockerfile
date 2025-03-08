FROM python:3.12.9
WORKDIR /opt/server/
COPY . /opt/server/
RUN pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
RUN pip install -r requirements.txt