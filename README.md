# ambitserver
Python Ambit Server - Set up for CentOS 

###Linux environment set up

`yum install gcc`

'yum install python-devel'

'yum install pip'

'yum install python'

###Initialize virtual environment

`pip install virtualenv`

`virtualenv .venv`

'source .venv/bin/activate'

`pip install -r requirements.txt`

###Launch the app

`.venv/bin/uwsgi --http localhost:8000 --http-websockets --master  --threads 16 --wsgi startServer:app --python-autoreload 1 -H .venv/`

