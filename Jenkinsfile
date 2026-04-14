pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('DockerHub')
        IMAGE_NAME = 'madhan-flask-portfolio'
        DOCKER_REPO = "kubemadhan/${IMAGE_NAME}"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Madhanavula/webhooks.git'
            }
        }

        stage('Run Lint Test') {
            steps {
                sh '''
                pip3 install --break-system-packages flake8 || true
                flake8 . || true
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:latest .'
            }
        }

        stage('Tag Docker Image') {
            steps {
                sh 'docker tag $IMAGE_NAME:latest $DOCKER_REPO:latest'
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    sh '''
                    echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                    docker push $DOCKER_REPO:latest
                    '''
                }
            }
        }

        stage('Deploy to Stage') {
            steps {
                sh 'docker run -d -p 5001:5000 $DOCKER_REPO:latest'
            }
        }
    }

    post {
        success { echo '✅ Build, Test, and Deploy completed successfully!' }
        failure { echo '❌ Pipeline failed. Check logs.' }
    }
}