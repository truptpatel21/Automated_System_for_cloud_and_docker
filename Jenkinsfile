pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/truptpatel21/Automated_System_for_cloud_and_docker.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Ensure Python is in the PATH
                bat 'python --version'
                // Install required Python packages
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // Run your test commands here
                bat 'python -m unittest discover tests'
            }
        }
        stage('Build Docker Image') {
            steps {
                // Ensure Docker is installed and in the PATH
                bat 'docker --version'
                // Build Docker image
                bat 'docker build -t flask-app .'
            }
        }
        stage('Deploy') {
            steps {
                // Deployment steps
                bat 'docker run -d -p 5000:5000 flask-app'
            }
        }
    }
    post {
        always {
            cleanWs()
        }
        failure {
            echo 'Build failed!'
        }
    }
}
