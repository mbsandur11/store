pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/mbsandur11/store.git'
        APP_DIR = '/store/app' // Update this to your desired directory
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the GitHub repository
                git branch: 'main', url: https://github.com/mbsandur11/store.git
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install necessary dependencies
                sh """
                cd store
                pip3 install -r requirements.txt
                """
            }
        }

        stage('Run Application') {
            steps {
                // Run the application
                sh """
                cd store
                nohup python3 app.py --host=0.0.0.0 --port=5000 &
                """
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed.'
        }
    }
}
