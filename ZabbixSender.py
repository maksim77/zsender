class ZabbixSender:
    def __init__(self, server, port):
        import socket
        self.s = socket.socket()
        self.server = server
        self.port = port

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

    def add(self, host, key, value):
        metric = {'host': host,
                  'key': key,
                  'value': value}
        self.packet['data'].append(metric)
