# Project 5: Point of interest map and route calculator

## Author
Sam Champer  
schampe2@uoregon.edu  

Some starter code by:  
Michal Young

********

This program displays a points of interest within a specified distance of a dropped marker, or can calculate the route that traverses the most possible routes in the specified distance.

## Usage  

To run, first copy credentials-skel.ini to the maps folder and rename to credentials.ini, then run ```make start``` or create a virtual environment and then run flask_maps.py in the maps folder:
```
python3 -m venv env
pip install -r requirements.txt
cd maps
python3 flask_maps.py
```

## Testing

To run nosetests, first activate the virtual environment, then change directory to maps and run nosetests:

```
. env/bin/activate
cd maps
nosetests
```

However, there are no nosetests yet!
