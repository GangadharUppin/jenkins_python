pipeline {
    agent any  // Use any available agent

    environment {
        GIT_REPO = 'https://github.com/GangadharUppin/jenkins_python.git'  // Replace with your repo URL
        GIT_BRANCH = 'master'  // Replace with your branch name
		PYTEST_PATH = r'C:\Users\ACER\AppData\Local\Programs\Python\Python312\Scripts\pytest.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the Git repository
                git url: "${env.GIT_REPO}", branch: "${env.GIT_BRANCH}"
            }
        }

        stage('Execute Code') {
            steps {
                // Run the script or commands to execute the code
                script {
                    // Example: Run a shell script or command
                    bat 'echo "Executing code..."'
                    bat "\"${env.PYTEST_PATH}\" -vs test.py" // Replace with the command to execute your code
                }
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline execution completed.'
        }
    }
}
