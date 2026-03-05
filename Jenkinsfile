pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/harishjangam235/harish-fastapi-devops.git'
            }
        }

        stage('SonarQube Scan') {
    steps {
        withSonarQubeEnv('sonarqube') {
            sh '''
            sonar-scanner \
            -Dsonar.projectKey=fastapi-devops \
            -Dsonar.sources=.
            '''
        }
    }
}

        stage('Build') {
            steps {
                sh 'echo Building FastAPI application'
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo Deployment complete'
            }
        }

    }
}
