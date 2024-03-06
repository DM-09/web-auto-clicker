from flask import *
import mouse
import keyboard
import time

app = Flask(__name__)

html = '''
<html>
  <head>
    <!-- Meta -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- import -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
  </head>
    <center>
      <button type="button" class="btn btn-secondary mt-5" onClick='a()'>자동 클릭 시작</button> <br>
      <button type="button" class="btn btn-secondary mt-2" onClick='e()'>강제 종료</button>
    </center>
    <script>
      function a() {
        alert('자동 클릭 시작')
        const xhr = new XMLHttpRequest();
 
        xhr.open('GET', "/auto_click/1", true);
        xhr.send();
        xhr.onload = function() {
          alert("자동 클릭 끝")
        }
      }
      
      function e() {
        const xhr = new XMLHttpRequest();
 
        xhr.open('GET', "/end_click", true);
        xhr.send();
      }
    </script>
  <body>
  </body>
</html>
'''

@app.route('/')
def Main():
  return html

enabled = True

@app.route('/auto_click/<wait>')
def autoClick(wait):
  global enabled
  enabled = True
  while 1:
    if enabled == False: break
    mouse.click()
    time.sleep(float(wait))
  return 'auto click ended'

@app.route('/end_click')
def end():
  global enabled
  enabled = False

def a(evt):
  global enabled
  enabled = False

keyboard.on_press_key('s', a)

app.run()
