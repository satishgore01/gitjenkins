**CI/CD Flask App Project with AWS, Git, Jenkins, and Docker**
This project demonstrates a continuous integration and continuous deployment (CI/CD) pipeline for a Flask web application using Jenkins. 
The CI/CD pipeline includes AWS instance creation, Git version control, Jenkins for automation, and Docker for containerization.

**Prerequisites**
Before setting up the CI/CD pipeline for this project, ensure you have the following prerequisites in place:
1)Ubuntu 20.04 server with SSH access.
2)AWS account and necessary IAM permissions.
3)Git installed on your local machine and Jenkins server.
4)Docker and Docker Compose installed on your Ubuntu server.

**Project Structure**
cicd-flask-app/
|-- app/
|   |-- ... (Flask app files)
|-- jenkins/
|   |-- ... (Jenkins pipeline configuration)
|-- Dockerfile
|-- docker-compose.yml
|-- README.md
|-- ...

**app/:** Contains your Flask application code.
**jenkins/**: Contains Jenkins pipeline configuration files.
**Dockerfile:** Defines how to build the Docker image for your Flask app.
**docker-compose.yml:** Configuration for running your app in Docker containers.

**Setting up AWS**
Create an AWS EC2 instance with Ubuntu 20.04.
SSH into your AWS instance.
Configure your AWS CLI with your credentials.

**Setting up Git**
Install Git on your local machine.
**Clone this repository.**

git clone https://github.com/satishgore01/gitjenkins.git

**Configure Git with your name and email.**
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"

**Setting up Jenkins**
Install Jenkins on your server following the official documentation.
Install necessary Jenkins plugins (e.g., Git, Docker, AWS).
Create a Jenkins pipeline job using the configuration in the jenkins/ folder

**Setting up Docker**
Install Docker and Docker Compose on your Ubuntu server following the official documentation.

**docker-file**
# start by pulling the python image

FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y vim
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
CMD ["newbuild.py" ]![image](https://github.com/satishgore01/gitjenkins/assets/148797721/a4c64102-523e-4abd-9cb9-00b3e57bb925)

**CICD-PIPELINE**


pipeline {
    agent any
    stages {
        stage('clone code from github') {
            steps {
               git url: "https://github.com/satishgore01/gitjenkins.git", branch: "satish
            }
        }
        stage('docker image build') {
            steps {
               sh "docker build -t myflaskapp ."
            }
        }
        stage('push image to dockerhub') {
            steps {
                sh  "docker tag myflaskapp satish8380/myflaskapp:latest"
                sh "docker login -u satish8380 -p Satdip@#83"
                sh "docker push satish8380/myflaskapp:latest"
               
                }

            }
                
         stage('deploy application on host') {
            steps {
               sh "docker-compose down -d"
               sh "docker-compose up -d"

            }
        }    
}
}


**CI/CD Workflow**
Any changes pushed to the Git repository trigger Jenkins to build and deploy the Flask app.
Jenkins runs the pipeline defined in the jenkins/ directory.
The app is built and deployed in a Docker container on the AWS EC2 instance.

**reference:**
https://www.youtube.com/watch?v=AaVO1Mvr3q4&ab_channel=TrainWithShubham



