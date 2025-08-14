pipeline {
  agent any
  options { timestamps() }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Set up Python venv') {
      steps {
        script {
          if (isUnix()) {
            sh '''
              python3 -m venv venv
              . venv/bin/activate
              pip install --upgrade pip
              pip install -r requirements.txt
            '''
          } else {
            bat '''
              python -m venv venv
              call venv\\Scripts\\activate
              pip install --upgrade pip
              pip install -r requirements.txt
            '''
          }
        }
      }
    }

    stage('Django checks & migrate') {
      steps {
        script {
          if (isUnix()) {
            sh '''
              . venv/bin/activate
              python manage.py check
              python manage.py migrate --noinput
            '''
          } else {
            bat '''
              call venv\\Scripts\\activate
              python manage.py check
              python manage.py migrate --noinput
            '''
          }
        }
      }
    }

    stage('Tests') {
      steps {
        script {
          if (isUnix()) {
            sh '. venv/bin/activate && python manage.py test -v 2'
          } else {
            bat 'call venv\\Scripts\\activate && python manage.py test -v 2'
          }
        }
      }
    }
  }
}
