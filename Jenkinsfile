pipeline {
    agent {
        docker {
            image 'ubuntu:xenial'
        }
    }

    stages {
        stage('build') {
            steps {
                // sh 'typhoon-python.cmd -m pytest --alluredir=report --clean-alluredir --log-cli-level=INFO "C:/Program Files/Typhoon HIL Control Center 2019.4 sp2/examples/scripts/basic model/test_model_basic.py"'
                sh 'apt update'
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
