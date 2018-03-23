#!/bin/bash

echo "Setting swappiness to 10"
echo "vm.swappiness = 10" >> /etc/sysctl.conf
sysctl --system
