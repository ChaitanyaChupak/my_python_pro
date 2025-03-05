pipeline {
    agent any
   
    environment {
        DOCKER_IMAGE = 'my-python-project:latest'
    }
   
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', 
                    url: 'git@github.com:ChaitanyaChupak/my_python_pro.git', 
                    credentialsId: 'your-ssh-key-id'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''#!/bin/bash
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip build pytest
                '''
            }
        }

        stage('Build Wheel') {
            steps {
                sh '''#!/bin/bash
                    source venv/bin/activate
                    python -m build --wheel
                '''
            }
        }
       
        stage('Test') {
            steps {
                sh '''#!/bin/bash
                    source venv/bin/activate
                    pytest tests/
                '''
            }
        }
       
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE} .'
            }
        }
       
        stage('Deploy') {
            steps {
                sh '''#!/bin/bash
                    # Stop and remove the existing container if running
                    docker ps -q --filter "name=my-python-container" | grep -q . && docker stop my-python-container && docker rm my-python-container || true
                    
                    # Run the new container
                    docker run -d --name my-python-container ${DOCKER_IMAGE}
                '''
            }
        }
    }
   
    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}
