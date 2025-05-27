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
                  sh 'sudo apt update'
                  sh 'sudo apt install python3-pip -y'
                  sh 'pip3 install pytest'  
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest test_app.py'
            }
        }
    }
}
