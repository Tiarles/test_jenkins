pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                bat 'docker container rm windows_typhoon_container_tmp'
                bat 'docker run -it -d --name windows_typhoon_container_tmp windows_typhoon:licensed-typhoon'
                // sh 'typhoon-python.cmd -m pytest --alluredir=report --clean-alluredir --log-cli-level=INFO "C:/Program Files/Typhoon HIL Control Center 2019.4 sp2/examples/scripts/basic model/test_model_basic.py"'
                bat 'docker exec -i set'
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
