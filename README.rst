Zabbix Sender
=============

Quick Start
-----------

Connection settings

.. code:: python

    from ZabbixSender import ZabbixSender, ZabbixPacket
    server = ZabbixSender('127.0.0.1', 10051)

Adds the values in the package. In the first example with the current
time, the second specified in unixtime format.

.. code:: python

    packet.add('myhost','key', 'value')
    packet.add('myhost2', 'other_key', 'value2', 1455607162)

Sending data

.. code:: python

    server.send(packet)
    print(server.status)

::

    {'info': 'processed: 2; failed: 0; total: 4; seconds spent: 0.207659',
     'response': 'success'}
