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
                sh '''
                echo "Running SonarQube Scan"

                sonar-scanner \
                -Dsonar.projectKey=fastapi-devops \
                -Dsonar.sources=. \
                -Dsonar.host.url=http://localhost:9000 \
                -Dsonar.login=sqp_0c5b73678bcf1c5820e92e1f55b527a2947de7d7
                '''
            }
        }

        stage('Build') {
            steps {
                sh 'echo Building application'
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo Deployment complete'
            }
        }

    }
}
