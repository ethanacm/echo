#!/bin/sh
# press the on button for a second and then release
# 0 is circuit-made  1 is circuit broken
echo out > /sys/class/gpio/gpio$1/direction
echo 0 > /sys/class/gpio/gpio$1/value
sleep 1
echo 1 > /sys/class/gpio/gpio$1/value


