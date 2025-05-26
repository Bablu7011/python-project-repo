pipeline {
    agent any
    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/Bablu7011/python-project-repo.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install pytest'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest test_app.py'
            }
        }
    }
}
