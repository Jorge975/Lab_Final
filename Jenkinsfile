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
						stage('Install requirements') {
							steps {
								script {
									sh 'apt-get update && apt-get install -y libmariadb-dev-compat'
									sh 'apt-get update && apt-get install -y pkg-config'
									sh 'apt-get update && apt-get install -y build-essential'
									sh 'apt-get update && apt-get install -y virtualenv'
									sh 'virtualenv venv && . venv/bin/activate'
            								sh 'python -m pip install -r requirements_venv.txt --user --no-cache'
									sh '. coverage run -m pytest'
									sh 'coverage report -m'
        							}
							}
						}
						stage('Tests & Linting') {
							steps {
								script {
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
