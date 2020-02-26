pipeline {
    agent { docker { image 'windows_typhoon:install-typhoon' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}


/*pipeline{
    agent any

    steps{
        stages ('Compile stage'){
            withMaven(maven: 'maven_3_6_1'){
                sh 'mvn clean compile'
            }
        }

        stages ('Testing stage'){
            withMaven(maven: 'maven_3_6_1'){
                sh 'mvn test'
            }
        }

        stages ('Deployment stage'){
            withMaven(maven: 'maven_3_6_1'){
                sh 'mvn deploy'
            }
        }

    }
}*/