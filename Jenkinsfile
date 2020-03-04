pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                bat 'dir'
                bat 'echo %APPDATA%'
                bat 'typhoon-python generateAPickle.py'
            }
        }
    }
    post {
        always { archiveArtifacts artifacts: 'tmp_pickle.pkl', fingerprint: true }
    }
}

/*docker run -d -t -w "C:/Program Files (x86)/Jenkins/workspace/stJenkinsDockerPipeline_master_3/" ^
    -v "C:/Program Files (x86)/Jenkins/workspace/stJenkinsDockerPipeline_master_3/:C:/Program Files (x86)/Jenkins/workspace/stJenkinsDockerPipeline_master_3/" ^
    -v "C:/Program Files (x86)/Jenkins/workspace/stJenkinsDockerPipeline_master_3@tmp/:C:/Program Files (x86)/Jenkins/workspace/stJenkinsDockerPipeline_master_3@tmp/" ^
    -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** ^
    -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** ^
    windows_typhoon:licensed-typhoon cmd.exe

    --detach , -d		Run container in background and print container ID
    --tty , -t		Allocate a pseudo-TTY
    --workdir , -w		Working directory inside the container
    --volume , -v		Bind mount a volume
    --env , -e		Set environment variables

*/

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