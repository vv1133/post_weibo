#! /bin/bash

date=`date "+%D %A %T"`
tem=`cat /sys/class/thermal/thermal_zone0/temp | awk '{print $1/1000}'`
#echo $date
#echo $tem
/home/pi/weibo_post/post.py "$date ... CPU temperature: $tem degree Celsius. -- From Raspberry."
