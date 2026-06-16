#!/bin/bash
/entrypoint.sh &
sleep 3
cp /gemnet.html /var/www/html/gemnet.html
wait
