pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/yourusername/python-addition-automation.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('python-addition')
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    def app = docker.image('python-addition')
                    app.inside {
                        sh 'pytest'
                    }
                }
            }
        }

        stage('Report Results') {
            steps {
                junit '**/test-results/*.xml'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
