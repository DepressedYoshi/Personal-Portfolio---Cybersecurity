#!/bin/bash
if [ "$1" == "" ]
then 
	echo "you forgot to input an ip adresss to start the range of search"
	echo "Syntax: ./ipsweep"
else
for ip in `seq 1 254`; do 
	ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done
fi
