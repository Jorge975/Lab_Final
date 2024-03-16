
pipeline {
	agent any
	environment { 
		DOCKERHUB_CREDENTIALS = credentials('admin-dockerhub')
		IMAGENAME = "admin/reto_final_python"
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
							args '-u root --privileged'
						}
					}
					stages {
						stage('Linting') {
							steps {
								dir('reto_final_python'){
									sh """
									pip install coverage
									coverage run -m pytest
									coverage report -m
									"""
									sh 'flake8'
								}
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
