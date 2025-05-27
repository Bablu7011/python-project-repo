pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main', 
                url: 'https://github.com/Bablu7011/python-project-repo.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    # Install Python and pip via apt (system packages)
                    sudo apt update -y
                    sudo apt install -y python3 python3-pip python3-venv
                    
                    # Create and activate virtual environment
                    python3 -m venv venv
                    . venv/bin/activate
                    
                    # Upgrade pip within the virtual environment
                    pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    . venv/bin/activate
                    pip install -r requirements.txt || pip install pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest tests/ -v
                '''
            }
        }
    }

    post {
        always {
            cleanWs()  // Clean up workspace after build
        }
    }
}