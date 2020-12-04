FROM python:3.7

ENV DJANGO_SETTINGS_MODULE AsYouWish.production

ENV PYTHONUNBUFFERED 1

RUN mkdir AsYouWish_Serv

WORKDIR /AsYouWish_Serv

ADD . /AsYouWish_Serv

RUN ./setup.sh

ENTRYPOINT ["./start.sh"]

EXPOSE 80