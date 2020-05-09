# Point of interest map and route calculator

## Author
Sam Champer  

Partially using code from:  
Michal Young

********

This program displays a points of interest within a specified distance of a dropped marker, or can calculate the route that traverses the most possible points of interest within the specified distance.

## Usage  

To run, first open credetials.ini in the maps folder. You'll need to provide a mapbox api key. Next, run ```make start``` or create a virtual environment and then run flask_maps.py in the maps folder:
```
python3 -m venv env
pip install -r requirements.txt
cd maps
python3 flask_maps.py
```
