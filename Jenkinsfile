pipeline {
	agent any
	environment { DOCKERHUB_CREDENTIALS = credentials('jorge-dockerhub')}
	stages {
		stage('Checkout') {
			parallel {
				stage('Install Data') {
					agent {
						docker { image 'python:3.12.1' }
					}
					steps {
                        dir('reto_final_python') {
                            sh 'echo "Image installed: " python --version'
                            sh 'echo "Installation Dates..."'
                            sh 'pip install -r requirements.txt -r requirements_venv.txt'
                        }
						
					}
				}
				stage('Validation tests and coverage') {
					steps {
						dir('reto_final_python') {
                            sh 'pytest --cov=tests --cov=app'
							sh 'coverage report -m'
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
		stage('Login') {
			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}
		stage('Push Image to Docker Hub') {         
			steps{                            
				sh 'sudo docker push mi_image'
				sh 'echo "Push Image Completed"'      
      		}           
    	}
	}
}