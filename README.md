### Setup Project: ###

### Install pip3 for python 3: ###
* sudo apt-get install python3-pip

### Install VirtualEnvWrapper: ###
* sudo pip install virtualenv virtualenvwrapper

### Install MYSQL: ###
* sudo apt-get update
* sudo apt-get install python-pip python-dev mysql-server libmysqlclient-dev
* sudo mysql_install_db
* sudo mysql_secure_installation*

### Virtual Env: ###
* Open Terminal and type:
* cd
* nano .bash.rc
* export WORKON_HOME=$HOME/.virtualenvs
* source /usr/local/bin/virtualenvwrapper.sh

### Restart Terminal and write: ###
* mkvirtual ps --python=python3

### Install inside Env: ###
* pip3 install django mysqlclient

### Database: ###
* mysql ---user=root -p
* CREATE DATABASE ps;
* GRANT all privileges on ps.* to root@localhost;
* exit;

### Deploying: ###
* login to google app engine account
* Create New Project
* Create New mysql Instance
* Make sure you provide your current public ip address (just google what's my ip) so that you can access mysql on your local machine.
* Create new user with password (password should be same as in your settings.py user database setting).
* open terminal and type: mysql -u pssukhwani -h 35.200.231.220 -p
* hit enter and type the password (password of the user you just created)
* create new database
* GRANT ALL PRIVILEGES ON ps.* TO 'pssukhwani'@'%' WITH GRANT OPTION;
* SOURCE "location of db without quotes"
* Download And install gcloud:
    * ./gcloud install.sh
    * ./bin/gcloud init
    * ./bin/gcloud config set app/use_deprecated_preparation True
    * ./bin/gcloud app deploy
