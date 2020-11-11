pipeline {
    if(env.BRANCH_NAME == 'master'){
        agent { docker { image 'python:3.5.1' } }
        stages {
            stage('build') {
                steps {
                    sh 'python --version'

                }
            }
        }

    stage('Post: CleanWorkspace') {
            agent any
            steps {
                cleanWs()
        }
    }
    }
}