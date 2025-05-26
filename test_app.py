import app

def test_add():
    assert app.add(2, 3) == 5
pipeline {
    agent any
    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/yourusername/my-python-app.git'
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
