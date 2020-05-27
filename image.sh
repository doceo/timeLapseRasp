#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

echo $DATE

raspistill -rot 120 -o /home/pi/Documents/timeLapseRasp/image/$DATE.jpg
