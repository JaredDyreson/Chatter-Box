#!/usr/bin/env bash


while true; do
    nohup python Webserver/Server.py &
    PID=`ps aux | grep "Server.py" | head -n1 | awk '{print $2}'`
    sleep 600 # every 10 minutes
    kill -9 "$PID"
    echo "[+] Killed $PID"
done
