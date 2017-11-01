# Project 5: Point of interest map and route calculator

## Author
Sam Champer  
schampe2@uoregon.edu  

Some starter code by:  
Michal Young

********

This program displays a points of interest within a specified distance of a dropped marker, or can calculate routes (right now the cropping of points of interest to within a distance of the marker and the calculation of routes is not yet implemented).

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
