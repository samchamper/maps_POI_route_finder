# Project 4:  Brevet time calculator with Ajax

Implementation of a brevit controle time calculator with flask and ajax.

## Author
Sam Champer  
schampe2@uoregon.edu  

Starter code by:  
Michal Young

## ACP controle times

That's "controle" with an 'e', because it's French, although "control"
is also accepted. Controls are points where a rider must obtain proof of passage, and control[e] times are the minimum and maximum times by which the rider must arrive at the location.   

The algorithm for calculating controle times is described at
https://rusa.org/octime_alg.html . Additional background information
is at https://rusa.org/pages/rulesForRiders .

This project functions similarly to the calculator at https://rusa.org/octime_acp.html , and is implemented using AJAX and Flask.   

## Usage  

To run, first copy credentials-skel.ini to the brevets folder and rename to credentials.ini, then run ```make start``` or create a virtual environment and then run flask_brevets.py in the brevets folder:
```
python3 -m venv env
pip install -r requirements.txt
cd brevets
python3 flask_brevets.py
```

## Testing

To run nosetests, first activate the virtual environment, then change directory to brevets and run nosetests:

```
. env/bin/activate
cd brevets
nosetests
```
