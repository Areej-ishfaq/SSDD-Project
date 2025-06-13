pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building the project...'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying Project'
            }
        }
    }

    // Post-build actions
    post {
        always {
            echo 'Post build condition running (always executes)'
        }
        
        success {
            echo 'Build succeeded!'
        }
        
        failure {
            echo 'Post Action: Build failed!'
        }
        
        unstable {
            echo 'Build is unstable!'
        }
    }
}

