pipeline {
    agent any

    stages {
        stage('Checkout Code From Git') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/SammyEiei/TTB-Spark-Test.git'
            }
        }

        stage('Run Test Automate') {
            steps {
                sh '''
                    apt-get install -y python3 python3-pip chromium chromium-driver 2>/dev/null || true
                    python3 -m pip install -r requirements.txt --break-system-packages
                    python3 -m pytest test_login.py test_api.py -v --junitxml=result.xml
                '''
            }
        }

        stage('Send Result To Jenkins') {
            steps {
                junit 'result.xml'
            }
        }
    }

    post {
        always {
            echo "Pipeline finished — check Test Results tab in Jenkins"
        }
        success {
            echo "All tests passed!"
        }
        failure {
            echo "Some tests failed. Check the report."
        }
    }
}
