#!/bin/bash


oscgroups/bin/OscGroupClient 146.164.80.56 22242 22241 22243 22244 shast shast hiper4 nano &
sleep 5
python shast.py -s localhost -o 22243 &
python yun_receiver.py &

