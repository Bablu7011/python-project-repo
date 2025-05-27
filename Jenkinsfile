pipeline {
    agent any

    environment {
        // Customize these as needed
        PYTHON_VERSION = '3.12'
        VENV_DIR = 'venv'
        REQUIREMENTS_FILE = 'requirements.txt'
        TEST_DIR = 'tests'
    }

    stages {
        stage('Setup Environment') {
            steps {
                script {
                    // Clean workspace first
                    cleanWs()
                    
                    // Checkout code
                    checkout scm
                    
                    // Setup Python environment
                    sh """
                        echo "Setting up Python ${PYTHON_VERSION} environment"
                        sudo apt-get update -y
                        sudo apt-get install -y python${PYTHON_VERSION} python${PYTHON_VERSION}-venv
                        
                        python${PYTHON_VERSION} -m venv ${VENV_DIR}
                        . ${VENV_DIR}/bin/activate
                        python -m pip install --upgrade pip
                        
                        # Install dependencies
                        if [ -f "${REQUIREMENTS_FILE}" ]; then
                            pip install -r ${REQUIREMENTS_FILE}
                        else
                            echo "No requirements.txt found, installing pytest"
                            pip install pytest
                        fi
                    """
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    try {
                        sh """
                            . ${VENV_DIR}/bin/activate
                            pytest ${TEST_DIR}/ -v --junitxml=test-results.xml --cov=. --cov-report=xml
                        """
                    } catch (err) {
                        // Tests failed - continue to publish results
                        echo "Tests failed: ${err}"
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
            post {
                always {
                    // Always publish test results
                    junit 'test-results.xml'
                    
                    // Publish coverage if generated
                    script {
                        if (fileExists('coverage.xml')) {
                            publishCoverage adapters: [coberturaAdapter('coverage.xml')]
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            // Archive useful files
            archiveArtifacts artifacts: '**/test-results.xml, **/coverage.xml', allowEmptyArchive: true
            
            // Clean up workspace
            cleanWs()
            
            // Send notifications if needed
            script {
                if (currentBuild.result == 'UNSTABLE') {
                    echo "Tests failed but pipeline continued"
                    // Add notification here (Slack/Email etc)
                } else if (currentBuild.result == 'FAILURE') {
                    echo "Pipeline failed with errors"
                } else {
                    echo "Pipeline succeeded"
                }
            }
        }
    }
}