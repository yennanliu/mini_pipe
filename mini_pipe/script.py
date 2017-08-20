# -*- coding: utf-8 -*-
# python 3 



import json
import datetime
import collections
import  csv
from collections import OrderedDict



def get_employer():
    with open('metadata/applicant_employer.json') as file:    
        data = dict(json.load(file))
    return data 

def get_nationality():
    with open('metadata/applicant_nationality.json') as file:
        data = dict(json.load(file))
    return data 

def get_nationality():
    with open('metadata/applicant_nationality.json') as file:
        data = dict(json.load(file))
    return data 
 
    
    
def load(date):
    employer = get_employer()
    nationality = get_nationality()
    righttowork = 'right_to_work/{}.csv'.format(date)
    identity = 'identity/{}.csv'.format(date)
    # get identy id 
    with open(identity,"rt") as f:
        reader = csv.reader(f, delimiter=',')
        identy_=[]
        for row in reader:
            identy_.append(row[1])
    with open(righttowork) as f:
        lines = f.readlines()
        for k in lines:
            identy_value = True if  k.split(",")[1] in identy_ else False
            value = datetime.datetime.fromtimestamp(float(k.split(",")[0]))
            keys = ['iso8601_timestamp',
                    'applicant_id',
                    'applicant_employer',
                    'applicant_nationality',
                    'is_eligble',
                    'is_verified']
            output = dict.fromkeys(keys,None)
            output=OrderedDict()
            output['iso8601_timestamp'] = value.strftime('%Y-%m-%d %H:%M:%S')
            output['applicant_id'] = k.split(",")[1]
            output['applicant_employer'] = employer[int(k.split(",")[2])]
            output['applicant_nationality'] = nationality[int(k.split(",")[3])]
            output['is_eligble'] = k.split(",")[4]
            output['is_verified'] = identy_value
            print(json.dumps(output))
 




            

    