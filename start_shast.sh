#!/bin/bash

python beebox.py -s localhost -o 22243 &
python receiver.py &

