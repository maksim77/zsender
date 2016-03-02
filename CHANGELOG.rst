Zabbix Sender Changelog
=======================

0.2.5 (02.03.2015)
------------------

Features
~~~~~~~~

-  Add *clean* method to ZabbixPacket. After successful sending of the
   packet can not create a new instance, but just clean the old one. ###
   Bugfixes
-  Added check for valid timestamp values passed in the packet.
