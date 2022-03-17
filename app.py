# coding:utf-8
import os, io
import codecs
import flask
from flask import render_template
import time
import json

from flask_script import Manager
from livereload import Server
from flask_apscheduler import APScheduler

import threading

import sendinfo
import subscribe

a = [0,0,0,0,0,0,0]
app = flask.Flask(__name__)
manager = Manager(app)

PWClast_status = 0
PW_dem_flag = 0
PW_dem_last = 0
PW_demandcal_15m = 0
PW_demandcal_1h = 0
ts_last = 0



class Config(object):
    JOBS = [
        {
            'id': 'read_ACinfo',
            'func': '__main__:read_ACinfo',
            'args': (4, 5),
            'trigger': 'interval',
            'seconds': 5
        }
    ]

def read_ACinfo(a, b): # send data to cloud
    ACPORT = '/dev/ttyS1'
    print(sendinfo.on_publish())

    
    
def ipc_subscribejob(ipc):
    subscribe.ipc_subscribe()

        
if __name__ == '__main__':
    
    app.config.from_object(Config())
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    
    first_thread = threading.Thread(target = ipc_subscribejob, args=("ipcjob",))
    first_thread.start()
    
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url_delay=True)
