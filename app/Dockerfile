# python runtime
FROM python:3.6
 
# working directory and set ENV
RUN mkdir /app
WORKDIR /app
ENV FLASK_APP=paxful.py
 
# copy current directory into the container
ADD . /app
 
# install requirements
RUN pip3.6 install -r requirements.txt
 
# make port 5000 available to the world outside
EXPOSE 5000
#CMD ["flask run --host=0.0.0.0"]
ENTRYPOINT [ "python3.6" ]
CMD [ "paxful.py" ]

