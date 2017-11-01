# Project 5: Point of interest map and route calculator

## Author
Sam Champer  
schampe2@uoregon.edu  

Some starter code by:  
Michal Young

********

This program displays a list of points of interest. Or can calculate routes (not working yet).

## Usage  

To run, first copy credentials-skel.ini to the brevets folder and rename to credentials.ini, then run ```make start``` or create a virtual environment and then run flask_maps.py in the brevets folder:
```
python3 -m venv env
pip install -r requirements.txt
cd maps
python3 flask_maps.py
```

## Testing

To run nosetests, first activate the virtual environment, then change directory to brevets and run nosetests:

```
. env/bin/activate
cd brevets
nosetests
```
