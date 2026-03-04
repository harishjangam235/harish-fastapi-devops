pipeline {
agent any

```
environment {
    SONAR_HOST_URL = "http://localhost:9000"
    SONAR_TOKEN = "sqp_0c5b73678bcf1c5820e92e1f55b527a2947de7d7"
}

stages {

    stage('Checkout Code') {
        steps {
            git branch: 'main', url: 'https://github.com/harishjangam235/harish-fastapi-devops.git'
        }
    }

    stage('SonarQube Scan') {
        steps {
            sh """
            echo Running SonarQube Analysis

            sonar-scanner \
            -Dsonar.projectKey=fastapi-devops \
            -Dsonar.sources=. \
            -Dsonar.host.url=$SONAR_HOST_URL \
            -Dsonar.login=$SONAR_TOKEN
            """
        }
    }

    stage('Build') {
        steps {
            sh "echo Building application"
        }
    }

    stage('Deploy') {
        steps {
            sh "echo Deployment completed"
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
