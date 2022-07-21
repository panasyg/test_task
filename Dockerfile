FROM python:3
EXPOSE 8000
RUN mkdir /simplewebserverpy
COPY . /simplewebserverpy
# WORKDIR /simplewebserverpy
RUN pip3 install httpserver

CMD python3 /simplewebserverpy/web.py