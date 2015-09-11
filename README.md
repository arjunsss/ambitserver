# ambitserver
python server ambit

1. Initialize virtual environment
pip install virtualenv
virtualenv .venv


2. Launch the app
.venv/bin/uwsgi --http localhost:8000 --http-websockets --master  --threads 16 --wsgi startServer:app --python-autoreload 1 -H .venv/

