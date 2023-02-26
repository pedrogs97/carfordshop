FROM python:3.9-alpine3.13

ENV PYTHONUNBUFFERED 1

COPY . /app
COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock
WORKDIR /app
EXPOSE 8000

RUN /py/bin/pip install --upgrade pip && \
    pip install pipenv && pipenv install && \
    apk add --update --no-cache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev zlib zlib-dev linux-headers && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER django-user

CMD ["python", "main.py"]