#!/bin/bash

# Replace these three settings.
PROJNAME="codeone"
PROJDIR="/var/lib/jenkins/workspace/$PROJNAME/"

PIDFILE="$PROJDIR/$PROJNAME.pid"
SOCKET="$PROJDIR/PROJNAME.sock"

cd $PROJDIR
if [ -f $PIDFILE ]; then
    kill `cat -- $PIDFILE`
    rm -f -- $PIDFILE
fi

source /home/alex/envs/test_env/bin/activate
exec python manage.py runfcgi socket=$SOCKET pidfile=$PIDFILE
