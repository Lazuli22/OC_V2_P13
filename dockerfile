FROM python:3.10-alpine

WORKDIR /code

COPY . /code

RUN pip install -r requirements.txt

EXPOSE 8000  

CMD python manage.py runserver 0.0.0.0:$PORT
