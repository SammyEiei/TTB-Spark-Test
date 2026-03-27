pipeline {
    agent any

    environment {
        PYTHON_ENV = 'venv'
    }

    stages {
        stage('Checkout Code From Git') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/SammyEiei/TTB-Spark-Test.git'
            }
        }

        stage('Setup Environment') {
            steps {
                sh """
                    python3 -m venv ${PYTHON_ENV}
                    . ${PYTHON_ENV}/bin/activate
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run Test Automate') {
            steps {
                sh """
                    . ${PYTHON_ENV}/bin/activate
                    mkdir -p reports
                    pytest test_login.py test_api.py \\
                        --junitxml=reports/test-results.xml \\
                        --html=reports/test-report.html \\
                        --self-contained-html \\
                        -v
                """
            }
        }

        stage('Send Result To Jenkins') {
            steps {
                junit 'reports/test-results.xml'

                archiveArtifacts artifacts: 'reports/test-report.html',
                                 allowEmptyArchive: true

                publishHTML(target: [
                    reportDir: 'reports',
                    reportFiles: 'test-report.html',
                    reportName: 'Test Automation Report',
                    keepAll: true,
                    alwaysLinkToLastBuild: true
                ])
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
        success {
            echo 'All tests passed successfully!'
        }
        failure {
            echo 'Some tests failed. Please check the report.'
        }
        cleanup {
            cleanWs()
        }
    }
}
