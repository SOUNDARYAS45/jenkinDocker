pipeline {
    agent any

    environment {
        IMAGE_NAME = "myapp"
        DEV_PORT = "5002"    // Host port for dev container
        TEST_PORT = "5003"   // Host port for test container
    }

    stages {
        stage('Cleanup') {
            steps {
                echo "Stopping and removing previous containers..."
                sh """
                docker rm -f ${IMAGE_NAME}_dev || true
                docker rm -f ${IMAGE_NAME}_test || true
                """
            }
        }

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/SOUNDARYAS45/jenkinDocker.git'
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
                -p ${DEV_PORT}:5000 -e ENV=dev ${IMAGE_NAME}:latest
                """
            }
        }

        stage('Run Test Container') {
            steps {
                echo "Running test environment..."
                sh """
                docker run -d --name ${IMAGE_NAME}_test \
                -p ${TEST_PORT}:5000 -e ENV=test ${IMAGE_NAME}:latest
                """
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully! Dev and Test containers are running."
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}
