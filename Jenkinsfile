// Define flag properly to avoid memory leak warning
def flag = true

pipeline {
    agent any
    
    // Global environment variables
    environment {
        URL_VERSION = "1.3.0"
        BUILD_NOTE  = "Prod-Ready"
        IS_FLAGGED  = "${flag}"
        // Remove credentials() if not properly configured in Jenkins
        // AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID') 
    }

    stages {
        stage('Build') {
            environment {
                STAGE_SPECIFIC = "build-${env.BUILD_ID}"
            }
            steps {
                echo 'Building the project...'
                echo "Using global URL_VERSION: ${URL_VERSION}"
                echo "Stage-specific var: ${STAGE_SPECIFIC}"
                echo "Flag status: ${IS_FLAGGED}"
                sh 'echo "Build note: $BUILD_NOTE"'
            }
        }

        stage('Test') {
            when {
                allOf {
                    expression { flag == true }
                    anyOf {
                        branch 'main'
                        environment name: 'RUN_TESTS', value: 'true'
                    }
                }
            }
            steps {
                echo 'Testing Project'
                // echo "AWS Key: ${AWS_ACCESS_KEY_ID}"  // Comment out until credentials are set up
            }
        }

        stage('Deploy') {
            when {
                allOf {
                    expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
                    branch 'main'
                }
            }
            environment {
                TARGET_ENV = "production"
            }
            steps {
                echo 'Deploying Project'
                echo "Target: ${TARGET_ENV}, Version: ${URL_VERSION}"
            }
        }
    }

    post {
        always {
            echo "Post build condition running (always executes)"
            echo "Build completed for version ${URL_VERSION}"
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
