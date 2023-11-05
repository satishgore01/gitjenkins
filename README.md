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

git clone <repository-url>

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

**CICD-PIPELINE**

