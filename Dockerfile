FROM python:3.10-bullseye

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        watchman \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt


VOLUME /app
EXPOSE 8000
CMD ["./docker-run.sh"]
