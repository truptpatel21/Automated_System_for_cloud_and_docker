pipeline {
    agent any
    parameters {
        choice(name: 'RESOURCE_TYPE', choices: ['ec2', 's3', 'lambda', 'vpc'], description: 'Select the AWS resource to create')
    }
    environment {
        AWS_CREDENTIALS_ID = 'b6493d48-501b-4e5a-81f4-ff3b0a3babce'  // Replace with your actual AWS_CREDENTIALS_ID
        GIT_REPO_URL = 'https://github.com/truptpatel21/Automated_System_for_cloud_and_docker.git'
        TERRAFORM_DIR = 'TerraformInstance'
    }
    stages {
        stage('Checkout') {
            steps {
                git credentialsId: 'your-github-credentials-id', url: "${env.GIT_REPO_URL}"
            }
        }
        stage('Terraform Init') {
            steps {
                dir("${env.TERRAFORM_DIR}/${params.RESOURCE_TYPE}") {
                    withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: "${env.AWS_CREDENTIALS_ID}"]]) {
                        sh 'terraform init'
                    }
                }
            }
        }
        stage('Terraform Plan') {
            steps {
                dir("${env.TERRAFORM_DIR}/${params.RESOURCE_TYPE}") {
                    withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: "${env.AWS_CREDENTIALS_ID}"]]) {
                        sh 'terraform plan'
                    }
                }
            }
        }
        stage('Terraform Apply') {
            steps {
                dir("${env.TERRAFORM_DIR}/${params.RESOURCE_TYPE}") {
                    withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: "${env.AWS_CREDENTIALS_ID}"]]) {
                        sh 'terraform apply -auto-approve'
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
