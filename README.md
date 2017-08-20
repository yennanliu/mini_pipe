
## Introduction

A mini pipeline schedule routine run jobs with log and output,
can be updated/modified flexibly 


## Structure

```
├── etl.py
├── identity
├── log
├── metadata
├── right_to_work
├── run.sh
└── script.py

script : utility, manipulate1 data 
etl    : main etl 
run    : shell that launch etl, can be put in crontab
log    : log location

```

## Tech
- Python 3.4.5, bash 


## Quick Start

```Bash
chmod +x run.sh
./run.sh -r 
```

### sample output 

```

['2017-08-20 20:27:28.894441'] - INFO - Hour - 2017-07-26-05 ETL start
-------------
{"iso8601_timestamp": "2017-07-26 05:36:39", "applicant_id": "1", "applicant_employer": "Tesco", "applicant_nationality": "British", "is_eligble": "true\n", "is_verified": true}
{"iso8601_timestamp": "2017-07-26 05:45:12", "applicant_id": "3", "applicant_employer": "ZipCar", "applicant_nationality": "Polish", "is_eligble": "false", "is_verified": false}
-------------
['2017-08-20 20:27:28.895948'] - INFO - Hour - 2017-07-26-05 elapsed time: 0.001498 s


['2017-08-20 20:27:28.960332'] - INFO - Hour - 2017-07-26-06 ETL start
-------------
{"iso8601_timestamp": "2017-07-26 06:12:45", "applicant_id": "2", "applicant_employer": "Deliveroo", "applicant_nationality": "Belgian", "is_eligble": "false\n", "is_verified": true}
{"iso8601_timestamp": "2017-07-26 06:07:32", "applicant_id": "5", "applicant_employer": "BlaBlaCar", "applicant_nationality": "French", "is_eligble": "true\n", "is_verified": true}
{"iso8601_timestamp": "2017-07-26 06:52:36", "applicant_id": "4", "applicant_employer": "Uber", "applicant_nationality": "Turkish", "is_eligble": "false", "is_verified": false}
-------------
['2017-08-20 20:27:28.962561'] - INFO - Hour - 2017-07-26-06 elapsed time: 0.002224 s

```


