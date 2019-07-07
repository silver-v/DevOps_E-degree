#!/bin/bash

pwd
whoami

workdir=/home/silver/workdir/
backupdir=/home/silver/backupdir/
logdir=/var/log/date_backup

rsync -a $workdir $backupdir

echo "$(date) bachup is done" >> $logdir
