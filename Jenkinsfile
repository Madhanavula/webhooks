pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('DockerHub')
        IMAGE_NAME = 'theshubhamgour/flask-portfolio'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/theshubhamgour/flask-portfolio.git'
            }
        }

        stage('Run Lint Test') {
            steps {
                sh 'pip3 install --break-system-packages flake8'
                sh 'flake8 . || true'
                  }
            }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$BUILD_NUMBER .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                    sh 'docker push $IMAGE_NAME:$BUILD_NUMBER'
                }
            }
        }

        stage('Deploy to Stage') {
            steps {
                sh 'docker run -d -p 5000:5000 $IMAGE_NAME:$BUILD_NUMBER'
            }
        }
    }

    post {
        success { echo '✅ Build, Test, and Deploy completed successfully!' }
        failure { echo '❌ Pipeline failed. Check logs.' }
    }
}
