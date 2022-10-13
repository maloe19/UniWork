#!/bin/bash
#sleep NUMBER[s]
chmod +x scheduler.sh
#ToRun in Terminal(use git bash): ./scheduler.sh
#Extension: Code Runner
task_100ms(){
    f1=""
    echo "task 100ms running"
}
task_1s(){
    f2=""
    echo "task 1s running"
}
task_5s(){
    f3=""
    echo "task 5s running"
}
number="0"
f1=$( task_100ms )
f2=$( task_1s )
f3=$( task_5s )
#f1=task_100ms()
#f2=task_1s()
#f3=task_5s()
while [ "$f1" -lt 50 ]; do
    sleep 0.1
    number=$((number+1))
    if $f2 -e 10 ; then
        number==10
    fi
    #if [$f3 -e 50] then
        #$f3
    #fi
done
