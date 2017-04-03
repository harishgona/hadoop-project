FROM tiangolo/uwsgi-nginx-flask:flask-index
COPY ./app /app

RUN pip install flask-restful

RUN pip install requests

