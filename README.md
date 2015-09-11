# ambitserver
python server ambit

###1. Initialize virtual environment

`pip install virtualenv`

`virtualenv .venv`

###2. Linux environment set up

`yum install gcc`

###3. Launch the app

.venv/bin/uwsgi --http localhost:8000 --http-websockets --master  --threads 16 --wsgi startServer:app --python-autoreload 1 -H .venv/

