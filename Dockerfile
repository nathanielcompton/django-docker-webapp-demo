FROM python:3.8.0-alpine

LABEL Author="Nathaniel Compton"
LABEL E-mail="nathanielcompton@gmail.com"
LABEL version="1.0.0"

# Set working directory
WORKDIR /usr/src/app

# Python Environment Variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# Install requirements dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# Copy entrypoint script and project files
COPY ./docker-entrypoint.sh /usr/src/app/docker-entrypoint.sh
COPY . /usr/src/app/

# Run the entrypoint script
ENTRYPOINT ["/usr/src/app/docker-entrypoint.sh"]
