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
        sh "docker run -d --name myapp_dev -p 5002:5000 -e ENV=dev myapp:latest || true"
    }
}

stage('Run Test Container') {
    steps {
        echo "Running test environment..."
        sh "docker run -d --name myapp_test -p 5003:5000 -e ENV=test myapp:latest || true"
    }
}


    post {
        success { echo "Docker containers started successfully!" }
        failure { echo "Pipeline failed!" }
    }
}
