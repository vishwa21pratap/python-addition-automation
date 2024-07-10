pipeline {
    agent any
    
    environment {
        GIT_REPO = "https://github.com/vishwa21pratap/python-addition-automation.git"
        DOCKERFILE_PATH = "./Dockerfile"  // Path to Dockerfile in your repository
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: "${GIT_REPO}"]]])
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
                    def dockerImage = docker.image('python-addition')
                    dockerImage.run('--rm', 'pytest')
                    currentBuild.result = dockerImage.inside("--rm", "--tty", "--workdir /app", "--entrypoint=''") {
                        sh "pytest"
                    }
                }
            }
        }

        // Add more stages as needed for reporting, deployment, etc.
    }

    post {
        always {
            script {
                junit '**/test-results.xml'
            }
            cleanWs()
        }
    }
}
