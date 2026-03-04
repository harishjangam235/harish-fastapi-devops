pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/harishjangam235/harish-fastapi-devops.git'
            }
        }

        stage('SonarQube Scan') {
            steps {
                echo "Running SonarQube Analysis"
            }
        }

        stage('Build') {
            steps {
                echo "Building FastAPI Application"
            }
        }

        stage('Upload to Nexus') {
            steps {
                echo "Uploading artifact to Nexus"
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                sudo systemctl restart fastapi
                '''
            }
        }
    }
}
