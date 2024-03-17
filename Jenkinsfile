
pipeline {
	agent any
	environment { 
		DOCKERHUB_CREDENTIALS = credentials('admin-dockerhub')
		IMAGENAME = "jcasillas245a/reto_final_python"
		DOCKERIMAGE = ''
		}
	stages {
		stage('Installation') {
			parallel {
				stage('Build Docker Image') {
					steps {
						sh 'docker build -t docker-imagen -f docker/Dockerfile .'
					}
				}
				stage('Test programm') {
					agent {
						docker {
							image 'python:3.11-slim'
							args '-u root --privileged'
						}
					}
					stages {
						stage('apt install') {
							steps {
								script {
									sh 'apt-get update && apt-get install -y virtualenv'
        						}
							}
						}
						stage('pip install') {
							steps {
								sh 'virtualenv venv && . venv/bin/activate'
								sh 'pip install -r requirements.txt -r requirements_venv.txt'
							}
						}
						stage('Coverage & Test') {
							steps {
								sh 'coverage run -m pytest .'
								sh 'coverage report -m'
							}
						}
						stage('Linting') {
							steps {
								sh 'flake8'
							}
						}
					}
				}
			}
		}
		stage('Login & Push ') {
			when {
                    branch "main/develop"
                }
			steps {
				sh """
					echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
					docker tag docker-image $IMAGENAME
					docker push $IMAGENAME

				"""
			}
		}
	}	
}
