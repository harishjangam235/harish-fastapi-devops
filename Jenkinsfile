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
                    echo "Running SonarQube Scan"

                    sonar-scanner \
                    -Dsonar.projectKey=fastapi-devops \
                    -Dsonar.sources=. \
                    -Dsonar.host.url=http://localhost:9000
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
