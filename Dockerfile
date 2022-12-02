FROM python:3.7.13
ENV TimeZone=Asia/Shanghai
WORKDIR /flask_model
ADD . /flask_model
RUN pip install -r requirements.txt
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone
#RUN python Manager.py db init
#RUN python Manager.py db migrate
#RUN python Manager.py db upgrade
CMD gunicorn -c gunicorn-config.py --preload app:app