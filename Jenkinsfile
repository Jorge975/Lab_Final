pipeline {
	agent any
	environment { 
		DOCKERHUB_CREDENTIALS = credentials('jorge-dockerhub')
		IMAGENAME = "jorge/reto_final_python"
		DOCKERIMAGE = ''
		}
	stages {
		stage('Installation') {
			parallel {
				stage('Build Docker Image') {
					steps {
						sh 'docker build -t reto_final_python . '
					}
				}
				stage('Test programm') {
					agent {
						docker {
							image 'python:3.11-slim'
						}
					}
					stages {
						stage('Install requirements') {
							steps {
								dir('reto_final_python') {
									sh """
										sudo pip3 install virtualenv
										virtualenv .venv
										source .venv/bin/activate
										pip install -r requirements.txt -r requirements_venv.txt
										"""
								}
							}
						}
						stage('Tests & Linting') {
							steps {
								sh """
								pytest --cov=tests --cov=app
								coverage report -m
								flake8 .
								"""
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
					docker tag reto_final_python $IMAGENAME
					docker push $IMAGENAME

				"""
			}
		}
	}	
}