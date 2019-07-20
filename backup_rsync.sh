#!/bin/bash

#enter the values of the working directory 
#and directory with backup 
#and location of the log file

#To automatically run the script, add the appropriate line to the crontab process 
#for an example: 0 0 * * * /home/user/backup_rsync.sh

workdir=/home/silver/workdir/
backupdir=/home/silver/backupdir/
logdir=/var/log/date_backup

rsync -a $workdir $backupdir

echo "$(date)- backup is done" >> $logdir
