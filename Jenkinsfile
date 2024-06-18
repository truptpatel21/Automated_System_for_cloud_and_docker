pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        APP_DIR = 'Automated System for cloud and Docker'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from the repository
                git url: 'https://github.com/truptpatel21/Automated_System_for_cloud_and_docker.git', branch: 'master'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Set up a Python virtual environment and install dependencies
                    if (fileExists(VENV_DIR)) {
                        sh "rm -rf ${VENV_DIR}"
                    }
                    sh "python3 -m venv ${VENV_DIR}"
                    sh "${VENV_DIR}/bin/pip install -r ${APP_DIR}/requirements.txt"
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run your tests
                    sh "${VENV_DIR}/bin/python -m unittest discover ${APP_DIR}/tests"
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build a Docker image if you are using Docker
                    sh "docker build -t flask-automation-project ."
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Deploy your application
                    // Add your deployment steps here
                    echo "Deploying application..."
                }
            }
        }
    }

    post {
        always {
            cleanWs() // Clean workspace after the build
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
