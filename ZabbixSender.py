class ZabbixSender:
    def __init__(self, server='127.0.0.1', port='10051', config=''):
        import socket
        if config is not '':
            import re

            conf_file = open(config, 'r')
            re_server = re.compile('\\nServer=(\S*)\\n\\n')
            temp_server = re_server.search(conf_file.read())
            self.server = temp_server.groups()[0]
        else:
            self.server = server
        self.port = port
        self.s = socket.socket()

    def __str__(self):
        import json
        return json.dumps({'server': self.server,
                           'port': self.port},
                          indent=4)

    def send(self, data):
        data = str(data).encode('utf-8')
        self.s.connect((self.server, int(self.port)))
        self.s.send(data)
        result = self.s.recv(1024)
        return result


class ZabbixPacket:
    def __init__(self):
        self.packet = {'request': 'sender data',
                       'data': []}

    def __str__(self):
        import json
        return json.dumps(self.packet, indent=2)

    def add(self, host, key, value):
        # TODO: Add named attribute
        metric = {'host': host,
                  'key': key,
                  'value': value}
        self.packet['data'].append(metric)
