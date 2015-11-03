# ambitserver
Python Ambit Server - Set up for CentOS 

###Linux environment set up

`yum install pip`

`yum install python`

`yum install python-devel gcc`

UWSGI, in order to support websockets must have libffi-devel installed. In order to build UWSGI with SSL we need to first install few openssl python libraries. These have a dependency on some libraries that you have to install through yum first.  

`sudo yum install openssl-devel libffi-devel python-cffi`

`pip install pyopenssl ndg-httpsclient pyasn1`

###Initialize virtual environment

`pip install virtualenv`

`virtualenv .venv`

`source .venv/bin/activate`

`pip install -r requirements.txt`

###Launch the app

.venv/bin/uwsgi --http 0.0.0.0:8000 --http-websockets --master  --threads 16 --wsgi startServer:app -H .venv/


