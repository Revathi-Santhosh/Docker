FROM  python:2.7.17-alpine3.10

RUN mkdir /application /application/templates /tmp/logs

WORKDIR /application

ADD app.py /application/app.py
ADD index.html /application/templates/index.html

ADD requirements.txt /application/requirements.txt

RUN pip install virtualenv
RUN virtualenv venv
RUN  source venv/bin/activate
RUN pip install -r requirements.txt

EXPOSE 7000

ENTRYPOINT ["python2","/application/app.py"]
