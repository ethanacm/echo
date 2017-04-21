#!/bin/sh
# ON switch: BCM ?? (phys 36)
echo $1 > /sys/class/gpio/export 2> /dev/null
echo out > /sys/class/gpio/gpio$1/direction
echo 1 > /sys/class/gpio/gpio$1/value
# OFF switch: BCM ?? (phys 37)
echo $2 > /sys/class/gpio/export 2> /dev/null
echo out > /sys/class/gpio/gpio$2/direction
echo 1 > /sys/class/gpio/gpio$2/value