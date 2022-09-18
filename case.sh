#!/bin/bash

case $1 in
        start)
                echo "Service started"
                echo $$ > /tmp/case.pid
                sleep 9999
                ;;
        stop)
                id_my_script=`cat /tmp/case.pid`
                kill $id_my_script
                rm -f /tmp/case.pid
                echo "Service stopped"
                ;;
        restart)
                id_my_script=`cat /tmp/case.pid`
                kill $id_my_script
                rm -f /tmp/case.pid
                echo "Service stopped"
                echo "Service started"
                echo $$ | tee /tmp/case.pid
                sleep 9999
                ;;
        *)
                echo "Wrong argument! Enter start/stop/restart instead"
esac
