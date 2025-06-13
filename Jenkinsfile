// Define a global flag (optional)
flag = true

pipeline {
    agent any
    
    // Global environment variables (accessible in ALL stages)
    environment {
        URL_VERSION = "1.3.0"                  // Hardcoded value
        BUILD_NOTE  = "Prod-Ready"             // Static value
        IS_FLAGGED  = "${flag}"                // Reference Groovy variable
        CREDENTIALS = credentials('AWS_ACCESS_KEY_ID')  // Jenkins credentials
    }

    stages {
        stage('Build') {
            // Stage-specific environment variable
            environment {
                STAGE_SPECIFIC = "build-${env.BUILD_ID}"
            }
            steps {
                echo 'Building the project...'
                echo "Using global URL_VERSION: ${env.URL_VERSION}"
                echo "Stage-specific var: ${env.STAGE_SPECIFIC}"
                echo "Flag status: ${env.IS_FLAGGED}"
                sh 'echo "Build note: $BUILD_NOTE"'  // Access in shell script
            }
        }

        stage('Test') {
            when {
                // Combined conditions: flag == true AND (branch is main OR RUN_TESTS env var set)
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
                echo "AWS Key: ${env.CREDENTIALS}"  // Securely injected
            }
        }

        stage('Deploy') {
            when {
                // Run only if previous stages succeeded AND branch is main
                allOf {
                    expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
                    branch 'main'
                }
            }
            environment {
                TARGET_ENV = "production"  // Deploy-specific variable
            }
            steps {
                echo 'Deploying Project'
                echo "Target: ${env.TARGET_ENV}, Version: ${env.URL_VERSION}"
            }
        }
    }

    post {
        always {
            echo "Post build condition running (always executes)"
            echo "Build completed for version ${env.URL_VERSION}"
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
