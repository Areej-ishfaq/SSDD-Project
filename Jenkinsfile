pipeline {
    agent any
    
    parameters {
        string(name: 'VERSION_STRING', defaultValue: '', description: 'Custom version to deploy on prod')
        choice(name: 'VERSION_CHOICE', choices: ['1.1.0', '1.2.0', '1.3.0'], description: 'Select version from list')
        booleanParam(name: 'executeTests', defaultValue: true, description: 'Check to execute tests')
    }
    
    environment {
        // Use either the custom string input or selected choice version
        NEW_VERSION = params.VERSION_STRING ?: params.VERSION_CHOICE
        BUILD_TYPE = 'Production'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building Project'
                echo "Building version: ${NEW_VERSION}"
                echo "Build type: ${BUILD_TYPE}"
            }
        }

        stage('Test') {
            when {
                expression { params.executeTests }
            }
            steps {
                echo 'Testing Project'
                echo "Running tests for version: ${NEW_VERSION}"
            }
        }

        stage('Deploy') {
            when {
                expression { params.VERSION_STRING || params.VERSION_CHOICE }
            }
            steps {
                echo 'Deploying Project'
                echo "Deploying version: ${NEW_VERSION} to production"
            }
        }
    }

    post {
        always {
            echo "Pipeline completed for version ${NEW_VERSION}"
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
