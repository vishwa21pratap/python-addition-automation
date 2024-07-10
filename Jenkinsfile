pipeline {
    agent any
    
    environment {
        GIT_REPO = "https://github.com/vishwa21pratap/python-addition-automation.git"
        DOCKERFILE_PATH = "./Dockerfile"  // Path to Dockerfile in your repository
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: "${GIT_REPO}"]]])
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("python-addition", "-f ${DOCKERFILE_PATH} .")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    def testResults = docker.image('python-addition').run('--rm', 'pytest', returnStdout: true).trim()
                    if (testResults.contains("ERRORS") || testResults.contains("FAILED")) {
                        currentBuild.result = 'FAILED'
                        error "Tests failed"
                    } else {
                        currentBuild.result = 'SUCCESS'
                        echo "Tests passed successfully"
                    }
                }
            }
        }

        // Add more stages as needed for reporting, deployment, etc.
    }

    post {
        always {
            cleanWs()
        }
        success {
            echo "Pipeline succeeded! Tests passed."
        }
        failure {
            echo "Pipeline failed! Tests did not pass."
        }
    }
}
