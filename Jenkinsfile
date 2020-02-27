pipeline {
    agent {docker {image 'windows_typhoon:licensed-typhoon'}}

    stages {
        stage('build') {
            steps {
                 bat 'set'
            }
        }
    }
}


/*pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                bat 'docker container rm -f windows_typhoon_container_tmp'
                bat 'docker run -it -d --name windows_typhoon_container_tmp windows_typhoon:licensed-typhoon'
                bat 'docker exec -i windows_typhoon_container_tmp typhoon-python.cmd -m pytest --alluredir=report --clean-alluredir --log-cli-level=INFO "C:/Program Files/Typhoon HIL Control Center 2019.4 sp2/examples/scripts/basic model/test_model_basic.py"'
                //bat 'docker exec -i windows_typhoon_container_tmp cmd /c "set"'
            }
        }
    }
}*/