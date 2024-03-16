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
				stage('Test & Coverage') {
					agent {
						docker {
							image 'python:3.11-slim'
							args '-u root --privileged'
						}
					}
					steps {
						dir('reto_final_python') {
							script {
								// Instalar requisitos y ejecutar pruebas
								sh """
								virtualenv venv
								. venv/bin/activate
								pip install -r requirements_venv.txt
								coverage run -m pytest
								coverage report -m
								"""
							}
						}
					}
        		}
				stage('Linting') {
					steps {
						dir('reto_final_python') {
							script {
								// Ejecutar linter
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
					docker tag reto_final_python $IMAGENAME
					docker push $IMAGENAME

				"""
			}
		}
	}	
}
