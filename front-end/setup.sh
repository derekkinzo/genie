#!/bin/bash
echo "$(uname)"
if [ "$(uname)" == "Darwin" ]; then
  echo "Creating postgresql user genie with password genie123 on MAC"
  psql postgres < create_user.sql;
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
  echo "checking updates"
  sudo apt update
  sudo apt install python3-pip
  sudo apt-get install postgresql
  sudo apt-get install python-psycopg2
  sudo apt-get install libpq-dev
  echo "Creating postgresql user genie with password genie123 on Linux"
  sudo su postgres < create_user_linux.sh
else
  echo "Operating system not supported"
  exit
fi

echo "creating database tables"
psql postgresql://genie:genie123@localhost:5432 < database.sql

echo "installing virtural env"
pip3 install virtualenv

echo "setup virtual env"
virtualenv .
source bin/activate

echo "installing python3 dependencies"
pip3 install -r requirements.txt

echo "starting server"
bash app.sh
