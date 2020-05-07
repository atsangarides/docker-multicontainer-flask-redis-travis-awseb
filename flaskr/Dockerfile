FROM python:3.7.7-stretch

EXPOSE 5000

# create new folder called "app" and set as working dir
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# copy everything to working dir
COPY ./ ./

# Give execute permission to below file, so that the script can be executed by docker.
#RUN chmod 777 entrypoint.sh
# set file permissions
ADD ./entrypoint.sh /tmp/entrypoint.sh
RUN chmod 777 /tmp/entrypoint.sh

#CMD python main.py
#CMD sleep 5; uwsgi uwsgi.ini
CMD ["/tmp/entrypoint.sh"]
