# start by pulling the python image
FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3 python3-pip

RUN pip3 install pyyaml

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

#RUN mkdir /home/ymlgenerator
RUN mkdir /home/ymlfiles

COPY ./ymlgenerator  /app/ymlgenerator
RUN touch /app/ymlgenerator/inputfile.txt
RUN touch /app/inputfile.txt


# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python3" ]

CMD ["mainflask.py" ]
