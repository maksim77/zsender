import json
import re
import socket
import time


class ZabbixSender:
    def __init__(self, server='127.0.0.1', port='10051', config=None):
        if config is not None:
            conf_file = open(config, 'r')
            re_server = re.compile('\\nServer=(\S*)\\n\\n')
            temp_server = re_server.search(conf_file.read())
            conf_file.close()
            self.server = temp_server.groups()[0]
        else:
            self.server = server
        self.port = port
        self.status = ''

    def __str__(self):
        return json.dumps({'server': self.server,
                           'port': self.port},
                          indent=4)

    def send(self, packet):
        packet = str(packet).encode('utf-8')
        s = socket.socket()
        try:
            s.connect((self.server, int(self.port)))
        except Exception as e:  # TODO: Horrible! Rewrite immediately.
            print(e)
        s.send(packet)
        time.sleep(0.5)
        status = s.recv(1024).decode('utf-8')
        re_status = re.compile('(\{.*\})')
        status = re_status.search(status).groups()[0]
        self.status = json.loads(status)
        s.close()
