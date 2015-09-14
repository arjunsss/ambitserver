#!/usr/bin/env python
from flask import Flask, render_template
from flask.ext.uwsgi_websocket import GeventWebSocket
import numpy

app = Flask(__name__)
ws = GeventWebSocket(app)

@app.route('/audio')
def audio():
   return render_template('audio.html')

@app.route('/')
def index():
  return render_template('index.html')

@ws.route('/websocket')
def webSocket(ws):
   first_message = True
   total_msg = ""
   sample_rate = 0
   count = 0

   while True:
      msg = ws.receive()

      if first_message and msg is not None: # the first message should be the sample rate
         #sample_rate = getSampleRate(msg)
         first_message = False
         continue
      elif msg is not None:
         audio_as_int_array = numpy.frombuffer(msg, 'i2')
         doSomething(audio_as_int_array)
         # Temporarily to test start/stop of laughter detection
         count = count + 1
         if (count % 30 == 0):
            ws.send("Start")
         if (count % 50 == 0):
            ws.send("Stop")
      else:
         break

def doSomething(audio_as_int_array):
	if audio_as_int_array.size > 0:
		print(audio_as_int_array)


if __name__ == '__main__':
    app.run(host='0.0.0.0', threads=16, port=8000)
