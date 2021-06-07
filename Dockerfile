#GRAB TH LATEST ALPINE IMAGE
FROM alpine:latest


#Install python and pip
RUN apk add --no-cache --update python3 py3-pip bash
ADD ./Movie-Recommendation-Engine/requirements.txt /tmp/requiremnents.txt

#ADD our code
ADD ./Movie-Recommendation-Engine /opt/Movie-Recommendation-Engine/

#Changing working directory
WORKDIR /opt/Movie-Recommendation-Engine

#EXPOSE 5000

RUN adduser -D myuser
USER myuser

#RUN THE APP. CMD IS REQUIRED TO RUN ON HEROKU
# $PORT is set by heroku

CMD gunicorn --bind 0.0.0.0:$PORT app