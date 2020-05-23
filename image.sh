#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

echo $DATE

raspistill -rot 90 -o /home/pi/Documents/timeLapseRasp/image/$DATE.jpg
