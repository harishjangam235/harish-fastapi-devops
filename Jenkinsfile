pipeline {
agent any

```
environment {
    SONAR_HOST_URL = "http://localhost:9000"
    SONAR_TOKEN = "sqp_0c5b73678bcf1c5820e92e1f55b527a2947de7d7"

    NEXUS_URL = "http://localhost:8081"
    NEXUS_REPO = "fastapi-artifacts"
    NEXUS_USER = "admin"
    NEXUS_PASS = "admin123"
}

stages {

    stage('Checkout Code') {
        steps {
            git branch: 'main', url: 'https://github.com/harishjangam235/harish-fastapi-devops.git'
        }
    }

    stage('SonarQube Scan') {
        steps {
            sh '''
            echo "Running SonarQube Analysis..."

            sonar-scanner \
            -Dsonar.projectKey=fastapi-devops \
            -Dsonar.sources=. \
            -Dsonar.host.url=$SONAR_HOST_URL \
            -Dsonar.login=$SONAR_TOKEN
            '''
        }
    }

    stage('Build') {
        steps {
            sh '''
            echo "Building FastAPI application"
            tar -czf fastapi-app.tar.gz *.py
            '''
        }
    }

    stage('Upload to Nexus') {
        steps {
            sh '''
            echo "Uploading artifact to Nexus..."

            curl -v -u $NEXUS_USER:$NEXUS_PASS \
            --upload-file fastapi-app.tar.gz \
            $NEXUS_URL/repository/$NEXUS_REPO/fastapi-app.tar.gz
            '''
        }
    }

    stage('Deploy Application') {
        steps {
            sh '''
            echo "Deploying FastAPI..."

            pkill -f uvicorn || true
            nohup uvicorn main:app --host 0.0.0.0 --port 8000 &
            '''
        }
    }

}

post {
    success {
        echo "Pipeline executed successfully!"
    }
    failure {
        echo "Pipeline failed!"
    }
}
```

}
