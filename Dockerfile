#
# Docker file for Message in a Bottle v1.0
#
FROM python:3.8
LABEL maintainer="<squa_id>_squad"
LABEL version="1.0"
LABEL description="Message in a Bottle User Microservice"

# creating the environment
COPY . /mib-lottery
# setting the workdir
WORKDIR /mib-lottery

# installing all requirements
RUN ["pip", "install", "-r", "requirements.prod.txt"]

# exposing the port
EXPOSE 5003/tcp

# Main command
CMD ["gunicorn", "--config", "gunicorn.conf.py", "wsgi:app"]