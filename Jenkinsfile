pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Bablu7011/python-project-repo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                sudo apt update -y
                sudo apt install -y python3-pip
                pip3 install pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest test_app.py'
            }
        }
    }
}
