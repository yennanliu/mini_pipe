#!/bin/sh



function run_job () {

python etl.py 2017-07-26-05
python etl.py 2017-07-26-06 
}


function help_ () {
	echo
		"""
################################################################
# mini pipeline manual                                         #
################################################################

run etl job : 

chmod +x run.sh
./run.sh -r 

check commands :

chmod +x run.sh
./run.sh -h 

run parallel etl :

chmod +x run.sh
./run.sh -p 

 """
}


function parallel () {
echo "to be finished :P"
}


if [ -z "$1" ] || [[ "$1" != "-r"  && "$1" != "-h"  &&  "$1" != "-p" ]]
	then 
	echo "command not found, please use './run.sh -h' for more help "
fi 


case "$1"  in
	-r) run_job;; 
	-h) help_ ;;
	-p) parallel;;
esac 




