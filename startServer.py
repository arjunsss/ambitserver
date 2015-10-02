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
   f = open("test.txt", 'w')
   while True:
      msg = ws.receive()

      if first_message and msg is not None: # the first message should be the sample rate
         #sample_rate = msg
         print(sample_rate)
         first_message = False
         continue
      elif msg is not None:
         audio_as_float_array = numpy.frombuffer(msg)
         isLaughter = doSomething(audio_as_float_array, f)

         if (isLaughter):
            ws.send("Start")
         else:
            ws.send("Stop")
      else:
         break



def doSomething(audio_as_int_array, f):
   if audio_as_int_array.size > 0:
      f.write(audio_as_int_array)
      print(audio_as_int_array)
   return False

if __name__ == '__main__':
    app.run(host='0.0.0.0', threads=16, port=8000)
