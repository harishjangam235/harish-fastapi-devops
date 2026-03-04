pipeline {
    agent any

    tools {
        sonarQubeScanner 'sonar-scanner'
    }

    environment {
        SONAR_SERVER = 'SonarQube'
        NEXUS_URL = 'http://localhost:8081'
        NEXUS_REPO = 'fastapi-artifacts'
        NEXUS_USER = 'admin'
        NEXUS_PASS = 'admin123'
    }

    stages {

        stage('Checkout SCM') {
            steps {
                git branch: 'main', url: 'https://github.com/harishjangam235/harish-fastapi-devops.git'
            }
        }

        stage('Checkout Code') {
            steps {
                echo "Code checked out successfully"
            }
        }

        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv("${SONAR_SERVER}") {
                    sh '''
                    sonar-scanner \
                    -Dsonar.projectKey=fastapi-devops \
                    -Dsonar.sources=. \
                    -Dsonar.host.url=http://localhost:9000 \
                    -Dsonar.login=admin
                    '''
                }
            }
        }

        stage('Build') {
            steps {
                echo "Building FastAPI Application"

                sh '''
                echo "Packaging application"
                tar -czf fastapi-app.tar.gz *.py
                '''
            }
        }

        stage('Upload to Nexus') {
            steps {
                echo "Uploading artifact to Nexus"

                sh '''
                curl -v -u ${NEXUS_USER}:${NEXUS_PASS} \
                --upload-file fastapi-app.tar.gz \
                ${NEXUS_URL}/repository/${NEXUS_REPO}/fastapi-app.tar.gz
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                echo "Deploying FastAPI Application"

                sh '''
                pkill -f uvicorn || true
                nohup uvicorn main:app --host 0.0.0.0 --port 8000 &
                '''
            }
        }

    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
