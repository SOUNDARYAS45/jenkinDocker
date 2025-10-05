pipeline {
    agent any

    environment {
        IMAGE_NAME = "myapp"
    }

    stages {
        stage('Cleanup') {
            steps {
                echo "Removing previous containers..."
                sh "docker rm -f ${IMAGE_NAME}_dev || true"
                sh "docker rm -f ${IMAGE_NAME}_test || true"
            }
        }

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/SOUNDARYAS45/jenkinDocker'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh "docker build -t ${IMAGE_NAME}:latest ."
            }
        }

        stage('Run Dev Container') {
            steps {
                echo "Running dev environment..."
                sh """
                docker run -d --name ${IMAGE_NAME}_dev \
                -p 5000:5000 -e ENV=dev ${IMAGE_NAME}:latest
                """
            }
        }

        stage('Run Test Container') {
            steps {
                echo "Running test environment..."
                sh """
                docker run -d --name ${IMAGE_NAME}_test \
                -p 5001:5000 -e ENV=test ${IMAGE_NAME}:latest
                """
            }
        }
    }

    post {
        success { echo "Docker containers started successfully!" }
        failure { echo "Pipeline failed!" }
    }
}
