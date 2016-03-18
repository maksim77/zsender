Zabbix Sender
=============

.. image:: https://badges.gitter.im/maksim77/zsender.svg
   :alt: Join the chat at https://gitter.im/maksim77/zsender
   :target: https://gitter.im/maksim77/zsender?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

|PyPI| |PyPI Count| |Build Status| |Coverage Status|

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
.. |Build Status| image:: https://travis-ci.org/maksim77/zsender.svg?branch=master
   :target: https://travis-ci.org/maksim77/zsender
.. |Coverage Status| image:: https://coveralls.io/repos/github/maksim77/zsender/badge.svg?branch=master
   :target: https://coveralls.io/github/maksim77/zsender?branch=master
