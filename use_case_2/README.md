# Health Check Script
A daily health check script to make our day much more pleasant. The inital functions of this scripts are as follows:
* Checks Catalyst Center for overall network health
* Checks each client reporting a health score below 6 and reports relevant details
* Individual client check 


# Usage   

```
./healthcheck.py --help
****************************************************************
Welcome to the Catalyst Center Client Health Check Tool
****************************************************************
usage: healthcheck.py [-h] --username USERNAME [--mac MAC] [--interactive INTERACTIVE]

options:
  -h, --help            show this help message and exit
  --username USERNAME   username for access
  --mac MAC             Specific mac address to search for
  --interactive INTERACTIVE
                        Future Interactive mode

```

# Full Client Health Check

```
/healthcheck.py --username devnetuser
****************************************************************
Welcome to the Catalyst Center Client Health Check Tool
****************************************************************
Password:
Please wait....


Global Client Health Results
****************************************************************
┏━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃    ┃   scoreValue ┃   clientCount ┃   clientUniqueCount ┃   connectedToUdnCount ┃   unconnectedToUdnCount ┃ scoreCategory.scoreCategory   ┃ scoreCategory.value   ┃
┣━━━━╋━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━┫
┃  0 ┃            0 ┃             2 ┃                   2 ┃                     0 ┃                       0 ┃ CLIENT_TYPE                   ┃ ALL                   ┃
┗━━━━┻━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━┛

Specific Health Results
****************************************************************
┏━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃    ┃   scoreValue ┃   clientCount ┃   clientUniqueCount ┃   connectedToUdnCount ┃   unconnectedToUdnCount ┃ scoreCategory.scoreCategory   ┃ scoreCategory.value   ┃
┣━━━━╋━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━┫
┃  0 ┃           -1 ┃             2 ┃                   0 ┃                     0 ┃                       0 ┃ SCORE_TYPE                    ┃ POOR                  ┃
┣━━━━╋━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━┫
┃  1 ┃           -1 ┃             0 ┃                   0 ┃                     0 ┃                       0 ┃ SCORE_TYPE                    ┃ FAIR                  ┃
┣━━━━╋━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━┫
┃  2 ┃           -1 ┃             0 ┃                   0 ┃                     0 ┃                       0 ┃ SCORE_TYPE                    ┃ GOOD                  ┃
┣━━━━╋━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━┫
┃  3 ┃           -1 ┃             0 ┃                   0 ┃                     0 ┃                       0 ┃ SCORE_TYPE                    ┃ IDLE                  ┃
┣━━━━╋━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━┫
┃  4 ┃           -1 ┃             0 ┃                   0 ┃                     0 ┃                       0 ┃ SCORE_TYPE                    ┃ NODATA                ┃
┣━━━━╋━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━┫
┃  5 ┃           -1 ┃             0 ┃                   0 ┃                     0 ┃                       0 ┃ SCORE_TYPE                    ┃ NEW                   ┃
┗━━━━┻━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━┛
Please press any key to print client details with Poor/Fair health...


Please wait.....


Client Mac Address: 52:54:00:1C:E8:D6
┏━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━┓
┃    ┃ healthType   ┃ reason   ┃   score ┃
┣━━━━╋━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━┫
┃  0 ┃ OVERALL      ┃          ┃       1 ┃
┣━━━━╋━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━┫
┃  1 ┃ ONBOARDED    ┃          ┃       1 ┃
┣━━━━╋━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━┫
┃  2 ┃ CONNECTED    ┃          ┃       0 ┃
┗━━━━┻━━━━━━━━━━━━━━┻━━━━━━━━━━┻━━━━━━━━━┛


Client Mac Address: 52:54:00:1B:2F:9F
┏━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━┓
┃    ┃ healthType   ┃ reason   ┃   score ┃
┣━━━━╋━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━┫
┃  0 ┃ OVERALL      ┃          ┃       1 ┃
┣━━━━╋━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━┫
┃  1 ┃ ONBOARDED    ┃          ┃       1 ┃
┣━━━━╋━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━┫
┃  2 ┃ CONNECTED    ┃          ┃       0 ┃
┗━━━━┻━━━━━━━━━━━━━━┻━━━━━━━━━━┻━━━━━━━━━┛

No other clients with poor or fair scores

```
<br>
<br>

# Specific Mac Address Search
```
./healthcheck.py --username devnetuser --mac 52:54:00:1B:2F:9F
****************************************************************
Welcome to the Catalyst Center Client Health Check Tool
****************************************************************
Password:
Please wait.....


Client Mac Address: 52:54:00:1B:2F:9F
┏━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━┓
┃    ┃ healthType   ┃ reason   ┃   score ┃
┣━━━━╋━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━┫
┃  0 ┃ OVERALL      ┃          ┃       1 ┃
┣━━━━╋━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━┫
┃  1 ┃ ONBOARDED    ┃          ┃       1 ┃
┣━━━━╋━━━━━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━┫
┃  2 ┃ CONNECTED    ┃          ┃       0 ┃
┗━━━━┻━━━━━━━━━━━━━━┻━━━━━━━━━━┻━━━━━━━━━┛

No other clients with poor or fair scores
```








