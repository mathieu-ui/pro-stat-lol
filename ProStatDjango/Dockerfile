FROM python:3.12
RUN mkdir /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install django requests
COPY . /app/
CMD python manage.py runserver --insecure 0.0.0.0:8000