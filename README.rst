Zabbix Sender
=============

|PyPI| |PyPI Count|

Quick Start
-----------

Connection settings

.. code:: python

    from ZabbixSender import ZabbixSender, ZabbixPacket
    server = ZabbixSender('127.0.0.1', 10051)

Create a package and add the metric values. In the first example with
the current time, the second specified in unixtime format.

.. code:: python

    packet = ZabbixPacket()
    packet.add('myhost','key', 'value')
    packet.add('myhost2', 'other_key', 'value2', 1455607162)

Now we send our package in Zabbix Server

.. code:: python

    server.send(packet)

And see the delivery status

.. code:: python

    print(server.status)

::

    {'info': 'processed: 2; failed: 0; total: 4; seconds spent: 0.207659',
     'response': 'success'}

.. |PyPI| image:: https://img.shields.io/pypi/v/ZabbixSender.svg
   :target: https://pypi.python.org/pypi/ZabbixSender
.. |PyPI Count| image:: https://img.shields.io/pypi/dw/ZabbixSender.svg
   :target: https://pypi.python.org/pypi/ZabbixSender
