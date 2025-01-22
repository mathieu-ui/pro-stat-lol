FROM python:3.12

WORKDIR /app

COPY ./ProStatDjango /app/

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "--insecure", "0.0.0.0:8000"]