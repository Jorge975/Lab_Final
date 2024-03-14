pipeline {
	agent any
	stages {
		stage('Checkout') {
			parallel {
				stage('Install Data') {
					agent {
						docker { image '3.12-slim' }
					}
					steps {
                        dir('reto_final_python') {
                            sh """
								echo 'Image installed:' python --version
								echo 'Installation Dates...'
								pip install -r requirements.txt -r requirements_venv.txt
								"""
                        }
						
					}
				}
				stage('Validation tests and coverage') {
					steps {
						dir('reto_final_python') {
                            sh """ 
								pytest --cov=tests --cov=app
								coverage report -m
								"""
                        }
					}
				}
				stage('Linting'){
					steps {
						dir('reto_final_python') {
							sh 'flake8'
						}
					}
				}
				stage('Build Image') {
					agent any
					steps {
						dir('reto_final_python') {
							sh 'docker build -t mi_image -f Dockerfile .'
						}
					}
				}
			}
		}
		stage('Login') {
			environment { DOCKERHUB_CREDENTIALS = credentials('jorge-dockerhub')}
			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}	
		}
		stage('Push Image to Docker Hub') {         
			steps{                            
				sh """
					sudo docker push mi_image
					echo 'Push Image Completed'
					"""
      		}           
    	}
	}	
}