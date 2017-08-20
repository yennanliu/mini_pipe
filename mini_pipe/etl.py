# -*- coding: utf-8 -*-
# python 3 



from datetime import datetime
from script import *
import time

#print (time)

def collect_log(time):
	with open("log/logfile.log", "a") as file:
		
		# start 
		start = datetime.datetime.now()
		msg = '{} - INFO - Hour - {} ETL start'.format( [str(datetime.datetime.now())],time)
		print (msg)
		file.write(msg) 
		# run tel 
		print ('-------------')
		load(time)
		print ('-------------')
		# end 													 
		end = datetime.datetime.now()
		elapsed = (end-start).total_seconds() 
		msg = '{} - INFO - Hour - {} elapsed time: {} s'.format([str(datetime.datetime.now())],time,elapsed)
		print (msg)
		file.write(msg) 



def run_etl(time):
	pass




"""

[2017-07-27 13:51:37,446] - INFO - Hour 2017-07-26-05 ETL start.
[2017-07-27 13:51:37,489] - INFO - Hour 2017-07-26-06 ETL start.
[2017-07-27 13:51:47,218] - INFO - Hour 2017-07-26-06 ETL complete, elapsed time: 10s.
[2017-07-27 13:51:48,491] - INFO - Hour 2017-07-26-05 ETL complete, elapsed time: 11s.
"""

if __name__ == '__main__':
	#load('2017-07-26-06')
	collect_log('2017-07-26-05')
	#run_etl('2017-07-26-05')            
