pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('build') {
            steps {
                cmd 'python --version'
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