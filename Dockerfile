FROM nginx/unit:1.28.0-python3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /code
COPY . /code

RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY static /srv/www/todo/
COPY unit.json /var/lib/unit/conf.json

RUN mkdir log
RUN python manage.py makemigrations
RUN python manage.py migrate

RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "--bind", "0.0.0.0:8070", "core.wsgi:application"]

