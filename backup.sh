#!/bin/sh
USERNAME="diomede"
PASSWORD="neru22da"
SERVER="192.168.1.181"
 
 
# local directory to pickup *.tar.gz file
FILE="readme"
 
# remote server directory to upload backup
BACKUPDIR="/Multimedia/timelapse"
 
# login to remote server
ftp -n -i $SERVER &lt;&lt;EOF
user $USERNAME $PASSWORD
cd $BACKUPDIR
mput $FILE
quit
EOF
