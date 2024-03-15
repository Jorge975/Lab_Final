pipeline {
	agent any
	environment { 
		DOCKERHUB_CREDENTIALS = credentials('jorge-dockerhub')
		IMAGENNAME = "jorge/reto_final_python"
		DOCKERIMAGE = ''
		}
	stages {
		stage('Installation') {
			parallel {
				stage('Build Docker Image') {
					steps {
						script {
							DOCKERIMAGE = docker.build IMAGENNAME
						}
					}
				}
				stage('Test programm') {
					agent {
						docker {
							image 'python:3.12-slim'
						}
					}
					stages {
						stage('Install requirements') {
							sh 'pip install -r requirements_venv.txt .'
						}
						stage('Tests & Linting') {
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
		stage('Login & Push ') {
			steps {
				sh """
					echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
					docker push $DOCKERIMAGE
				"""
			}
		}
	}	
}