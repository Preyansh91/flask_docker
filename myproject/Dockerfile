FROM ubuntu:16.04

RUN apt-get update \ 
#    && apt-get upgrade -y \
    && apt-get install -y python-pip python-dev libmysqlclient-dev \
    && pip install virtualenv \
    && pip install flask \
    && pip install uwsgi \
    && pip install MySQL-python

RUN mkdir -p /home/myproject; mkdir -p /var/log/uwsgi

COPY . /home/myproject

COPY myproject.ini /etc/uwsgi/

RUN touch /var/log/uwsgi/myproject.log; chmod 777 /var/log/uwsgi/myproject.log

WORKDIR /home/myproject

CMD ["uwsgi", "--ini", "/etc/uwsgi/myproject.ini", "--die-on-term"]



#RUN mkdir -p /home/preyansh/app; mkdir -p /var/log/uwsgi; touch /etc/systemd/system/app.service

#COPY . /home/preyansh/app

#COPY /etc/systemd/system/app.service /etc/systemd/system/app.service

#RUN cp /home/preyansh/app/app.service /etc/systemd/system/app.service; touch /var/log/uwsgi/app.log; chmod 777 /var/log/uwsgi/app.log; chmod 777 /home/preyansh/app/*

#CMD cd /home/preyansh/app; systemctl start app; systemctl enable app
#CMD  cd /home/flaskapp ; pwd ; uwsgi --socket 0.0.0.0:8000 --protocol=http -w wsgi

      
