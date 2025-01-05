pipeline {
    agent any
    stages {
        stage('Prepare Environment') {
            steps {
                script {
                    echo "Creating Virtual Environment and Installing Dependencies..."
                    bat '''
                        python -m venv venv
                        venv\\Scripts\\activate && pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    echo "Running tests and Generating Reports..."
                    bat '''
                        venv\\Scripts\\activate && pytest --junitxml=reports/results.xml --html=reports/report.html
                    '''
                }
            }
        }
    }
    post {
        always {
            echo "Archiving and Publishing Reports..."
            archiveArtifacts artifacts: 'reports/*.xml, reports/*.html', fingerprint: true
            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Test Report'
            ])
        }
    }
}
