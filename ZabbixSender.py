class ZabbixSender:
    def __init__(self, server, port):
        import socket
        self.s = socket.socket()
        self.server = server
        self.port = port

    def __str__(self):
        import json
        return json.dumps({'server': self.server,
                           'port': self.port},
                          indent=4)

    def send(self, data):
        import json
        data = json.dumps(data)
        data = data.encode('utf-8')
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
        metric = {'host': host,
                  'key': key,
                  'value': value}
        self.packet['data'].append(metric)
