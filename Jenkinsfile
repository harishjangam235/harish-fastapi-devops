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
            script {
                def scannerHome = tool 'sonar-scanner'
                withSonarQubeEnv('sonarqube') {
                    sh """
                    ${scannerHome}/bin/sonar-scanner \
                    -Dsonar.projectKey=fastapi-devops \
                    -Dsonar.sources=. \
                    -Dsonar.host.url=http://3.109.33.186:9000
                    """
                }
            }
        }
    }

    stage('Build') {
        steps {
            sh '''
            echo "Creating artifact"
            zip -r fastapi-app.zip .
            '''
        }
    }

    stage('Upload to Nexus') {
        steps {
            nexusArtifactUploader(
                nexusVersion: 'nexus3',
                protocol: 'http',
                nexusUrl: '3.109.33.186:8081',
                groupId: 'devops',
                version: '1.0',
                repository: 'fastapi-devops',
                credentialsId: 'nexus-creds',
                artifacts: [
                    [
                        artifactId: 'fastapi-app',
                        classifier: '',
                        file: 'fastapi-app.zip',
                        type: 'zip'
                    ]
                ]
            )
        }
    }

    stage('Deploy') {
        steps {
            sh '''
            echo "Deployment complete"
            '''
        }
    }

}
}
