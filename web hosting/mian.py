# parth bansal
# https://github.com/parthbansal05
import time
import socket
from _thread import *
from flask import Flask, request, render_template
   
a=b=0 

def webhost(a,b):
    ip=socket.gethostbyname(socket.gethostname())
    global an

    app = Flask(__name__)
    @app.route('/sendparthge')
    def my_form():
        return render_template('t.html')

    @app.route('/sendparthge', methods=['POST'])
    def my_form_post():
        global an
        global an1
        global an2
        global an3
        global an4
        global an5
        an=request.form['iot_s']
        an1=request.form['room']
        an2=request.form['switch_c']
        an3=request.form['state']
        an4=request.form['time_i_t']
        an5=request.form['time_f_t']
        
        return render_template('a.html', age=an, bge=an1, cge=an2, dge=an3,ege=an4 ,fge=an5)

    app.debug = False
    app.run(host='127.0.0.1')

start_new_thread(webhost,(a,b))
while True:
    time.sleep(1000)