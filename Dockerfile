FROM debian:jessie

RUN apt-get update && apt-get install -y python3 git python3-pip \
	libmysqlclient-dev locales build-essential python3-dev --no-install-recommends

WORKDIR /

RUN dpkg-reconfigure locales && \
	locale-gen C.UTF-8 && \
	/usr/sbin/update-locale LANG=C.UTF-8
ENV LC_ALL C.UTF-8

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

ADD gunicorn_starter.bash /gunicorn_starter.bash
ADD . /challengeboard
RUN mkdir /static

WORKDIR /challengeboard

RUN pip3 install -r requirements.txt
ENV DJANGO_SETTINGS_MODULE=challengeboard.deploy_settings
RUN pip3 install gunicorn mysqlclient
RUN python3 manage.py collectstatic --noinput

ADD gunicorn_starter.bash /gunicorn_starter.bash
RUN chmod +x /gunicorn_starter.bash

RUN mkdir /data
VOLUME /data

EXPOSE 80
ENTRYPOINT ["/gunicorn_starter.bash"]

