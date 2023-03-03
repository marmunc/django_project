FROM python:3.10.9

SHELL ["/bin/bash", "-c"]

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim

RUN useradd -rms /bin/bash dj && chmod 777 /opt /run

WORKDIR /dj

RUN mkdir /dj/static && mkdir /dj/media && chown -R dj:dj /dj && chmod 755 /dj

COPY --chown=dj:dj . .

RUN pip install -r requirements.txt

USER dj

CMD ["gunicorn","-b","0.0.0.0:8001","backend.wsgi:application"]

#####################
version: "3.9"

services:
  db:
    image: postgres:15
    container_name: postgres
    volumes:
      - ~/.pg/pg_data/dj:/var/lib/postgresql/data
    env_file:
      - .env

  django:
    build:
      dockerfile: Dockerfile
      context: .
    ##image: django:latest
    container_name: django
    depends_on:
      - db
    volumes:
      - static_volume:/dj/static
      - media_volume:/dj/media
    env_file:
      - .env
    command: >
      bash -c "./backend/manage.py collectstatic --noinput && ./backend/manage.py migrate && gunicorn -b 0.0.0.0:8000 backend.wsgi:application"

  nginx:
    build:
      dockerfile: ./Dockerfile
      context: ./docker/nginx/
    container_name: nginx
    image: nginx
    volumes:
      - static_volume:/dj/static
      - media_volume:/dj/media
    depends_on:
      - django
    ports:
      - "${NGINX_EXTERNAL_PORT}:80"

volumes:
  static_volume:
  media_volume:
