**CI/CD Flask App Project with AWS, Git, Jenkins, and Docker**
This project demonstrates a continuous integration and continuous deployment (CI/CD) pipeline for a Flask web application using Jenkins. 
The CI/CD pipeline includes AWS instance creation, Git version control, Jenkins for automation, and Docker for containerization.

**Prerequisites**
Before setting up the CI/CD pipeline for this project, ensure you have the following prerequisites in place:
1)Ubuntu 20.04 server with SSH access.
2)AWS account and necessary IAM permissions.
3)Git installed on your local machine and Jenkins server.
4)Docker and Docker Compose installed on your Ubuntu server.

**app/:** Contains your Flask application code.
**jenkins/**: Contains Jenkins pipeline configuration files.
**Dockerfile:** Defines how to build the Docker image for your Flask app.
**docker-compose.yml:** Configuration for running your app in Docker containers.

**STEP1: **

**Setting up AWS**
Create an AWS EC2 instance with Ubuntu 20.04.
SSH into your AWS instance.
Configure your AWS CLI with your credentials.

**STEP2:**

**Setting up Git**
Install Git on your local machine.
**Clone this repository.**

git clone https://github.com/satishgore01/gitjenkins.git

**Configure Git with your name and email.**
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"

**STEP3:**
**Setting up Jenkins**
Install Jenkins on your server following the official documentation.
Install necessary Jenkins plugins (e.g., Git, Docker, AWS).
Create a Jenkins pipeline job using the configuration in the jenkins/ folder

**STEP4:**
**Setting up Docker**
Install Docker and Docker Compose on your Ubuntu server following the official documentation.

**STEP5: create dockerfile and docker compose-file**
  check execting docker file which is alreday added in git repo.

**Step6**
      **Jenkins configuration**

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

**STEP7:
     common errors:**
        check docker is running or not.
	jenkins user added or not in docker group
        git resgistry and credentials


**CI/CD Workflow**
Any changes pushed to the Git repository trigger Jenkins to build and deploy the Flask app.
Jenkins runs the pipeline defined in the jenkins/ directory.
The app is built and deployed in a Docker container on the AWS EC2 instance.

**reference:**
https://www.youtube.com/watch?v=AaVO1Mvr3q4&ab_channel=TrainWithShubham



