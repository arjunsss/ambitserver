# ambitserver
Python Ambit Server - Set up for CentOS 

###Initialize virtual environment

`pip install virtualenv`

`virtualenv .venv`

###Linux environment set up

`yum install gcc`

###Launch the app

`.venv/bin/uwsgi --http localhost:8000 --http-websockets --master  --threads 16 --wsgi startServer:app --python-autoreload 1 -H .venv/`

