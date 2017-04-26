#!/bin/sh

function isrunning()
{
    pidof -s "$1" > /dev/null 2>&1
    status=$?
    if [[ "$status" -eq 0 ]]; then
        echo 1
    else
        echo 0
    fi
}
if [[ $(isrunning compton) -eq 1 ]]; then 
     pkill compton 
  else 
     compton -b
fi