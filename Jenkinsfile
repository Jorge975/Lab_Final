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
							args '--user admin'
						}
					}
					stages {
						stage('Install requirements') {
							steps {
								script {
            						sh 'apt-get update && apt-get install -y pkg-config'
            						sh 'python -m pip install -r requirements.txt --user --no-cache'
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