pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                // Clone the main branch of the repo
                git branch: 'main', url: 'https://github.com/Bablu7011/python-project-repo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Update the system and install required Python tools
                sh 'sudo apt update'
                sh 'sudo apt install python3-pip -y'
                sh 'pip3 install pytest'
            }
        }

        stage('Run Tests') {
            steps {
                // Run pytest on your test file
                sh 'pytest test_app.py'
            }
        }
    }
}
