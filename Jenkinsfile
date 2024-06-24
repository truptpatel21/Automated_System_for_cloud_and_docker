pipeline {
    agent any
    parameters {
        choice(name: 'RESOURCE_TYPE', choices: ['ec2', 's3', 'lambda', 'vpc'], description: 'Select the AWS resource to create')
    }
    environment {
        AWS_CREDENTIALS_ID = 'aws-credentials-id'  // Make sure this ID matches the one you set in Jenkins
        GIT_CREDENTIALS_ID = 'github-credentials-id'
        GIT_REPO_URL = 'https://github.com/truptpatel21/Automated_System_for_cloud_and_docker.git'
        TERRAFORM_DIR = 'TerraformInstance'
    }
    stages {
        stage('Checkout') {
            steps {
                git credentialsId: "${env.GIT_CREDENTIALS_ID}", url: "${env.GIT_REPO_URL}"
            }
        }
        stage('Terraform Init') {
            steps {
                dir("${env.TERRAFORM_DIR}/${params.RESOURCE_TYPE}") {
                    withCredentials([usernamePassword(credentialsId: env.AWS_CREDENTIALS_ID, passwordVariable: 'AWS_SECRET_ACCESS_KEY', usernameVariable: 'AWS_ACCESS_KEY_ID')]) {
                        bat '''
                            terraform init
                        '''
                    }
                }
            }
        }
        stage('Terraform Plan') {
            steps {
                dir("${env.TERRAFORM_DIR}/${params.RESOURCE_TYPE}") {
                    withCredentials([usernamePassword(credentialsId: env.AWS_CREDENTIALS_ID, passwordVariable: 'AWS_SECRET_ACCESS_KEY', usernameVariable: 'AWS_ACCESS_KEY_ID')]) {
                        bat '''
                            terraform plan
                        '''
                    }
                }
            }
        }
        stage('Terraform Apply') {
            steps {
                dir("${env.TERRAFORM_DIR}/${params.RESOURCE_TYPE}") {
                    withCredentials([usernamePassword(credentialsId: env.AWS_CREDENTIALS_ID, passwordVariable: 'AWS_SECRET_ACCESS_KEY', usernameVariable: 'AWS_ACCESS_KEY_ID')]) {
                        bat '''
                            terraform apply -auto-approve
                        '''
                    }
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
