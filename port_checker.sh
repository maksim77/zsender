#!/bin/bash
RESULT='init'
while [ $RESULT != 0 ]
do
 nc -z 127.0.0.1 10051 2>/dev/null >/dev/null
 RESULT=$?
done
