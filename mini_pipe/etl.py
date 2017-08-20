# -*- coding: utf-8 -*-
# python 3 



from datetime import datetime
from script import *
import time
import sys



def run_etl(time):
	with open("log/logfile.log", "a") as file:
		
		# start 
		start = datetime.datetime.now()
		msg = '{} - INFO - Hour - {} ETL start'.format( [str(datetime.datetime.now())],time)
		print (msg)
		file.write(msg) 
		# etl  
		print ('-------------')
		load(time)
		print ('-------------')
		# end 													 
		end = datetime.datetime.now()
		elapsed = (end-start).total_seconds() 
		msg = '{} - INFO - Hour - {} elapsed time: {} s'.format([str(datetime.datetime.now())],time,elapsed)
		print (msg)
		file.write(msg) 


if __name__ == '__main__':
	
	run_etl(sys.argv[1])
	print ('\n')







