pipeline {
    agent any
    
    tools {
        maven 'Maven'  // Name of Maven tool configured in Jenkins
    }
    
    environment {
        // Global environment variables
        NEW_VERSION = '1.3.0'
        BUILD_TYPE = 'Production'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building Project'
                echo "Building version ${NEW_VERSION}"
                echo "Build type: ${BUILD_TYPE}"
                
                // Maven build command (fixed from "nwn install")
                sh "mvn clean install"
                
                // Archive the built artifacts
                archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
            }
            
            post {
                success {
                    echo 'Build stage completed successfully!'
                }
                failure {
                    echo 'Build stage failed!'
                }
            }
        }

        stage('Test') {
            when {
                expression { env.BUILD_TYPE == 'Production' }
            }
            steps {
                echo 'Running Tests'
                sh "mvn test"
                
                // Store test results
                junit 'target/surefire-reports/*.xml'
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo 'Deploying Application'
                echo "Deploying version ${NEW_VERSION} to ${BUILD_TYPE}"
                
                // Add deployment commands here
                // sh "./deploy.sh"
            }
        }
    }

    post {
        always {
            echo "Pipeline completed for ${NEW_VERSION}"
            cleanWs()  // Clean workspace after build
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
