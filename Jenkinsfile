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
                script {
                    if (isUnix()) {
                        sh 'pip install -r requirements.txt'
                    } else {
                        bat 'pip install -r requirements.txt'
                    }
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python -m unittest discover'
                    } else {
                        bat 'python -m unittest discover'
                    }
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'docker build -t flask_app .'
                    } else {
                        bat 'docker build -t flask_app .'
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'docker run -d -p 5000:5000 flask_app'
                    } else {
                        bat 'docker run -d -p 5000:5000 flask_app'
                    }
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
        success {
            echo 'Build completed successfully!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
